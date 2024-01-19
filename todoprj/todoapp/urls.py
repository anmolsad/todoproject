from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='homepage'),
    path('register/',views.register,name='register'),
    path('login/',views.loginpage,name='login'),
    path('logout',views.logoutview,name='logout'),
    path('delete/<str:name>',views.deleteTask,name="delete"),
    path('update/<str:name>',views.updateTask,name="update")

]