from django.urls import path
from account.views import signup, logout_user, login_user
from application.views import index, Category, subcat, content, ADD
from . import views

urlpatterns = [
    path('', index, name='home'),

    path('<id>/subcat/', subcat, name='subcat'),
    path('subcat/<subid>/content/', content, name='content'),

    path('', views.files_form,name='files_insert'),
    path('', views.files_insert,name='files_insert'),
    path('<int:id>/', views.files_form,name='files_update'),
    path('delete/<int:id>/',views.files_delete,name='files_delete'),
    path('list/',views.files_list,name='files_list'),

    path('add', ADD , name='ADD'),
    path('add', index , name='index'),

    path('signup/', signup, name="signup"),
    path('logout/', logout_user, name="logout"),
    path('login/',login_user, name="login"),
]
