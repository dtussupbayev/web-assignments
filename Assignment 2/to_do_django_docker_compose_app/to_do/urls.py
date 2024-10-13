from django.urls import path

from to_do import views

urlpatterns = [
    path('', views.to_do_list, name='to_do_list'),
    path('add/', views.add_to_do_item, name='add_to_do_item'),
    path('toggle_to_do_completed/<int:item_id>/', views.toggle_to_do_completed, name='toggle_to_do_completed'),
    path('delete/<int:item_id>/', views.delete_to_do_item, name='delete_to_do_item'),
]