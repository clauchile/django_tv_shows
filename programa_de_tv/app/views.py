from django.shortcuts import render, redirect
from .models import Show

def index(request):
    context = {
        'saludo': 'Hola'
    }
    return redirect('/shows')

def shows(request):

    if request.method == 'GET':
        context = {
        'programas' : Show.objects.all(), 

    }
    return render(request, 'shows.html', context)

def new(request):
    if request.method == 'GET':
        context = {
        
        }

        return render(request, 'new.html', context)

    if request.method == 'POST':
        print(request.POST)

        peli = Show.objects.create(
            title = request.POST['titulo'],
            network = request.POST['plataforma'],
            release_date = request.POST['release'],
            description = request.POST['descripcion'],
        )
        
        return redirect('/shows')    

def edit(request, dato):

    if request.method == 'GET':
        print(dato)
        context = {
        'editar' : Show.objects.get(id=dato) 
        }
        return render(request, 'edit.html', context)

    if request.method == 'POST':
        print(request.POST)
        change = Show.objects.get(id=dato)
        # print(change + "ok")

        change.title = request.POST['titulo']
        change.network = request.POST['plataforma']
        change.release_date = request.POST['release_date']
        change.description = request.POST['descripcion']

        change.save()
        return redirect(f"/shows/{dato}")

    #     		○ c = ClassName.objects.get(id=1)
    # c.field_name = "algún valor nuevo para field_name"
    # c.save()

def mostrar_id(request, dato):

    if request.method == 'GET':
    
        context = {
        # var : Show.objects.get(id = dato)
        'programas' : Show.objects.get(id = dato), 

    }


    print (Show.objects.get(id = dato))
    return render(request, 'showsid.html', context)

def eliminar(request, dato):
    print(request.GET)

    if request.method == 'GET':
        borrar = Show.objects.get(id=dato)
        borrar.delete()
        # borrar.save()
    return redirect(f"/shows") 
    # if request.method == 'GET':
    #     print(dato)
    #     context = {
    #     'editar' : Show.objects.get(id=dato) 
    #     }
    #     return render(request, 'edit.html', context)


