from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home ,name="home"),
    path('login/',views.loginPage, name="login"),
     path('logout',views.logoutUser, name="logout"),
    path('register/',views.registerPage, name="register"),
    path('index/',views.donate ,name="index"),
    path('about/',views.about,name="about"),
    path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.successMsg, name="success"),
    path('index1/',views.index,name="test"),
    path('pdf/',views.render_pdf_view,name="pdf"),
    path('index2/',views.sell,name="buy"),
    path('index3/',views.sell1,name="sell"),
]