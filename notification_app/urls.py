# notification_project/urls.py
from django.urls import path
from . import consumers
from django.contrib import admin
from django.urls import path, include


websocket_urlpatterns = [
    path('ws/notifications/', consumers.NotificationConsumer.as_asgi()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.notification_view, name='notification_view'),
    path('notifications/', include('notification_app.urls')),
]
