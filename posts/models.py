from django.db import models
import uuid


def upload_to(instance, filename):
    return '/'.join(['files', str(instance.name), filename])
# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30)
    content = models.TextField()
    file = models.FileField(blank=True, null=True)
    file_name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    def __str___(self):
        return self.title