from django.contrib.auth.models import User, Group
from rest_framework import serializers

from hatchapp.models import Skill, UserProfile, Space, Post, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class SkillSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Skill

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = UserProfile

class SpaceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Space

class PostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Post

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
