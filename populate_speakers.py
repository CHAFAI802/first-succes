import os
import django
from django.core.files import File

# Configuration Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")  # Adapter 'project'
django.setup()

from test.models import SpeakerDetails, Session  # Adapter 'conference'

BASE_IMAGE_PATH = "media/speakers"

# Données des conférenciers
speakers_data = {
    "speaker-7.webp": {
        "full_name": "Michael Rodriguez",
        "title": "Director of innovation Strategy",
        "company": "TechForward Solutions",
        "years_experience": 15,
        "sessions_count": 3,
        "companies_advised": "200+",
        "quote": "Pushing boundaries through machine learning.",
        "biography": "lorem ipsum sit , consecteur elit , sed eiusmod tempor incididunt ut labore et dolore magna aliqua.Ut enim ad minim veniam , quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat .",
        #"expertise_areas": "Digital Strategy, Innovation Management,Tech leadership ,Business Transformation",
        "linkedin_url": "https://www.linkedin.com/in/jenniferwalsh",
        "twitter_url": "https://twitter.com/jwalsh_ai",
        "website_url": "https://jenniferwalsh.dev",
        "sessions": [
            {
                "session_type": "Workshop",
                "name": "ML for Production",
                "date": "2024-04-20",
                "time": "14:00",
                "location": "Room B",
                "attendees": 60,
                "summary": "Deploying ML models at scale."
            }
        ]
    },
    
      # Ajouter d'autres conférenciers ici avec le même format...
}

# Traitement
for filename, data in speakers_data.items():
    image_path = os.path.join(BASE_IMAGE_PATH, filename)

    if not os.path.exists(image_path):
        print(f"[❌] Image non trouvée : {image_path}")
        continue

    if SpeakerDetails.objects.filter(full_name=data["full_name"]).exists():
        print(f"[⏭️] {data['full_name']} déjà existant.")
        continue

    # Création des sessions liées
    session_objects = []
    for session_data in data.get("sessions", []):
        session_obj, created = Session.objects.get_or_create(
            name=session_data["name"],
            defaults={
                "session_type": session_data["session_type"],
                "date": session_data["date"],
                "time": session_data["time"],
                "location": session_data["location"],
                "attendees": session_data["attendees"],
                "summary": session_data["summary"],
            }
        )
        session_objects.append(session_obj)

    # Création de l'objet Speaker
    with open(image_path, "rb") as img_file:
        speaker = SpeakerDetails(
            full_name=data["full_name"],
            title=data["title"],
            company=data["company"],
            years_experience=data["years_experience"],
            sessions_count=data["sessions_count"],
            companies_advised=data["companies_advised"],
            quote=data["quote"],
            biography=data["biography"],
            expertise_areas=data["expertise_areas"],
            linkedin_url=data["linkedin_url"],
            twitter_url=data["twitter_url"],
            website_url=data["website_url"]
        )
        speaker.image.save(filename, File(img_file), save=True)
        speaker.save()

        # Ajout des sessions au M2M
        speaker.sessions.set(session_objects)
        print(f"[✅] {speaker.full_name} ajouté avec succès.")
