from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Saying, SavedSayings, Reflections
from .serializers import SayingSerializer, SavedSayingSerializer, ReflectionSerializer
import random

@api_view(['GET'])
def daily_saying(request):
    shown_ids = request.session.get('shown_ids', [])

    # Optional: Filter by culture if passed as query param
    culture = request.query_params.get('culture')  # e.g., ?culture=Greek

    sayings_queryset = Saying.objects.exclude(id__in=shown_ids)
    if culture:
        sayings_queryset = sayings_queryset.filter(culture=culture)

    if not sayings_queryset.exists():
        shown_ids = []
        sayings_queryset = Saying.objects.all()
        if culture:
            sayings_queryset = sayings_queryset.filter(culture=culture)

    if not sayings_queryset.exists():
        return Response({"error": "No sayings available"}, status=404)

    saying = random.choice(list(sayings_queryset))
    shown_ids.append(saying.id)
    request.session['shown_ids'] = shown_ids

    serializer = SayingSerializer(saying)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_saying(request, saying_id):
    saying = get_object_or_404(Saying, id=saying_id)
    SavedSayings.objects.get_or_create(user=request.user, saying=saying)
    return Response({'message': 'Saying saved successfully'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_reflection(request, saying_id):
    saying = get_object_or_404(Saying, id=saying_id)
    content = request.data.get('content')

    if not content:
        return Response({'error': 'Content is required.'}, status=400)

    reflection = Reflections.objects.create(user=request.user, saying=saying, context=content)
    serializer = ReflectionSerializer(reflection)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_saved_sayings(request):
    saved = SavedSayings.objects.filter(user=request.user)
    serializer = SavedSayingSerializer(saved, many=True)
    return Response(serializer.data)