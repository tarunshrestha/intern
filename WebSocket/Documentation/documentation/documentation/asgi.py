"""
ASGI config for documentation project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from.consumer import *
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'documentation.settings')

application = ProtocolTypeRouter({
    "http":get_asgi_application(), # just a demo http ( We can add other protocols later.)
    "websocket":URLRouter([
        path('practice', PracticeConsumer.as_asgi())
        ])
    
    })

# ws = new WebSocket("ws://localhost:8000/practice");
# ws.onmessage = (data) => console.log(data.data);
# ws.send("PING");