from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name="index"),
    path('aboutus/',views.aboutus, name="laboutus"),
    path('register/',views.register, name="register"),
    path('blogs/',views.blogs, name="blogs"),
    path('contactus/',views.contactus, name="contactus"),
    path('gallery/',views.gallery, name="gallery"),
    path('packages/',views.packages, name="packages"),
    path('check_user/',views.check_user, name="check_user"),
    path('check_user_email/',views.check_user_email, name="check_user_email"),
    path('user_login/',views.user_login, name="user_login"),
    path('cust_dash/',views.cust_dash, name="cust_dash"),
    path('user_logout/',views.user_logout, name="user_logout"),
    path('add_img/',views.add_img, name="add_img"),
    path('add_tour/',views.add_tour, name="add_tour"),
    path('my_tour/',views.my_tour, name="my_tour"),
    path('update_tour/',views.update_tour, name="update_tour"),
    path('delete_tour/',views.delete_tour, name="delete_tour"),
    path('booking/',views.booking, name="booking"),
    path('mybooking/',views.mybooking, name="mybooking"),
    path('allbookings/',views.allbookings, name="allbookings"),
    path('delete_booking/',views.delete_booking, name="delete_booking")



   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)