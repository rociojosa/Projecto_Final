from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import UserEditForm, AvatarForm, User
from django.contrib.auth import login, authenticate
from Account.models import Avatar


def editar_usuario(request):

    user = request.user

    if request.method == 'POST':
        mi_formulario = UserEditForm(request.POST)
        if mi_formulario.is_valid: 

            informacion = mi_formulario.cleaned_data
            user.email = informacion['email']
            user.password1= informacion['password1']
            user.password2 = informacion['password2']
            user.save()

            return render(request, "AppFood/inicio.html")
    else:

        mi_formulario= UserEditForm(initial={'email':user.email})
    return render(request, "AppFood/editar_usuario.html", {"mi_formulario": mi_formulario, "usuario":user})


def register_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppFood/inicio.html", {"mensaje": "Usuario Creado"})
        
    else:

         form= UserCreationForm()

    return render(request, "AppFood/registro.html", {"form": form})


def login_account(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password= contra)

            if user is not None:
                login(request, user)

                return render(request, "AppFood/inicio.html", {"mensaje": f"Bienvenid@ {usuario}"})
            
            else:

                return render(request, "AppFood/inicio.html", {"mensaje": "Error, datos incorrectos"})
        else:

            return render(request, "AppFood/inicio.html", {"mensaje": "Error, formulario erroneo"})
        
    form = AuthenticationForm()
    context = {
        "form": form,
        "titulo": "Log In",
        "enviar": "Enviar"
    }
    return render(request, "AppFood/login.html", context = context)

def AgregarAvatar(request):
    if request.method == "POST":
        mi_formulario = AvatarForm(request.POST, request.FILES)
        if mi_formulario.is_valid:

            u = User.objects.get(surname=request.user)
            avatar = Avatar (user=u, imagen=mi_formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, "AppFood/inicio.html")
        else:

            mi_formulario= AvatarForm()
    return render(request, "AppFood/agregar_avatar.html", {"mi_formulario": mi_formulario})
    
