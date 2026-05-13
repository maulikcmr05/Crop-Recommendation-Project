from django.shortcuts import render
import random

def home(request):

    crops = [
        "Rice",
        "Wheat",
        "Cotton",
        "Sugarcane",
        "Maize",
        "Barley"
    ]

    result = ""

    if request.method == "POST":
        result = random.choice(crops)

    return render(request, 'index.html', {'result': result})