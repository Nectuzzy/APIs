from django.contrib.auth.models import User
from links.serializers import LinkSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Link



# Create your views here.
class PostListApi(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = LinkSerializer

class PostCreateApi(generics.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailApi(generics.RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateApi(generics.UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteApi(generics.DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer