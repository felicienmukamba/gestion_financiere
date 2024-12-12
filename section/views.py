from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from section.models import Departement, Etudiant, Promotion, Section,Beneficiere
from .forms import BeneficiereForm, EtudiantForm, PromotionForm, SectionForm, DepartementForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.hashers import make_password

# section views.
def section_save(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True,  'message': 'Ajout de du section reussie!'}) 
    else:
        form = SectionForm()
    return JsonResponse({'success': False,  'message': 'POST only supported!'}, 400) 

def section_delete(request, id):
    try:
        section_on_database = Section.objects.get(pk=id) 
        section_on_database.delete() 
        return JsonResponse({'success': True,  'message': 'section supprimé avec succès!'}) 
    except Section.DoesNotExist:
        return JsonResponse({'success': False, 'message': "section non supprimé."}, status=404)

def section_edit(request,id ):
    section_to_edit = get_object_or_404(Section, pk=id)
    print(request.POST)
    if request.method == 'POST':
        designation = request.POST.get('designation') 
        section_to_edit.designation = designation
        section_to_edit.save()
        return JsonResponse({'success': True, 'message': "section modifiée avec succès."})
    else:
        return JsonResponse({'success': False, 'message': "Une erreur est survenue. Veuillez corriger les champs du formulaire."})


# Departement cours views.
def departement_save(request):
    if request.method == 'POST':
        form = DepartementForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True,  'message': 'Departement de du cours reussie!'}) 
    else:
        form = DepartementForm()
    return JsonResponse({'success': False,  'message': 'POST only supported!'}, 400) 

def departement_delete(request, id):
    try:
        departement_on_database = Departement.objects.get(pk=id) 
        departement_on_database.delete() 
        return JsonResponse({'success': True,  'message': 'departement supprimé avec succès!'}) 
    except Departement.DoesNotExist:
        return JsonResponse({'success': False, 'message': "departement non supprimé."}, status=404)
    
def departement_edit(request, id):
    departement_to_edit = get_object_or_404(Departement, pk=id)
    print(request.POST)
    if request.method == 'POST':
        designation = request.POST.get('designation')
        section = get_object_or_404(section, pk=request.POST.get('section'))
        departement_to_edit.designation = designation
        departement_to_edit.section = section
        departement_to_edit.save()
        return JsonResponse({'success': True, 'message': "Departement cours modifiée avec succès."})
    else:
        return JsonResponse({'success': False, 'message': "Une erreur est survenue. Veuillez corriger les champs du formulaire."})


def section_list(request):
    context = {
        'sections': Section.objects.all(),
    }

    return render(request, 'sections/list.html', context)


def departement_list(request):
    context = {
        'departements': Departement.objects.all(),
        'sections': Section.objects.all(),
    }

    return render(request, 'sections/departement/list.html', context)

# Vues pour les étudiants
class EtudiantListView(ListView):
    model = Etudiant
    context_object_name = "etudiants"
    template_name = 'etudiant/list.html'

class EtudiantCreateView(CreateView):
    model = Etudiant
    form_class = EtudiantForm
    template_name = 'etudiant/add.html'
    success_url = reverse_lazy('etudiant-list')

    def form_valid(self, form):
        # Hash the password
        return super().form_valid(form)


class EtudiantUpdateView(UpdateView):
    model = Etudiant
    form_class = EtudiantForm
    template_name = 'etudiant/edit.html'
    success_url = reverse_lazy('etudiant-list')


# promotion views.

def promotion_list(request):
    context = {
        'promotions': Promotion.objects.all(),
    }

    return render(request, 'promotions/list.html', context)

def promotion_save(request):
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True,  'message': 'Ajout de du promotion reussie!'}) 
    else:
        form = PromotionForm()
    return JsonResponse({'success': False,  'message': 'POST only supported!'}, 400) 

def promotion_delete(request, id):
    try:
        promotion_on_database = Promotion.objects.get(pk=id) 
        promotion_on_database.delete() 
        return JsonResponse({'success': True,  'message': 'promotion supprimé avec succès!'}) 
    except Promotion.DoesNotExist:
        return JsonResponse({'success': False, 'message': "promotion non supprimé."}, status=404)

def promotion_edit(request,id ):
    promotion_to_edit = get_object_or_404(Promotion, pk=id)
    print(request.POST)
    if request.method == 'POST':
        designation = request.POST.get('designation') 
        promotion_to_edit.designation = designation
        promotion_to_edit.save()
        return JsonResponse({'success': True, 'message': "promotion modifiée avec succès."})
    else:
        return JsonResponse({'success': False, 'message': "Une erreur est survenue. Veuillez corriger les champs du formulaire."})


class BeneficiereCreateView(CreateView):
    model = Beneficiere
    form_class = BeneficiereForm
    template_name = 'beneficiere/add.html'
    success_url = reverse_lazy('beneficiere-list')

    def form_valid(self, form):
        return super().form_valid(form)

class BeneficiereListView(ListView):
    model = Beneficiere
    context_object_name = "beneficieres"
    template_name = 'beneficiere/list.html'

class BeneficiereUpdateView(UpdateView):
    model = Beneficiere
    form_class = BeneficiereForm
    template_name = 'beneficiere/edit.html'
    success_url = reverse_lazy('Beneficiere-list')

