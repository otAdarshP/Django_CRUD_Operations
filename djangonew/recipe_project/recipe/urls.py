from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('create/', views.recipe_create, name='recipe_create'),
    path('<int:id>/edit/', views.recipe_edit, name='recipe_edit'),
    path('<int:id>/delete/', views.recipe_delete, name='recipe_delete'),
]
