from rest_framework import serializers
from .models import Saying, SavedSayings, Reflections

class SayingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saying
        fields = '__all__'

class SavedSayingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = SavedSayings
        fields = '__all__'

class ReflectionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Reflections
        fields = '__all__'
