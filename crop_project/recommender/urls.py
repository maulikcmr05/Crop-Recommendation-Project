from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('signup/', signup_view, name='signup'),
    path('predict/', predict_view, name='predict'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login')
]