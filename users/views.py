from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import ProfileEditForm

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileEditForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('users:profile_detail')

    def get_object(self, queryset=None):
        return self.request.user

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user