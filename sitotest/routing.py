from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import landing_page.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            landing_page.routing.websocket_urlpatterns
        )
    ),
})
# Channels
#ASGI_APPLICATION = 'sitotest.routing.application'