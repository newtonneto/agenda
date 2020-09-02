from django.urls import path
from . import views

app_name = "contatos"

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new_contact, name='new_contact'),
    path('save', views.save_contact, name='save_contact'),
    path('<int:id>/edit', views.edit_contact, name='edit_contact'),
    path('<int:id>/save', views.save_edit_contact, name='save_edit_contact'),
    path('<int:id>/remove', views.remove_contact, name='remove_contact'),
]