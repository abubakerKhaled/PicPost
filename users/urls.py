from django.urls import path
from .views import ProfileEditView, ProfileDetailView

app_name = "users"

urlpatterns = [
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('profile/detail/', ProfileDetailView.as_view(), name='profile_detail'),
]