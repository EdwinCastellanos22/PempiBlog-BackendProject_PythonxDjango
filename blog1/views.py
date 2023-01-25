from django.shortcuts import render
from .models import Profile, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('index/')
    else:
        return redirect('login/')

def index(request):
    posts= Post.objects.all()
    return render(request, 'index.html', {
        'posts':posts,
    })

def register(request):
    form= UserCreationForm(request.POST)
    profile = Profile()
    if request.method == "POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            profile.user= user
            profile.save()
            username= form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado con exito')
            return redirect('/index/')
        else:
            messages.error(request,'Por favor completa la informacion requerida')
            form= UserCreationForm()
    return render(request, 'register.html',{"form":form})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def profile(request):
    return render(request, 'profile.html')

def save(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post= Post()
            post.user_id= request.user.id
            post.title= request.POST['titulo']
            post.text= request.POST['texto']
            if request.POST['imagen']:
                post.post_image= request.POST['imagen']
            post.save()
            messages.success(request, "Pubicado")
            print("exito")
            return redirect('/index/')
        else:
            print("Error")
            return redirect('/index.html/')

def update_image(request):
    id= request.user.id
    perfil= Profile.objects.get(id= id)
    if request.method == 'POST':
        perfil.image= request.POST['image']
        perfil.save()
        messages.success(request, "Imagen de Perfil Actualizada")
    else:
        messages.error(request, "Error en la subida")
    return redirect('/profile/')

def update_profile(request):
    id= request.user.id
    user= User.objects.get(id =id)

    if request.method == 'POST':
        user.username= request.POST['username']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        messages.success(request, "Imagen de Perfil Actualizada")
    else:
        messages.error(request, "Error en la subida")
    return redirect('/index/')

def error_404(request, exception):
    return render(request, 'error404.html')

def error_500(request):
    return render(request, 'error500.html')

