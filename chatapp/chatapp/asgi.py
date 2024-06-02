"""
ASGI config for chatapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

"""import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

django_asgi_application = get_asgi_application()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatapp.settings")
application = ProtocolTypeRouter({
    "http": django_asgi_application
})

ASGI_APPLICATION = 'chatapp.asgi.application'"""
import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTING_MODULE','chatapp.settings')

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from chat import routing

application = ProtocolTypeRouter(
    {
        "http":get_asgi_application(),
        "websocket":AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )
        )
    }
)
