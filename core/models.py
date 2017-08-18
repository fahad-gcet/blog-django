from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
	bio = models.TextField(max_length=500, blank=True, null=True)
	birth_date = models.DateField(blank=True, null=True)


class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField()
	body = models.TextField()
	posted_by = models.ForeignKey(settings.AUTH_USER_MODEL)

	def __str__(self):
		return self.title