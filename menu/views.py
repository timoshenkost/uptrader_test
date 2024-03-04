from .models import MenuItem
from django.shortcuts import render


def menu_view(request, item_slug, menu_name):
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')

    # Создание списка родителей активного пункта меню
    active = next(item for item in menu_items if item.slug == item_slug)
    parent_list = [active]

    while active.parent:
        active = next(item for item in menu_items if item == active.parent)
        parent_list.append(active)

    parent_list.append(None)
    parent_list.reverse()

    return render(request, 'menu.html', {'menu_items': menu_items, 'parent_list': parent_list})
