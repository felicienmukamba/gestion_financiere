from django.urls import path
from users.views import ProfileUpdateView, ProfileView, SignUpView, logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile-edit'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    # other paths
]
