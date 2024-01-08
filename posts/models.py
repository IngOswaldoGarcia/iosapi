from django.db import models
import uuid

# Create your models here.
class Posts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)