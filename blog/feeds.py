import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from blog.models import Post
from django.utils import feedgenerator
import feedparser
from django.shortcuts import render

class LatestPostsFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('blog:post_list')
    description = 'New posts of my blog.'
    def items(self):
        post_feed = Post.published.all()[:5]
        return post_feed
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.body), 30)
    def item_pubdate(self, item):
        return item.publish
    
def post_feeds(request):
    feed = LatestPostsFeed()
    items = feed.items()
    li = []
    for item in items:
        vars = {}
        vars['title'] = feed.item_title(item)
        vars['pub'] = feed.item_pubdate(item)
        vars['desc'] = feed.item_description(item)
        li.append(vars)
    return render(request, 'blog/post/feed.xhtml', {'posts_lts': li})