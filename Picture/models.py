from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class FileUploaded(models.Model):
  title = models.CharField(max_length=50)
  upFile = models.FileField(upload_to="uploads")
  ct = models.CharField(max_length=20)
  thumbnail = ImageSpecField(
    source='upFile',
    processors=[ResizeToFill(100, 50)],
    format='JPEG',
    options={'quality': 80})
  
  def __unicode__(self):
    return self.upFile.name