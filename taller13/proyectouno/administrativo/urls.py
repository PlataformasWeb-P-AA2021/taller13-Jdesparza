"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('obtener_edificio/<int:id>', views.obtener_edificio, name='obtener_edificio'),
    path('crear_edificio', views.crear_edificio, name='crear_edificio'),
    path('editar_edificio/<int:id>', views.editar_edificio, name='editar_edificio'),
    path('eliminar_edificio/<int:id>', views.eliminar_edificio, name='eliminar_edificio'),
    path('obtener_departamento/<int:id>', views.obtener_departamento, name='obtener_departamento'),
    path('crear_departamento', views.crear_departamento, name='crear_departamento'),
    path('editar_departamento/<int:id>', views.editar_departamento, name='editar_departamento'),
    path('eliminar_departamento/<int:id>', views.eliminar_departamento, name='eliminar_departamento'),
    path('crear_departamento_edificio/<int:id>', views.crear_departamento_edificio, name='crear_departamento_edificio'),
    path('saliendo/logout/', views.logout_view, name="logout_view"),
    path('entrando/login/', views.ingreso, name="login"),
]