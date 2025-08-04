from django.shortcuts import render,get_object_or_404
from .models import Speaker,SpeakerDetails,Session
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
    return render (request ,'pages/tickets.html')

def get_buy_tickets(request):
    return render (request ,'pages/buy-tickets.html')

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