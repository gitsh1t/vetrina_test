from django import template 
from ..models import Post, slider_1, slider_2
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown


register = template.Library()

#simple tags
#--------------------------------------------------------------------------------------------------------
@register.simple_tag
def totale_post():
    return Post.published.count()


#tag di inclusione
#-------------------------------------------------------------------------------------------------------
@register.inclusion_tag('landing_page/post/ultimi_post.html')
def post_più_recenti(count=10):
    ultimi_post = Post.published.order_by('-publish')[:count]
    return{'ultimi_post' : ultimi_post}    


#filtri
#-------------------------------------------------------------------------------------------------------
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))