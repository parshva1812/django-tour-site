from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
import sqlite3
import requests
from myapp.models import Customer,Gallery,Tour,Booking
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from myapp.forms import Gallery_form,Tour_form,Booking_form,Tourist_form



def index(request):
    context ={}
    all=Tour.objects.all()
    context['tours']=all

    return render(request,'myapp\index.html',context)
def aboutus(request):
    
    return render(request,'myapp\\laboutus.html')
def register(request):
    if request.method =="POST":
        fname=request.POST["fname"]
        mname=request.POST["mname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        phone=request.POST["contact"]
        gender=request.POST["gender"]
        address=request.POST["address"]
        password=request.POST["password"]
        age=request.POST["age"]

        usr = User.objects.create_superuser(phone,email,password)
        usr.first_name=fname
        usr.last_name=lname
        usr.is_staff=False
        usr.is_superuser=False
        usr.save()
        reg=Customer(user=usr,Mname=mname,Gender=gender,Address_no=address,Age=age,Contact_no=phone)
        reg.save()
        return render(request,'myapp\\register.html',{"status":"{} registered succesfuly".format(fname)})
    
        # data=Customer(Fname=fname,Lname=lname,Mname=mname,Email=email,Phone=phone,Genders=gender,Address=address,Age=age,Password=password)
        # data.save()
        # print(data)

    return render(request,'myapp\\register.html')
def blogs(request):
    return render(request,'myapp\\blogs.html')
def gallery(request):
    images=Gallery.objects.all()

    return render(request,'myapp\\gallery.html',{'images':images})
def contactus(request):
    return render(request,'myapp\\contactus.html')
def packages(request):
    context ={}
    all=Tour.objects.all()
    context['tours']=all
    return render(request,'myapp\packages.html',context)

def booking(request):
    context ={}
    context['count']=[]
    ch=Customer.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        data=Customer.objects.get(user__id=request.user.id)
        context['data'] =data
    form=Booking_form()
    if request.method =="POST":
    
        form =Booking_form(request.POST)
        
        if form.is_valid():
            
            data = form.save(commit=False)
            login_user=User.objects.get(username=request.user.username)
            data.customer=login_user
            data.Amount=int(data.Persons) * int(data.tour.fare)
            data.save()

            context['status']="Booking done successfully"
        
    context['form']=form
    print(context['count'])
    return render(request,'myapp\\booking.html',context)
@login_required
def mybooking(request):
    context ={}
    all=Booking.objects.filter(customer__id = request.user.id)
    context['booking'] =all
    return render(request,'myapp\\mybooking.html',context)
@login_required
def allbookings(request):
    context ={}
    all=Booking.objects.all()
    context['booking'] =all
    return render(request,'myapp\\allbookings.html',context)


def check_user(request):
    if request.method =="GET":
        contact=request.GET["contact"]
        check=User.objects.filter(username=contact)
        if len(check) == 1:
            return HttpResponse("Exist")
        else:
            return HttpResponse("notExist")
def check_user_email(request):
    if request.method =="GET":
        email=request.GET["email"]
        check=User.objects.filter(email=email)
        print(check)
        if len(check) == 1:
            return HttpResponse("Exist")
        else:
            return HttpResponse("notExist")
def user_login(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        
        user=authenticate(username=username, password=password)
        if user:
            login(request,user)
            
            if user.is_superuser:
                return HttpResponseRedirect("/admin")
            elif user.is_staff:
                return HttpResponseRedirect("/")

            elif user.is_active:
                return HttpResponseRedirect("/")

        else:
            return render(request,"myapp\index.html",{"status":"Invalid Id or Password"})
     
@login_required
def cust_dash(request):
    return render(request,'myapp\cust_dash.html')
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")
@login_required
def add_img(request):
    context={}
    form=Gallery_form()
    if request.method =="POST":
        form=Gallery_form(request.POST,request.FILES)
        if form.is_valid():
            data=form.save()
            data.save()
            context['status']="Image added successfully"
    context['form']=form
    return render(request,'myapp\\add_img.html',context)
@login_required
def add_tour(request):
    context ={}
    form=Tour_form()
    if request.method =="POST":
        form =Tour_form(request.POST, request.FILES)
        
        if form.is_valid():
            
            data = form.save()
            data.save()
            context['status']="done"
    context['form']=form
    return render(request,'myapp\\add_tour.html',context)
@login_required
def my_tour(request):
    context ={}
    all=Tour.objects.all()
    context['tours']=all
    return render(request,'myapp\my_tour.html',context)
@login_required
def update_tour(request):
    context ={}
    all=Tour.objects.all()
    context['tours']=all
    tid=request.GET['tid']
    tour=Tour.objects.get(id=tid)
    context['tour']=tour
    if request.method =="POST":
        tn=request.POST['tour_name']
        pf=request.POST['place_from']
        pt=request.POST['place_to']
        ptb=request.POST['places_to_be']
        days=request.POST['days']
        nights=request.POST['nights']
        fare=request.POST['fare']
        description=request.POST['tour_descriptions']

        tour.tour_name=tn
        tour.place_from=pf
        tour.place_to=pt
        tour.places_to_be=ptb
        tour.days=days
        tour.nights=nights
        tour.fare=fare
        tour.tour_descriptions=description
        if "tour_image" in request.FILES:
            img=request.FILES["tour_image"]
            tour.tour_image=img
        tour.save()
        context['status']="Tour updated successfully"


    return render(request,'myapp\\update_tour.html',context)
@login_required
def delete_tour(request):
    context ={}
    if "tid" in request.GET:
        tid=request.GET["tid"]
        tr=get_object_or_404(Tour,id=tid)
        context['tour'] =tr
        if "action" in request.GET:
            tr.delete()
            context['status']=str(tr.tour_name) + "Deleted successfully"
    return render(request,'myapp\\delete_tour.html',context)
@login_required
def delete_booking(request):
    context ={}
    if "bid" in request.GET:
        bid=request.GET["bid"]
        bk=get_object_or_404(Booking,id=bid)
        context['booking'] =bk
        if "action" in request.GET:
            bk.delete()
            context['status']=str(bk.tour.tour_name) + "Deleted successfully"
    return render(request,'myapp\\delete_booking.html',context)







