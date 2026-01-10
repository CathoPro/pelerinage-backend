from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File

VOCATIONS = [
    ('cardinal', 'Cardinal'),
    ('eveque', 'Évêque'),
    ('pretre', 'Prêtre'),
    ('diacre', 'Diacre'),
    ('religieux', 'Religieux'),
    ('religieuse', 'Religieuse'),
    ('seminariste', 'Séminariste'),
    ('laic', 'Laïc'),
]

class Pelerin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    diocese = models.CharField(max_length=100)
    paroisse = models.CharField(max_length=100, blank=True)
    vocation = models.CharField(max_length=20, choices=VOCATIONS)
    telephone = models.CharField(max_length=13)
    email = models.EmailField()
    photo = models.ImageField(upload_to="photos/")
    reference_paiement = models.CharField(max_length=100)
    qr_code = models.ImageField(upload_to="qrcodes/", blank=True)

    def save(self, *args, **kwargs):
        qr_data = f"{self.nom} {self.prenom} - {self.telephone}"
        qr_img = qrcode.make(qr_data)
        buffer = BytesIO()
        qr_img.save(buffer)
        self.qr_code.save(f"qr_{self.telephone}.png", File(buffer), save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
