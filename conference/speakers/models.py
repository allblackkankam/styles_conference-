from django.db import models
from datetime import datetime

# Create your models here.
class Speakers(models.Model):
	name = models.CharField(max_length=200)
	job = models.CharField(max_length=200)
	about = models.TextField()
	twitter_handle = models.CharField(max_length=200)
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = 'Speakers'