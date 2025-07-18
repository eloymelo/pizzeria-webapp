from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    path('', views.index, name='index'),
    path('pizza/<int:pizza_id>/', views.pizza, name='pizza'),
    path('order/', views.order, name='order'),
]