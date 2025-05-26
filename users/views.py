from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.shortcuts import render

class UserRegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/'


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')

class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'

def registration_success(request):
    return render(request, 'users/success.html')