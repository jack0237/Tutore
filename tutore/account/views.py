from django.contrib.auth import get_user_model, login, logout, authenticate, models
from django.shortcuts import render, redirect

#User = models.User
User = get_user_model()

def signup(request):


    if request.method == "POST": # Traitement du formulaire 
                     
        username = request.POST.get("username")
        usermail = request.POST.get("usermail") #|____| ecuperation des info du formulaire
        password = request.POST.get("password") #|
        
                                                 
        user = User.objects.create_user(username=username, email=usermail, password=password)
                                         

        login(request, user) #connexion au site
        return redirect('home') # admin.site.register(Shopper)rediriger vers la page daccueil


    return render(request, 'accounts/signup.html')

def login_user(request):
    if request.method == "POST": 

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')



    return render(request,'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')


# def add_to_cart(request, slug):
#     user = request.user.add_to_cart
#     product = get_object_or_404(Product, slug=slug)
#     cart, _ = Cart.objects.get_or_create(user=user)
#     order, created = Order.objects.get_or_create(user=user, product=product)

#     if created:
#         cart.orders.add(order)
#         cart.save()
#     else:
#         order.quantity += 1
#         order.save()

#     return redirect(reverse("product"))