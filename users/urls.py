from django.urls import path
from .views import ProfileEditView

urlpatterns = [
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
]