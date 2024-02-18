from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('',views.IndexClassView.as_view(),name='index'),
    path('<int:pk>/',views.FoodDetail.as_view(), name='detail'),
     path('add/', views.CreateItem.as_view(), name='create_item'),
    path('edit/<int:pk>/', views.ItemUpdateView.as_view(), name='edit_item'),
    path('delete/<int:pk>/', views.ItemDeleteView.as_view(), name='delet_item'),

]

