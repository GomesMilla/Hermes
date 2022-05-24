from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Users.forms import UserForm

def view_login(request):
    if request.user.is_authenticated: return redirect('/')
    
    if request.method == "POST":
        user = authenticate(email = request.POST['username'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('LadingPage')
        else:
            messages.error(request, "Usuário ou senha inválidos!")
    
    context = {
        "name_page": "Hermes Technologys"
    }
    return render(request, 'Pages/Login.html', context)

def view_create_account(request):
    Formulario = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            objPessoa = form
            objPessoa.save()  
            return redirect("ViewLogin") 
        else:
            print(form.errors.as_data())
    else:
        form = UserForm()

    context = {
        "name_page" : "Create Account",
        "form" : form
    }
    return render(request, "Pages/CreateAccount.html", context)