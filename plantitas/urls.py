from django.urls import path
from .views import Inicio,organizacion,Productos,Formulario,Api,Ver,crear,eliminar,modificar, registrar

urlpatterns=[
    path('', Inicio, name="Inicio"),
    path('organizacion/', organizacion, name="organizacion"),
    path('Productos/', Productos, name="Productos"),
    path('Formulario/', Formulario, name="Formulario"),
    path('Api/', Api, name="Api"),
    path('Ver/', Ver, name="Ver"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('registrar/', registrar, name="registrar"),
]