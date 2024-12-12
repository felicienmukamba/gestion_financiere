from django import forms
from .models import Beneficiere, Etudiant, Promotion, Section, Departement


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = '__all__'


class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = '__all__'


class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['matricule', 'nom', 'postnom', 'prenom',
                  'sexe', 'telephone', 'departement', 'promotion']

    def __init__(self, *args, **kwargs):
        super(EtudiantForm, self).__init__(*args, **kwargs)
        # Disable editing of login field (assuming it should be unique and not changeable)
        self.fields["matricule"].widget.attrs.update(
            {"class": "form-control", "placeholder": "matricule"})
        self.fields["nom"].widget.attrs.update(
            {"class": "form-control", "id": "nom"})
        self.fields["postnom"].widget.attrs.update(
            {"class": "form-control", "placeholder": "postnom"})
        self.fields["prenom"].widget.attrs.update(
            {"class": "form-control", "placeholder": "prenom"})
        self.fields["sexe"].widget.attrs.update(
            {"class": "form-control", "placeholder": "sexe"})
        self.fields["telephone"].widget.attrs.update(
            {"class": "form-control", "placeholder": "telephone"})
        self.fields["departement"].widget.attrs.update(
            {"class": "form-control", "placeholder": "departement"})
        self.fields["promotion"].widget.attrs.update(
            {"class": "form-control", "placeholder": "promotion"})

    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        # Check for uniqueness (consider using a unique validator)
        if Etudiant.objects.filter(telephone=telephone).exists():
            raise forms.ValidationError('This phone number is already in use.')
        return telephone


class BeneficiereForm(forms.ModelForm):
    class Meta:
        model = Beneficiere
        fields = ['qualite', 'nom', 'postnom',
                  'prenom', 'sexe']

    def __init__(self, *args, **kwargs):
        super(BeneficiereForm, self).__init__(*args, **kwargs)
        # Disable editing of login field (assuming it should be unique and not changeable)
        self.fields["qualite"].widget.attrs.update(
            {"class": "form-control", "placeholder": "qualite"})
        self.fields["nom"].widget.attrs.update(
            {"class": "form-control", "id": "nom", "placeholder": "nom"})
        self.fields["postnom"].widget.attrs.update(
            {"class": "form-control", "placeholder": "postnom"})
        self.fields["prenom"].widget.attrs.update(
            {"class": "form-control", "placeholder": "prenom"})
        self.fields["sexe"].widget.attrs.update(
            {"class": "form-control", "placeholder": "sexe"})
