from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, UserListView, registration_success
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('list/', UserListView.as_view(), name='user_list'),
    path('success/', registration_success, name='registration_success'),
]
