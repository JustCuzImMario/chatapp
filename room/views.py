from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room, Message

@login_required
def chatrooms(request):
    chatrooms = Room.objects.all()

    return render(request, 'room/chatrooms.html', {'chatrooms': chatrooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room = room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})
