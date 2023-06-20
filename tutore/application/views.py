from django.shortcuts import render, redirect
from .models import Category, SubCategory, Files
from .forms import FilesForm


def index(request):
    files_object = Files.objects.all()
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    item = request.GET.get('item-name')
    if item !='' and item is not None:
        files_object = Files.objects.filter(title__icontains=item,)
    context =  { 'files_object':files_object , 'category':category, 'subcategory':subcategory }
    
    return render(request, 'tutore/index.html',context )



def subcat(request,id):
    category = Category.objects.all()
    c = Category.objects.get(id=id)
    subcategory = SubCategory.objects.filter(category=c) 
    
    context =  { 'category':category, 'subcategory':subcategory }
    
    return render(request, 'tutore/sub.html',context )


def content(request,  subid):
    subcategory = Files.objects.all()
    category = Category.objects.all()
    s = SubCategory.objects.get(id=subid)
    filesd = Files.objects.filter(sub_category= s)
    subcategory = SubCategory.objects.all()
    
    context =  { 'subcategory':subcategory, 'category':category, 'filesd':filesd }
    
    return render(request, 'tutore/content.html',  context )

#--------------------------- CRUD on  files -----------------------


def files_list(request):

    context = {'files_list': Files.objects.all()}
    return render(request, "tutore/files_list.html", context)


def files_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = FilesForm()
        else:
            files = Files.objects.get(pk=id)
            form = FilesForm(files)
        return render(request, "tutore/files_form.html", {'form': form})
    else:
        if id == 0:
            form = FilesForm(request.POST)
        else:
            files = Files.objects.get(pk=id)
            form = FilesForm(request.POST, files)
        if form.is_valid():
            form.save()
        return redirect('/list')
    
def files_insert(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = FilesForm()
        else:
            files = Files.objects.get(pk=id)
            form = FilesForm(files)
        return render(request, "tutore/files_form.html", {'form': form})


def files_delete(request,id):
    files = Files.objects.get(pk=id)
    files.delete()
    return redirect('/list')





# def cat_list(request):
#     context = {'files_list': Files.objects.all()}
#     return render(request, "tutore/list.html", context)


# def cat_form(request, id=0):
#     if request.method == "GET":
#         if id == 0:
#             form = FilesForm()
#         else:
#             files = Files.objects.get(pk=id)
#             form = FilesForm(instance=files)
#         return render(request, "tutore/form.html", {'form': form})
#     else:
#         if id == 0:
#             form = FilesForm(request.POST)
#         else:
#             files = Files.objects.get(pk=id)
#             form = FilesForm(request.POST,instance= files)
#         if form.is_valid():
#             form.save()
#         return redirect('/list')


# def cat_delete(request,id):
#     files = Files.objects.get(pk=id)
#     files.delete()
#     return redirect ('/list')

def dis (request):
    return redirect('tutore/insert.html')


def ADD(request):
  if request.method == "POST":
        Titre = request.POST.get('Titre')
        Auteur = request.POST.get('Auteur')
        nom = request.POST.get('nom_du_fichier')
        contributeur = request.POST.get('dernier_contributeur')
        datecreation = request.POST.get('date_de_creation')
        sujet = request.POST.get('sujet')
        description = request.POST.get('description')
        document = request.FILES['document']
 
        fich = Files(
            Titre = Titre,
            Auteur = Auteur,
            nom_du_fichier = nom,
            dernier_contributeur = contributeur,
            date_de_creation = datecreation,
            sujet = sujet,
            description = description,
            document = document
        )
        fich.save()    
        return redirect('mesfichiers')
  
    
#   return render(request, 'crud/ajout_fichier.html', )