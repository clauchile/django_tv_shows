from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages


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


        if request.method == 'POST':
        # print(request.POST)
            errors = Show.objects.basic_validator(request.POST)
        # compruebe si el diccionario de errores tiene algo en él
        if len(errors) > 0:
        #     # si el diccionario de errores contiene algo, recorra cada par clave-valor y cree un mensaje flash
            for key, value in errors.items():
                messages.error(request, value)
                print(errors)
                # request.session['show_titulo'] = request.POST['id']
                request.session['show_titulo'] = request.POST['titulo']
                request.session['show_plataforma'] =request.POST['plataforma']
                request.session['show_release_date'] = request.POST['release_date']
                request.session['show_descripcion'] =request.POST['descripcion']
                
                
        #     # redirigir al usuario al formulario para corregir los errores
            return redirect('/shows/new')

        else:
            
            peli = Show.objects.create(
                title = request.POST['titulo'],
                network = request.POST['plataforma'],
                release_date = request.POST['release_date'],
                description = request.POST['descripcion'],
            )
            messages.add_message(request, 25 , f" el Show {request.POST['titulo']}, fue agregado con exito")
            request.session['show_titulo'] = ""
            request.session['show_plataforma'] = ""
            request.session['show_release_date'] = ""
            request.session['show_descripcion'] = ""
            
            return redirect('/shows')    

def edit(request, dato):

    if request.method == 'GET':
        # print(dato)
        context = {
        'editar' : Show.objects.get(id=dato) 
        }

        data = Show.objects.get(id = dato)
        print(f'{data.updated_at} + "aqui--->"') 
        return render(request, 'edit.html', context)

    if request.method == 'POST':
        # print(request.POST)
        errors = Show.objects.basic_validator(request.POST)
        # compruebe si el diccionario de errores tiene algo en él
        if len(errors) > 0:
        #     # si el diccionario de errores contiene algo, recorra cada par clave-valor y cree un mensaje flash
            for key, value in errors.items():
                messages.error(request, value)
                print(errors)
                # request.session['show_titulo'] = request.POST['id']
                request.session['show_titulo'] = request.POST['titulo']
                request.session['show_plataforma'] =request.POST['plataforma']
                request.session['show_release_date'] = request.POST['release_date']
                request.session['show_descripcion'] =request.POST['descripcion']
                
                
        #     # redirigir al usuario al formulario para corregir los errores
            return redirect(f'/shows/{dato}/edit')

        else:
            change = Show.objects.get(id=dato)
        #     # print(change + "ok")

            change.title = request.POST['titulo']
            change.network = request.POST['plataforma']
            change.release_date = request.POST['release_date']
            change.description = request.POST['descripcion']

            change.save()
            messages.add_message(request, 25 , f" el Show {dato}, fue actualizado con exito")
            request.session['show_titulo'] = ""
            request.session['show_plataforma'] = ""
            request.session['show_release_date'] = ""
            request.session['show_descripcion'] = ""


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
        messages.add_message(request, 20 , f" el Show {borrar.title}, fue eliminado con exito")

        # borrar.save()
    return redirect(f"/shows") 
    # if request.method == 'GET':
    #     print(dato)
    #     context = {
    #     'editar' : Show.objects.get(id=dato) 
    #     }
    #     return render(request, 'edit.html', context)

# def update(request, id):
#     # pasar los datos al método que escribimos y guardar la respuesta en una variable llamada errores
#     errors = Show.objects.basic_validator(request.POST)
#         # compruebe si el diccionario de errores tiene algo en él
#     if len(errors) > 0:
#         # si el diccionario de errores contiene algo, recorra cada par clave-valor y cree un mensaje flash
#         for key, value in errors.items():
#             messages.error(request, value)
#         # redirigir al usuario al formulario para corregir los errores
#         return redirect(f'/shows/+{id}')
#     else:
#         # si el objeto de errores está vacío, eso significa que no hubo errores.
#         # recuperar el blog para actualizarlo, realizar los cambios y guardar
#         show = Show.objects.get(id = id)
#         show.desc = request.POST['desc']
#         show.save()
#         show.name = request.POST['nombre']
#         messages.success(request, "Blog successfully updated")
#         # redirigir a la ruta de exito
#         return redirect('/shows')
