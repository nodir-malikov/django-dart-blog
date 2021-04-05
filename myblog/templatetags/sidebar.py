from django import template
from myblog.models import Post, Tag
import random

register = template.Library()


@register.inclusion_tag('myblog/popular_posts_tpl.html')
def get_popular_posts(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}


@register.inclusion_tag('myblog/tag_tpl.html')
def get_tags(cnt=25):
    items = Tag.objects.order_by('posts__views')[:cnt]

    while items.count() < cnt:  # if tags less than we want we decrement 'cnt'
        cnt -= 1

    random_tags = random.sample(list(items), cnt)
    return {'tags': random_tags}
