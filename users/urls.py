from django.urls import path
from users.views import ProfileUpdateView, ProfileView, SignUpView

urlpatterns = [
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile-edit'),
    # other paths
]
