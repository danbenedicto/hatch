from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from hatchapp.serializers import *
from hatchapp.models import Skill, UserProfile, Space, Post, Comment

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SkillViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Skills to be viewed or edited.
	"""
	queryset = Skill.objects.all()
	serializer_class = SkillSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows UserProfiles to be viewed or edited.
	"""
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer

class SpaceViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Spaces to be viewed or edited.
	"""
	queryset = Space.objects.all()
	serializer_class = SpaceSerializer

class PostViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Posts to be viewed or edited.
	"""
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Comments to be viewed or edited.
	"""
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
