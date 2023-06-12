from django.urls import path
from application.views import index, Category
from . import views

urlpatterns = [
    path('', index, name='home'),



    path('update/', views.files_form,name='files_insert'), 
    path('<int:id>/', views.files_form,name='files_update'),
    path('delete/<int:id>/',views.files_delete,name='files_delete'),
    path('list/',views.files_list,name='files_list') 
]
