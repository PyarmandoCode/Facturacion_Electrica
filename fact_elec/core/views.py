from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .models import Cliente

def index(request):
    template_name="Index.html"
    return render(request,template_name)

def Clientes_Listado(request):
    clientes=Cliente.objects.all() #Traer los clientes de la bd
    context = {
        "Clientes":clientes
    }
    template_name="Listado_clientes.html"
    return render(request,template_name,context)

def Cliente_form(request):
    template_name="Nuevo_Cliente.html"
    return render(request,template_name)

def CreateCrudClientes(request):
    response_data = {}
    template_name="Nuevo_cliente.html"
    if request.POST.get('action') =='registrar_cliente':
        try:
            #Recogiendo los datos del form
            nombre_cliente = request.POST.get('txtnomclie')
            cedula_cliente = request.POST.get('txtcedula')
            dir_cliente = request.POST.get('txtdirclie')
            tlf_cliente = request.POST.get('txttelclie')
            email_cliente = request.POST.get('txtemailclie')
            #/Grabas en el objeto clientes
 
            Cliente.objects.create(nombre=nombre_cliente,direccion=dir_cliente,cedula=cedula_cliente,telefono=tlf_cliente,email=email_cliente)
            
        except Exception as error:
            response_data['flag'] = False
            response_data['msg'] = f'No se Registro El Cliente Correctamente {error}'
        else:
            response_data['flag'] = True
            response_data['msg'] = 'Se Registro con exito El Cliente'   
        return JsonResponse(response_data)   
    return render(request,template_name)

class DeleteCrudClientes(View):
      def  get(self, request):
        id1 = request.GET.get('id', None)
        Cliente.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

def Cliente_visualizar(request,id):
    template_name = "Visualizar_cliente.html"
    cliente=Cliente.objects.get(id=id)
    context = {"cliente":cliente
               }
    return render(request, template_name,context) 

def UpdateCrudCliente(request):
    response_data = {}
    template_name="Visualizar_cliente.html"
    if request.POST.get('action') =='actualizar_cliente':
        try:
            id=request.POST.get('id')
            cliente = Cliente.objects.get(id=id)
            cliente.nombre=request.POST.get('txtnom')
            cliente.ruc=request.POST.get('txtcedula')
            cliente.direccion=request.POST.get('txtdir')
            cliente.telefono=request.POST.get('txtfono')
            cliente.email=request.POST.get('txtemail')
            cliente.save()
        except Exception as error:
            response_data['flag'] = False
            response_data['msg'] = f'No Se Modifico el Cliente Correctamente {error}'
        else:
            response_data['flag'] = True
            response_data['msg'] = 'Se Modifico con exito El Cliente'  
            
             
        return JsonResponse(response_data)   
    return render(request,template_name) 