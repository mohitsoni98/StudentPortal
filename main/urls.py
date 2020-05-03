from main import views
from django.urls import path


urlpatterns=[
    path('',views.dashboard,name='dashboard'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('ajax/exists',views.exists,name='exists')

]