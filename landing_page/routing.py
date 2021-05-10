#We need to create a routing configuration for the chat app that has a route to the consumer.
#Create a new file routing.py. Your app directory should now look like:


from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'landing_page/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]


#(Note we use re_path() due to limitations in URLRouter.)
