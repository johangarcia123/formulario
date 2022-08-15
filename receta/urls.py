from django.urls import path
from .views import insert, receta, delete_receta, update_from, update

urlpatterns = [
    path('', receta),  
    path("insert/", insert, name='insert'),
    path('update', update, name='update'),
    path('update/<int:receta_id>/', update_from, name='update_from'),
    path('delete_receta/<int:receta_id>/', delete_receta, name='delete_receta'),
    
]