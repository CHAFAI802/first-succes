import os
from django.core.files.storage import FileSystemStorage
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
import io

def handle_uploaded_file(fichier):
    fs = FileSystemStorage(location='uploads/recus/')
    filename = fs.save(fichier.name, fichier)
    return fs.url(filename)

def generate_receipt_pdf(ticket):
    """
    Génère un PDF de reçu de paiement pour un ticket donné.

    Args:
        ticket: Objet contenant les attributs user, type, amount, date

    Returns:
        io.BytesIO: Buffer contenant le PDF
    """
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Titre principal
    p.setFont("Helvetica-Bold", 20)
    p.setFillColor(colors.HexColor("#333333"))
    p.drawCentredString(width / 2, height - 40 * mm, "Reçu de Paiement")

    # Ligne de séparation
    p.setStrokeColor(colors.HexColor("#999999"))
    p.setLineWidth(1)
    p.line(20 * mm, height - 45 * mm, width - 20 * mm, height - 45 * mm)

    # Détails du reçu
    p.setFont("Helvetica", 12)
    p.setFillColor(colors.black)

    y = height - 60 * mm
    line_spacing = 10 * mm

    p.drawString(30 * mm, y, f"Client : {ticket.user}")
    y -= line_spacing
    p.drawString(30 * mm, y, f"Type de ticket : {ticket.type}")
    y -= line_spacing
    p.drawString(30 * mm, y, f"Montant : {ticket.amount} €")
    y -= line_spacing
    p.drawString(30 * mm, y, f"Date : {ticket.date.strftime('%d/%m/%Y')}")

    # Bas de page
    p.setFont("Helvetica-Oblique", 10)
    p.setFillColor(colors.grey)
    p.drawCentredString(width / 2, 20 * mm, "Merci pour votre achat.")

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer
