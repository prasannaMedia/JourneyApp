from django.urls import path

from . import views

urlpatterns = [ 
               path("register", views.register, name="register"),
               path("login",views.login, name="login"), 
               path("logout",views.logout,name="logout"),
               path("findbus",views.findbus,name="findbus"),
               path('bookings', views.bookings, name="bookings")
               
 ]
