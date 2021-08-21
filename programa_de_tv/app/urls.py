from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('shows/<int:dato>/edit', views.edit),
    path('shows/<int:dato>', views.mostrar_id),
    path('shows/<int:dato>/destroy', views.eliminar),
    # path('shows/<int:dato>/update', views.update),
    # path('', views.index),
    
]
