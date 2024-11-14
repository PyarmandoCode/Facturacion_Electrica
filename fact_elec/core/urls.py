from django.urls import path
from .views import index,Clientes_Listado,Cliente_form,CreateCrudClientes,DeleteCrudClientes,Cliente_visualizar,UpdateCrudCliente

urlpatterns = [
    path('', index,name="index"),
    path('clientes_listado/', Clientes_Listado,name="clientes_listado"),
    path('cliente_form/', Cliente_form,name="cliente_form"),
    path('registrar_cliente/', CreateCrudClientes,name="registrar_cliente"),
    path('cliente_eliminar/', DeleteCrudClientes.as_view(),name="cliente_eliminar"),
    path('cliente_visualizar/<int:id>', Cliente_visualizar,name="cliente_visualizar"),
    path('cliente_actualizar/', UpdateCrudCliente,name="cliente_actualizar"),

]