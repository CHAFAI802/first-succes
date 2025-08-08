from django.contrib import admin
from .models import Speaker,SpeakerDetails,Session,Ticket
from . forms import TicketForm

# Register your models here.
admin.site.register(Speaker)
admin.site.register(SpeakerDetails)
admin.site.register(Session)
admin.site.register(Ticket)