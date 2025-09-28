from django.urls import path,include
from .import views

urlpatterns = [
   path('',views.index),
   path('create_accounts',views.create_accounts,name="create_accounts"),
   path('login',views.login,name="login"),
   path('home_page/<int:id>/',views.home_page,name="home_page"),
   path('upload_post/<int:id>/',views.upload_post,name="upload_post"),
   path('view_my_lines/<int:id>/',views.view_my_lines,name="view_my_lines"),
   path('delete_lines/<int:id>/',views.delete_lines,name='delete_lines'),
   path('edit_post/<int:id>/',views.edit_post,name="edit_post"),
]