from django.db import models

# Create your models here.
class Show(models.Model):
    title= models.CharField(max_length= 250)
    network= models.CharField(max_length= 250)
    release_date = models.DateTimeField()
    description = models.CharField(max_length= 250)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f"{self.title} ({self.network})"


    def __repr__(self):
        return f"{self.title}"