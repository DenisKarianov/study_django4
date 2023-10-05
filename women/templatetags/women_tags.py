from django import template
import women.views as views
from women.models import Category, TagPost

register = template.Library()


@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('women/list_tags.html')
def show_all_tags():
    tags = TagPost.objects.all()
    tags_with_posts = []
    for t in tags:
        if len(t.tags.all()) > 0:
            tags_with_posts.append(t)

    return {'tags': tags_with_posts}