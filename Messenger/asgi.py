"""
ASGI config for choco project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.routing import URLRouter,ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from message import routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Messenger.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket':AuthMiddlewareStack(URLRouter(routing.ws_urlpattern))
    # Just HTTP for now. (We can add other protocols later.)
})
