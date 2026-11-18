from django.shortcuts import render, redirect

from recommender.ml.loader import predict_one
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not name or not email or not phone or not password:
            messages.error(request, 'Please fill in all fields.')
            return redirect('signup')
        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
            return redirect('signup')
        if User.objects.filter(username=email):
            messages.error(request, 'Email is already registered.')
            return redirect('signup')
        user = User.objects.create_user(username=email, password=password)
        if " " in name:
            first, last = name.split(" ", 1)
        else:
            first, last = name, ""
        user.first_name = first
        user.last_name = last
        user.save()

        UserProfile.objects.create(user=user, phone=phone)
        login(request, user)
        messages.success(request, 'Account created successfully! You are now logged in.')
        return redirect('predict')
    return render(request, 'signup.html')

from .ml.loader import predict_one,load_bundle
from django.contrib.auth.decorators import login_required
@login_required
def predict_view(request):
    feature_order = load_bundle()["feature_cols"]

    if request.method == 'POST':
        data = {}
        try:
            for c in feature_order:
                data[c] = float(request.POST.get(c))
        except (ValueError, TypeError):
            messages.error(request, 'Invalid input. Please enter valid numeric values.')
            return redirect('predict')

        label = predict_one(data)
        if not isinstance(label, str):
            label = label[0]
        label = str(label)

        Prediction.objects.create(user=request.user, predicted_label=label, **data)
        request.session['predict_result'] = {'result': label, 'last_data': data}
        messages.success(request, f"Prediction successful! Recommended Crop: {label}")
        return redirect('predict')
    saved = request.session.pop('predict_result', None)
    context = {
        'feature_order': feature_order,
        'result': saved['result'] if saved else None,
        'last_data': saved['last_data'] if saved else None,
    }
    return render(request, 'predict.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if not user:
            messages.error(request, 'Invalid Login Credentials.')
            return redirect('login')
        login(request, user)
        messages.success(request, 'Login successful!')
        return redirect('predict')
    return render(request, 'login.html')

@login_required
def user_history_view(request):
    predictions = Prediction.objects.filter(user=request.user)
    context = {
        'predictions': predictions
    }
    return render(request, 'history.html', context)
from django.shortcuts import get_object_or_404
@login_required
def user_delete_prediction(request, id):
    prediction = get_object_or_404(Prediction, id=id, user=request.user)
    prediction.delete()
    messages.success(request, 'Prediction deleted successfully.')
    return redirect('user_history')

@login_required
def profile_view(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()

        if not name or not phone or not email:
            messages.error(request, 'All fields are required.')
            return redirect('profile')

        # Check if email is taken by another user (since username stores email)
        if User.objects.filter(username=email).exclude(id=user.id).exists():
            messages.error(request, 'This email is already registered to another account.')
            return redirect('profile')

        # Split full name into first_name and last_name (matching signup_view)
        if " " in name:
            first, last = name.split(" ", 1)
        else:
            first, last = name, ""

        user.first_name = first
        user.last_name = last
        user.username = email
        user.email = email
        user.save()

        profile.phone = phone
        profile.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    full_name = f"{user.first_name} {user.last_name}".strip()
    total_predictions = Prediction.objects.filter(user=user).count()

    context = {
        'full_name': full_name,
        'phone': profile.phone,
        'email': user.username,
        'total_predictions': total_predictions,
    }
    return render(request, 'profile.html', context)

from django.contrib.auth import update_session_auth_hash

@login_required
def change_password_view(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not old_password or not new_password or not confirm_password:
            messages.error(request, 'Please fill in all fields.')
            return redirect('change_password')

        if not request.user.check_password(old_password):
            messages.error(request, 'Current password is incorrect.')
            return redirect('change_password')

        if len(new_password) < 8:
            messages.error(request, 'New password must be at least 8 characters long.')
            return redirect('change_password')

        if new_password != confirm_password:
            messages.error(request, 'New passwords do not match.')
            return redirect('change_password')

        if old_password == new_password:
            messages.error(request, 'New password cannot be the same as your current password.')
            return redirect('change_password')

        request.user.set_password(new_password)
        request.user.save()
        update_session_auth_hash(request, request.user)

        messages.success(request, 'Password changed successfully!')
        return redirect('profile')

    return render(request, 'change_password.html')

from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count

def is_admin(user):
    return user.is_authenticated and user.is_staff

def admin_login_view(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_dashboard')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            messages.success(request, 'Welcome back, Admin!')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid admin credentials or unauthorized account.')
            return redirect('admin_login')

    return render(request, 'admin_login.html')

import json
from django.db.models import Count, Avg

import json
from django.db.models import Count, Avg

@user_passes_test(is_admin, login_url='admin_login')
def admin_dashboard_view(request):
    total_users = User.objects.filter(is_staff=False).count()
    total_predictions = Prediction.objects.count()
    recent_predictions = Prediction.objects.select_related('user').order_by('-id')[:8]

    # 1. Crop Distribution (Top 8 Crops)
    top_crops = list(
        Prediction.objects.values('predicted_label')
        .annotate(count=Count('predicted_label'))
        .order_by('-count')[:8]
    )
    crop_labels = [item['predicted_label'].title() for item in top_crops]
    crop_counts = [item['count'] for item in top_crops]

    # 2. Average Soil N-P-K & Environmental Metrics
    averages = Prediction.objects.aggregate(
        avg_n=Avg('N'),
        avg_p=Avg('P'),
        avg_k=Avg('K'),
        avg_temp=Avg('temperature'),
        avg_hum=Avg('humidity'),
        avg_ph=Avg('ph'),
        avg_rain=Avg('rainfall'),
    )
    npk_values = [
        round(averages['avg_n'] or 0, 1),
        round(averages['avg_p'] or 0, 1),
        round(averages['avg_k'] or 0, 1),
    ]
    climate_values = [
        round(averages['avg_temp'] or 0, 1),
        round(averages['avg_hum'] or 0, 1),
        round((averages['avg_ph'] or 0) * 10, 1),  # Scaled x10 for visual comparison
        round(averages['avg_rain'] or 0, 1),
    ]

    # 3. Top Active Users (Horizontal Bar Chart)
    top_users = list(
        Prediction.objects.values('user__username', 'user__first_name', 'user__last_name')
        .annotate(count=Count('id'))
        .order_by('-count')[:5]
    )
    user_labels = [
        f"{u['user__first_name']} {u['user__last_name']}".strip() or u['user__username']
        for u in top_users
    ]
    user_counts = [u['count'] for u in top_users]

    # Avg Predictions per User KPI
    avg_per_user = round(total_predictions / total_users, 1) if total_users > 0 else 0

    context = {
        'total_users': total_users,
        'total_predictions': total_predictions,
        'avg_per_user': avg_per_user,
        'recent_predictions': recent_predictions,
        'top_crops': top_crops,
        'crop_labels_json': json.dumps(crop_labels),
        'crop_counts_json': json.dumps(crop_counts),
        'npk_values_json': json.dumps(npk_values),
        'climate_values_json': json.dumps(climate_values),
        'user_labels_json': json.dumps(user_labels),
        'user_counts_json': json.dumps(user_counts),
    }
    return render(request, 'admin_dashboard.html', context)

@user_passes_test(is_admin, login_url='admin_login')
def admin_users_view(request):
    users = User.objects.filter(is_staff=False).order_by('-date_joined')
    user_data = []
    for u in users:
        profile = UserProfile.objects.filter(user=u).first()
        pred_count = Prediction.objects.filter(user=u).count()
        user_data.append({
            'id': u.id,
            'full_name': f"{u.first_name} {u.last_name}".strip() or u.username,
            'email': u.username,
            'phone': profile.phone if profile else 'N/A',
            'date_joined': u.date_joined,
            'pred_count': pred_count,
        })

    return render(request, 'admin_users.html', {'users': user_data})

@user_passes_test(is_admin, login_url='admin_login')
def admin_delete_user(request, id):
    target_user = get_object_or_404(User, id=id, is_staff=False)
    target_user.delete()
    messages.success(request, 'User account deleted successfully.')
    return redirect('admin_users')

@user_passes_test(is_admin, login_url='admin_login')
def admin_predictions_view(request):
    predictions = Prediction.objects.select_related('user').order_by('-id')
    return render(request, 'admin_predictions.html', {'predictions': predictions})

@user_passes_test(is_admin, login_url='admin_login')
def admin_delete_prediction(request, id):
    prediction = get_object_or_404(Prediction, id=id)
    prediction.delete()
    messages.success(request, 'Prediction record deleted successfully.')
    return redirect('admin_predictions')