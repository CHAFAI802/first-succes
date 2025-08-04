from django.urls import path
from .  import views
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('',views.get_index,name='index'),
    path('about',views.get_about,name='about'),
    path('schedule',views.get_schedule,name='schedule'),
    path('speakers',views.get_speakers,name='speakers'),
    path ('venue',views.get_venue, name='venue'),
    path('speaker/<int:speaker_id>/', views.get_speakers_details, name='speakerdetails'),
    path('tickets',views.get_tickets,name='tickets'),
    path('buy-tickets',views.get_buy_tickets,name='buy-tickets'),
    path('gallery',views.get_gallery,name='gallery'),
    path('terms',views.get_terms,name='terms'),
    path('privacy',views.get_privacy,name='privacy'),
    path('404',views.get_four_o_four,name='404'),
    path('contact',views.get_contact,name='contact'),
    
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
