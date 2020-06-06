from django.urls import path
from .views import (
    user_profile,
    login_user,
    logout_user,
    save_profile,
)

app_name = 'profiles'

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('save-profile/', save_profile, name='save-profile'),
    path('', user_profile, name='index'),
]