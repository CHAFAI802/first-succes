from django.shortcuts import render,get_object_or_404,redirect
from .models import Speaker,SpeakerDetails,Session,Ticket
from .forms import TicketForm
from django.core.mail import send_mail
from django.conf import settings
from test.utils.file_handlers import handle_uploaded_file,generate_receipt_pdf
from test.services.paiment import traiter_paiement
from django.http import FileResponse


# Create your views here.


def get_index(request):
    return render(request,'parts/index.html')

def get_about(request):
    return render (request,'pages/about.html')

def get_schedule(request):
    return render (request ,'pages/schedule.html')

def get_speakers(request):
    speakers = Speaker.objects.all()
    return render (request ,'pages/speakers.html',{'speakers':speakers})

def get_venue(request):
    return render (request ,'pages/venue.html')



def get_speakers_details(request, speaker_id):
    speaker = get_object_or_404(SpeakerDetails, pk=speaker_id)
    expertise_list = speaker.get_expertise_list()
    sessions = speaker.sessions.all()

    context = {
        'speaker': speaker,
        'expertise_list': expertise_list,
        'sessions': sessions,
    }

    return render(request, 'pages/speaker-detail.html', context)


def get_tickets(request):
    return render(request,'pages/tickets.html')

    


#def get_tickets(request):
    #return render (request ,'pages/tickets.html')

def get_buy_tickets(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            # 1. Extraction des données
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            ticket_type = form.cleaned_data.get('ticket_type', 'standard')

            # 2. Création / enregistrement du ticket en base
            ticket = form.save(commit=False)  # On ne sauvegarde pas tout de suite
            ticket.save()  # Maintenant on a ticket.id

            # 3. Gestion du paiement ou de l'upload du reçu
            recu = request.FILES.get('recu')
            if recu:
                handle_uploaded_file(recu)
            else:
                success = traiter_paiement(form.cleaned_data)
                if not success:
                    form.add_error(None, "Échec du paiement.")
                    return render(request, 'pages/buy-tickets.html', {'form': form})

            # 4. Envoi de l’email de confirmation
            send_mail(
                subject="Confirmation de votre ticket",
                message=f"Bonjour {first_name},\n\nVotre inscription a été reçue pour le ticket : {ticket_type}.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )

            # 5. Redirection vers le téléchargement du PDF
            return redirect('download-receipt', ticket_id=ticket.id)

    else:
        form = TicketForm()
    return render(request, 'pages/buy-tickets.html', {'form': form})

def get_gallery(request):
    return render (request ,'pages/gallery.html')

def get_terms(request):
    return render (request ,'pages/terms.html')

def get_privacy(request):
    return render (request ,'pages/privacy.html')

def get_four_o_four(request):
    return render (request ,'pages/404.html')

def get_contact(request):
    return render (request ,'pages/contact.html')


def download_receipt(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    pdf_buffer = generate_receipt_pdf(ticket)
    return FileResponse(pdf_buffer, as_attachment=True, filename="recu_paiement.pdf")

