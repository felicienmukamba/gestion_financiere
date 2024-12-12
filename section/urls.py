from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # section urls
    path("section/", views.section_list, name="section-list"),
    path("section-add/", views.section_save, name="section-add"),
    path("section-delete/<int:id>/", views.section_delete, name="section-delete"),
    path("section-edit/<int:id>/", views.section_edit, name="section-edit"),

    # departement urls
    path("departement/", views.departement_list, name="departement-list"),
    path("departement-add/", views.departement_save, name="departement-add"),
    path("departement-delete/<int:id>/",
         views.departement_delete, name="departement-delete"),
    path("departement-edit/<int:id>/",
         views.departement_edit, name="departement-edit"),

    # promotion urls
    path("promotion/", views.promotion_list, name="promotion-list"),
    path("promotion-add/", views.promotion_save, name="promotion-add"),
    path("promotion-delete/<int:id>/",
         views.promotion_delete, name="promotion-delete"),
    path("promotion-edit/<int:id>/", views.promotion_edit, name="promotion-edit"),

    # disponibilite urls
    path("etudiant-create/", views.EtudiantCreateView.as_view(), name="etudiant-add"),
    path("etudiant/", views.EtudiantListView.as_view(), name="etudiant-list"),
    path("etudiant-edit/<int:pk>/",
         views.EtudiantUpdateView.as_view(), name="etudiant-edit"),

         # disponibilite urls
    path("beneficiere-create/", views.BeneficiereCreateView.as_view(), name="beneficiere-add"),
    path("beneficiere/", views.BeneficiereListView.as_view(), name="beneficiere-list"),
    path("beneficiere-edit/<int:pk>/",views.BeneficiereUpdateView.as_view(), name="beneficiere-edit"),
]
