from django.db import models
from uuid import uuid4

# Create your models here.
class Games(models.Model): 
    id_game = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='games')
    release_date = models.DateField()
    link = models.TextField()
    created_at = models.DateField(auto_now_add=True)
