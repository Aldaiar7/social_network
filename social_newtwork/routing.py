from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from django.core.asgi import get_asgi_application
import os
import django
import message.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social_newtwork.settings")
django.setup()


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(message.routing.websocket_urlpatterns)
        ),
    }
)
