import re

from django import template
from django.http import HttpRequest
from django.template import RequestContext
from django.urls import reverse, NoReverseMatch

from ..models import TreeMenu

register = template.Library()


@register.inclusion_tag('app_menu/menu.html', takes_context=True)
def draw_menu(context: RequestContext, name: str = '', parent: int = 0):
    if parent != 0 and 'menu' in context:
        menu = context['menu']
    else:
        if 'request' in context and isinstance(context['request'], HttpRequest):
            current_path = context['request'].path
        else:
            current_path = ''

        tree_items = TreeMenu.objects.select_related().filter(category__name=name).order_by('pk')
        menu = []

        for item in tree_items:
            path = item.path.strip()
            target = '_self'

            if re.compile(r'^https?://').match(path):
                url = path
                target = '_blank'
            else:
                try:
                    url = reverse(path)
                except NoReverseMatch:
                    url = path

            menu.append({
                'id': item.pk,
                'url': url,
                'target': target,
                'name': item.name,
                'parent': item.parent_id or 0,
                'active': True if url == current_path else False,
            })

    return {
        'menu': menu,
        'current_menu': (item for item in menu if 'parent' in item and item['parent'] == parent),
    }
