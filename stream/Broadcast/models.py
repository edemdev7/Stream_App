from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

"""class User(AbstractUser):
    # Ajoutez ici des champs personnalisés si nécessaire
    pass"""

class Broadcast(models.Model):
    titre = models.CharField(max_length=100)
    url_flux_audio_video = models.URLField()
    heure_debut = models.DateTimeField(default=timezone.now)

    # Ajoutez d'autres champs pertinents ici, tels que la description, l'auteur, etc.
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='broadcast')

    def __str__(self):
        return self.titre
