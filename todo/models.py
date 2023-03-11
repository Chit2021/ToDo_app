from django.db import models

class ToDo(models.Model):
	text = models.CharField(max_length=300)
	done = models.BooleanField()