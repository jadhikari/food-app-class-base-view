from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:item_id>/',views.detail, name='detail'),
    path('add/',views.create_item, name='create_item'),
    path('edit/<int:item_id>/',views.edit_item, name='edit_item'),
    
    path('delete/<int:item_id>/',views.delete_item, name='delet_item'),

]

