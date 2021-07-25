from django.db import models
from django.shortcuts import render
from rest_framework import generics

from .models import Post
from .serializer import MealSerializer

class MealListView(generics.ListCreateAPIView):    
    serializer_class = MealSerializer
    queryset = Post.objects.all()

class MealDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MealSerializer
    queryset = Post.objects.all()