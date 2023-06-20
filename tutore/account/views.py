from django.contrib.auth import get_user_model, login, logout, authenticate, models
from django.shortcuts import render, redirect


User = get_user_model()

def signup(request):


    if request.method == "POST": # Traitement du formulaire 
                     
        username = request.POST.get("username")
        usermail = request.POST.get("usermail") #|____| recuperation des info du formulaire
        password = request.POST.get("password") #|
        
                                                 
        user = User.objects.create_user(username=username, email=usermail, password=password)
                                         

        login(request, user) #connexion au site
        return redirect('home') # admin.site.register(Shopper)rediriger vers la page daccueil


    return render(request, 'account/signup.html')

def login_user(request):
    if request.method == "POST": 

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')



    return render(request,'account/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

