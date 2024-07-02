from django.db import models

# Create your models here.


class Usuarios(models.Model):
    usu_user = models.CharField(primary_key=True, max_length=50)
    usu_clave = models.CharField(max_length=12)
    def __str__(self):
        return self.usu_user