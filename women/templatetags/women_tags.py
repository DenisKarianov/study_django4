from django import template
from django.db.models import Count

import women.views as views
from women.models import Category, TagPost

register = template.Library()


@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(total=Count("posts")).filter(total__gt=0)
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('women/list_tags.html')
def show_all_tags():
    # tags = TagPost.objects.all()
    tags = TagPost.objects.annotate(total=Count("tags")).filter(total__gt=0)
    # tags_with_posts = [t for t in tags if t.tags.all()]  # len(t.tags.all()) > 0
    # for t in tags:
    #     if len(t.tags.all()) > 0:
    #         tags_with_posts.append(t)

    return {'tags': tags}