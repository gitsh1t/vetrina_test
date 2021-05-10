from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from .models import Post

class LatestPostFeed(Feed):
    title = "EDEN project"
    link = reverse_lazy('landing_page:post:list')
    description = 'Nuovo post sul blog!'

    def item(self):
        return Post.published.all()[:5]
		
    def item_title(self, item):
        return item.title
		
