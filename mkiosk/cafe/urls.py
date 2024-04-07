from django.urls import path
from . import views

urlpatterns = [
    path('', views.rich_cafe, name='home'),
    path('coffee/', views.coffee_view, name='coffee'),
    path('tea/', views.tea_view, name='tea'),
    path('dessert/', views.dessert_view, name='dessert'),
    path('order/', views.order_view, name='order'),
]