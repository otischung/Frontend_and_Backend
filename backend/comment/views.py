from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from comment.models import Comment
from comment.serilalizers import CommentSerializer


class SimpleUserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        instance = Comment.objects.all().order_by("-created_at")
        serializer = CommentSerializer(instance, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data.copy()
        serializer = CommentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            data["author_id"] = request.user.id
            obj = serializer.create(data)
            return Response(data={"id": obj.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)