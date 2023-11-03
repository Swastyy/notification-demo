# notification_app/views.py
from django.shortcuts import render

def notification_view(request):
    return render(request, 'notification_app/notification.html')
