from io import BytesIO
from pathlib import Path
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from finance.models import Transaction
BASE_DIR = Path(__file__).resolve().parent.parent

class HomeView(View):
    def get(self, request):
        return render(request, 'app/home.html')


from django.http import HttpResponse
from reportlab.lib.pagesizes import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from io import BytesIO
from datetime import datetime
from pathlib import Path

def generate_pdf_view(request, transaction_id, entry=True):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="bon_de_caisse.pdf"'

    buffer = BytesIO()
    custom_height = 75 * mm  # Hauteur personnalisée de 148 mm
    p = canvas.Canvas(buffer, pagesize=(120 * mm, custom_height))  # Largeur A5, hauteur personnalisée
    width = 120 * mm
    height = custom_height

    # Définir les marges
    margin_left = 20
    margin_top = height - 40

    # Enregistrer les polices
    APTO_FONT = Path(BASE_DIR) / "staticfiles/fonts/Aptos.ttf"
    APTO_FONT_BOLD = Path(BASE_DIR) / "staticfiles/fonts/Aptos-Bold.ttf"
    pdfmetrics.registerFont(TTFont('Aptos', str(APTO_FONT)))
    pdfmetrics.registerFont(TTFont('Aptos-Bold', str(APTO_FONT_BOLD)))

    # Informations de l'entreprise
    company_name = "SCAI ISP BUKAVU"
    company_address = "ISP BUKAVU/VAMARO/IBANDA"
    company_phone = "+243995209133 / +243008336056"
    company_logo = Path(BASE_DIR) / "staticfiles/images/logo.png"  # Mettez le chemin correct du logo de l'entreprise

    # Informations du bon de caisse
    transaction = Transaction.objects.get(pk=transaction_id)
    account = transaction.account

    title = "Bon d'Entrée de Caisse" if entry else "Bon de Sortie de Caisse"
    amount = f"Montant : {transaction.amount}"
    print_date = datetime.now().strftime("%d/%m/%Y")
    user = request.user.username

    # Ajouter le filigrane
    p.saveState()
    p.setFont('Aptos-Bold', 40)
    p.setFillAlpha(0.1)
    p.drawCentredString(width / 2, height / 2, "ISP-BUKAVU")
    p.restoreState()

    # Ajouter la bordure
    p.setLineWidth(1)
    p.rect(10, 10, width - 20, height - 20)

    # Entête du document
    p.drawImage(str(company_logo), margin_left, height - 52, width=40, height=40)  # Logo de l'entreprise
    p.setFont('Aptos-Bold', 10)
    p.drawString(margin_left + 50, height - 20, company_name)
    p.setFont('Aptos', 8)
    p.drawString(margin_left + 50, height - 35, company_address)
    p.drawString(margin_left + 50, height - 50, company_phone)
    p.drawString(margin_left + 180, height - 20, f"Date d'impression: {print_date}")
    p.drawString(margin_left + 180, height - 35, f"Utilisateur: {user}")

    # Titre du bon de caisse
    p.setFont('Aptos-Bold', 12)
    p.drawString(margin_left, height - 80, title)

    # Détails de la transaction
    p.setFont('Aptos', 10)
    p.drawString(margin_left, height - 100, "Informations de la transaction:")
    p.drawString(margin_left, height - 115, f"Date : {transaction.date.strftime('%d/%m/%Y')}")
    p.drawString(margin_left, height - 130, f"Compte : {account.name}")
    p.drawString(margin_left, height - 145, f"Utilisateur : {transaction.user.username}")
    p.drawString(margin_left, height - 160, f"{amount}$")
    p.drawString(margin_left, height - 175, f"Description : {transaction.description}")

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def bon_entree(request, transaction_id):
    return generate_pdf_view(request, transaction_id, entry=True)

def bon_sortie(request, transaction_id):
    return generate_pdf_view(request, transaction_id, entry=False)
