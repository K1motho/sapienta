from rest_framework import serializers
from .models import Saying, SavedSayings, Reflections

class SayingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saying
        fields = '__all__'

class SavedSayingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedSayings
        fields = '__all__'

class ReflectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reflections
        fields = '__all__'
