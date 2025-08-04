import os
from django.core.files import File
import django

# Initialise Django si exécuté en dehors du shell
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")  # remplace 'project' si besoin
django.setup()

from test.models import Speaker  # Remplace 'test' si ton app porte un autre nom

BASE_IMAGE_PATH = "media/speakers"

speakers_data = {
    "speaker-4.webp": {
        "name": "Jennifer Walsh",
        "position": "Senior Data Scientist",
        "organization": "DataVision Labs",
        "track": "Machine Learning",
        "topic": "Advanced Neural Networks in Real-World Applications",
        "summary": "Exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit voluptate.",
    },
    "speaker-1.webp": {
        "name": "Kamal BABORI",
        "position": "Blockchain Architect",
        "organization": "CryptoTech Solutions",
        "track": "Technology",
        "topic": "Decentralized Finance: Building the Future",
        "summary": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium totam rem aperiam.",
    },
    "speaker-5.webp": {
        "name": "Dr. Sophia Chen",
        "position": "Innovation Director",
        "organization": "FutureTech Institute",
        "track": "Innovation",
        "topic": "Sustainable Technology Solutions for Tomorrow",
        "summary": "Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit sed quia consequuntur magni dolores.",
    },
    "speaker-10.webp": {
        "name": "Robert Martinez",
        "position": "UX Research Lead",
        "organization": "Design Collective",
        "track": "Design",
        "topic": "Human-Centered Design in Digital Products",
        "summary": "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque.",
    },
    "speaker-13.webp": {
        "name": "Amanda Foster",
        "position": "Growth Strategist",
        "organization": "ScaleUp Partners",
        "track": "Business",
        "topic": "Scaling Digital Businesses in 2024",
        "summary": "Corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident similique sunt.",
    },
    "speaker-14.webp": {
        "name": "Kevin Park",
        "position": "Digital Marketing Expert",
        "organization": "Growth Agency Pro",
        "track": "Marketing",
        "topic": "Next-Gen Marketing Automation Strategies",
        "summary": "Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae.",
    },
}

for filename, data in speakers_data.items():
    image_path = os.path.join(BASE_IMAGE_PATH, filename)

    if not os.path.exists(image_path):
        print(f"Image non trouvée : {image_path}")
        continue

    if Speaker.objects.filter(name=data["name"]).exists():
        print(f"{data['name']} déjà existant, ignoré.")
        continue

    with open(image_path, "rb") as img_file:
        speaker = Speaker(
            name=data["name"],
            position=data["position"],
            organization=data["organization"],
            track=data["track"],
            topic=data["topic"],
            summary=data["summary"],
        )
        speaker.photo.save(filename, File(img_file), save=True)
        print(f"{data['name']} ajouté avec succès.")
