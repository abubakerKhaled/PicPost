from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from models import CustomUser
from forms import ProfileEditForm

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileEditForm
    template_name = 'account/profile_edit.html'
    success_url = reverse_lazy('profile_detail')  # Create this URL

    def get_object(self, queryset=None):
        return self.request.user
