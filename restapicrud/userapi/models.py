from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    contact = models.CharField(max_length = 15 )
