from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Saying, SavedSayings, Reflections
from .serializers import SayingSerializer, SavedSayingSerializer, ReflectionSerializer
import random

@api_view(['GET'])
def daily_saying(request):
    shown_ids = request.session.get('shown_ids', [])
    available = Saying.objects.exclude(id__in=shown_ids)

    if not available.exists():
        shown_ids = []
        available = Saying.objects.all()

    saying = random.choice(list(available))
    shown_ids.append(saying.id)
    request.session['shown_ids'] = shown_ids

    serializer = SavedSayings(saying)
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
    reflection = Reflections.objects.create(user=request.user, saying=saying, content=content)
    serializer = ReflectionSerializer(reflection)
    return Response(serializer.data)
