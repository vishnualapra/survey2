from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import serializers
from rest_framework.permissions import BasePermission
from rest_framework import viewsets
from master import models


class Survey(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.GetSurveySerializer

class Choice(viewsets.ModelViewSet):
    queryset = models.Choises.objects.all()
    serializer_class = serializers.ChoiceSerializer


class Result(viewsets.ModelViewSet):
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer
    