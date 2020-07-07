from django.contrib.syndication.views import Feed

from .models import Post


class AllPostsFeed(Feed):
    title = '周末小站'
    link = '/'
    description = '周末小站的全部文章'

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return item.body_html
