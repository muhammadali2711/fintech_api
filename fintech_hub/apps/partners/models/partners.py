from django.db import models
from uuid import uuid4


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'partners/{name}'.format(
        user_id=str(instance.id), name='{}.{}'.format(uuid4().hex, ext))
    return file_path


class PartnersModel(models.Model):
    image = models.ImageField(upload_to=upload_location, blank=True)

    def __str__(self):
        return str(self.id)


