from rest_framework import serializers
from rest_framework import exceptions, response
from rest_framework.validators import UniqueValidator
from master import models
from rest_framework.response import Response
import json


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','choice','question')
        model = models.Choises


class GetSurveySerializer(serializers.ModelSerializer):
    choices = serializers.SerializerMethodField('get_choices',read_only=True)
    def get_choices(self,dat):
        ch = models.Choises.objects.filter(question_id=dat.id)
        ser = ChoiceSerializer(ch,many=True)
        return ser.data
    class Meta:
        fields = ('id','title','is_multiple','is_mandatory','choices')
        model = models.Question


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = models.Result