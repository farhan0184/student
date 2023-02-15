from django.db import models

# Create your models here.
class Info(models.Model):
  name = models.CharField(max_length=122)
  email = models.CharField(max_length=120)
  department = models.CharField(max_length=10)
  section = models.CharField(max_length=8)
  date = models.DateField()
  # code to show name of the person who sent you the message
  def _str_(self):
    return self.name