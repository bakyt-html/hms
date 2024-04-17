from django.http import HttpResponse
from django.shortcuts import render

from .models import Room, RoomPhoto

def room_list(request):
    rooms = Room.objects.all()

    return render(request, 'hotel_app/room_list.html', {'rooms':rooms})


def base_page(request):
    return render(request, 'hotel_app/base.html')

def main_page(request):
    return render(request, 'hotel_app/main.html')

def room_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    data = {
        'room': room
    }
    return render(request, 'hotel_app/room_detail.html', data)