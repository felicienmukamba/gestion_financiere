from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core import settings
from core.views import HomeView
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import bon_entree, bon_sortie


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('bon_entree/<int:transaction_id>/', bon_entree, name='bon_entree'),
    path('bon_sortie/<int:transaction_id>/', bon_sortie, name='bon_sortie'),
    path("", include("finance.urls")),
    path("", include("users.urls")),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns += staticfiles_urlpatterns()