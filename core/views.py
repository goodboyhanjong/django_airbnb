from urllib import response
from django.core import serializers
import json
from django.http import HttpResponse
from rooms.models import Room


def list_rooms(request):
    data = serializers.serialize("json", Room.objects.all())
    response = HttpResponse(content=data)
    return response
