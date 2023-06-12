from django.shortcuts import render, redirect
from .models import Category, SubCategory, Files
from .forms import FilesForm

# Create your views here.

def index(request):
    files_object = Files.objects.all()
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    item = request.GET.get('item-name')
    if item !='' and item is not None:
        files_object = Files.objects.filter(title__icontains=item)
    
    context =  {
        'files_object':files_object ,
         'category':category,
         'subcategory':subcategory
        }
    
    return render(request, 'tutore/index.html',context  )

# def search(request):
#     query = request.GET.get('item-name')
#     results = Files.objects.filter(title__icontains=query) | Files.objects.filter(author__icontains=query)
#     return render(request, 'tutore/index.html', {'results': results})



def files_list(request):
    context = {'files_list': Files.objects.all()}
    return render(request, "tutore/list.html", context)


def files_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = FilesForm()
        else:
            files = Files.objects.get(pk=id)
            form = FilesForm(instance=files)
        return render(request, "tutore/form.html", {'form': form})
    else:
        if id == 0:
            form = FilesForm(request.POST)
        else:
            files = Files.objects.get(pk=id)
            form = FilesForm(request.POST,instance= files)
        if form.is_valid():
            form.save()
        return redirect('/list')


def files_delete(request,id):
    employee = Files.objects.get(pk=id)
    employee.delete()
    return redirect ('/list')