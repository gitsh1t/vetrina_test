"""
ASGI config for sitotest project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""
import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.http import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sitotest.settings')

application = ProtocolTypeRouter({ 
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(URLRouter(sitotest.routing.websocket_urlpatterns)),
    })
