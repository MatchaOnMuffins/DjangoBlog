from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
import sqlite3

from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import EditProfileForm
from django.contrib.auth.decorators import login_required


class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class UpdateProfile(generic.UpdateView):
    form_class = EditProfileForm
    success_url = reverse_lazy('login')
    template_name = 'registration/update_profile.html'

    def get_object(self, queryset=None):
        return self.request.user


class ShowProfile(generic.DetailView):
    model = User
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        users = User.objects.all()
        context = super().get_context_data(**kwargs)

        page_user = get_object_or_404(User, id=self.kwargs['pk'])

        context['page_user'] = page_user

        return context

    def get_object(self, queryset=None):
        return self.request.user

