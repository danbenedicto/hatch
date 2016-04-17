from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Skill(models.Model):
	name = models.CharField(max_length=24, unique=True)

	def __str__(self):
		return self.name

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	skills = models.ManyToManyField(Skill)

	def __str__(self):
		return self.name + " profile"

class Space(models.Model):
	name = models.CharField(max_length=24, unique=True)
	description = models.CharField(max_length=140)

	def __str__(self):
		return self.name

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.description[:10]

class Comment(models.Model):
	text = models.CharField(max_length=140)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	def __str__(self):
		return self.text[:10]
