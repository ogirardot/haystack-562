from django.db import models

class Data(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now=True)