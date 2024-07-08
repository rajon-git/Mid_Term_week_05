from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login, update_session_auth_hash, logout
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from car.models import Order

# Create your views here.
def register(request):
    if request.method == 'POST':
        register_forms = forms.RegistrationForm(request.POST)
        if register_forms.is_valid():
            register_forms.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')
    else:
        register_forms = forms.RegistrationForm()
    return render(request, 'register.html', {'form': register_forms})

class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self,form):
        messages.success(self.request, 'Logged in successfull')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.UserDataChangeForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Account update successfully')
            return redirect('profile')
    else:
        profile_form = forms.UserDataChangeForm(instance =  request.user)
    return render(request, 'update_profile.html', {'form': profile_form})

@login_required
def change_password(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(request.user, data = request.POST)
        if pass_form.is_valid():
            pass_form.save()
            messages.success(request, 'Password chanfe successfully')
            update_session_auth_hash(request, pass_form.user)
            return redirect('profile')
    else:
        pass_form = PasswordChangeForm(user = request.user)
    return render(request, 'pass_change.html', {'form': pass_form})

@login_required
def profile(request):
    data = Order.objects.filter(user= request.user)
    return render(request, 'profile.html', {'data':data})

def user_logout(request):
    logout(request)
    return redirect('login')
    