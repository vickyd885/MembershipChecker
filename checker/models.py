from django.db import models

# Create your models here.

class Member(models.Model):
    value = models.CharField(max_length=300)
    def __unicode__(self):
        return self.value

