from django.contrib import admin

from section.models import Departement, Qualite, Section,Etudiant,Beneficiere

# Register your models here.
admin.site.register(Section)
admin.site.register(Departement)
admin.site.register(Etudiant)
admin.site.register(Beneficiere)
admin.site.register(Qualite)
