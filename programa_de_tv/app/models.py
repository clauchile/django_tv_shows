from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData['titulo']) < 2:
            errors["largo_titulo"] = "El título debería tener al menos 2 carácteres"
        if len(postData['plataforma']) < 3:
            errors["largo_plataforma"] = "La plataforma debe tener al menos 3 caracteres"
        if len(postData['descripcion']) >0:
            if len(postData['descripcion'])<10 :
        # if len((postData['descripcion'] >0) & len(postData['descripcion'] <10)):
                errors["largo_descripcion"] = "La descripción debería tener al menos 10 caracteres"
        if Show.objects.filter(title=postData['titulo']).exists():
            errors['titulo_existe'] ='El titulo ya existe, favor ingresar otro'

        return errors
# Create your models here.
class Show(models.Model):
    title= models.CharField(max_length= 250)
    network= models.CharField(max_length= 250)
    release_date = models.DateTimeField()
    description = models.CharField(max_length= 250)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects= ShowManager() 

    def __str__(self):
        return f"{self.title} ({self.network})"


    def __repr__(self):
        return f"{self.title}"

