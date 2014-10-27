from django.db import models

# Create your models here.
class FileUploaded(models.Model):
  title = models.CharField(max_length=50)
  upFile = models.FileField(upload_to="uploads")
  ct = models.CharField(max_length=20)
  
  def __unicode__(self):
    return self.upFile.name