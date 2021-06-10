from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Comment


class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at']

    author = UsernameSerializer(read_only=True, default=serializers.CurrentUserDefault())

    def validate_content(self, val):
        if len(val) > 200:
            raise ValidationError("content too long")
        return val

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)