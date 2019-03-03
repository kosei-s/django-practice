from django.db import models

class Train(models.Model):
    line = models.CharField(max_length=255)
