from .models import SpeakerDetails

def featured_speaker_context(request):
    return {
        'featured_speaker': SpeakerDetails.objects.first()
    }
