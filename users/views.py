from django.shortcuts import render,  redirect
from django.contrib.auth import get_user_model
from django.views.generic import View, UpdateView, DetailView

from .forms import RegisterForm
from .models import Profile

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user = form.save(commit=False)
            # user.is_active = False
            user.save()
            user.profile.first_name = first_name
            user.profile.last_name = last_name
            user.save()
            return redirect('users:login')
        return redirect('users:register')


class ProfileView(DetailView):
    model = Profile
    template_name = 'users/profile.html'


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ('first_name', 'last_name', 'image', 'location', 'about_me', 'phone')






