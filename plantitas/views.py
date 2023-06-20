from django.shortcuts import render, redirect
from .models import Stock, Categoria
from .forms import StockForm, RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.

def Inicio(request):
    return render(request, 'Inicio.html')

def organizacion(request):
    return render(request,'organizacion.html')

def Productos(request):
    jardin = Stock.objects.all()
    datos = {
        'jardin': jardin
    }
    return render(request,'Productos.html', datos)

def Formulario(request):
    return render(request,'Formulario.html')

def Api(request):
    return render(request,'Api.html')

@login_required
def Ver(request):
    plantitas = Stock.objects.all()
    datos = {
        'jardin': plantitas
    }
    return render(request,'Stock.html', datos)

@login_required
def crear(request):
    if request.method=="POST":
        stockForm = StockForm(request.POST, request.FILES)
        if stockForm.is_valid():
            stockForm.save()     #similar al insert
            return redirect('Ver')
    else:
        stockForm=StockForm()
    return render(request, 'crear.html', {'stock_Form':stockForm})


@login_required
def eliminar(request, id):
    stockEliminado = Stock.objects.get(code=id) #obtenemos un objeto por su id
    stockEliminado.delete()
    return redirect ('Ver')


@login_required
def modificar(request, id):
    stockModificado=Stock.objects.get(code=id)
    datos = {
        'form' : StockForm(instance=stockModificado)
    }
    if request.method=='POST':
        formulario = StockForm(data=request.POST, instance=stockModificado)
        if formulario.is_valid:
            formulario.save()
            return redirect('Ver')
    return render(request, 'modificar.html', datos)


def registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect ('Inicio')
        data["form"] = formulario
    return render(request, 'registration/registrar.html',data)