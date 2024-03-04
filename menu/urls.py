from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('<str:menu_name>/<slug:item_slug>/', views.menu_view, name='menu_item'),
]