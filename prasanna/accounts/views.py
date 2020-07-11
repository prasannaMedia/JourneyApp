from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Bus,Book
from decimal import Decimal
from django.core.files import File


# Create your views here.
def login(request):
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                    auth.login(request,user)
                    return redirect("/")
            else:
                    return redirect('login')   

        else:
            return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")

def findbus(request):
    context = {}
    if request.method == 'POST':
        source_r = request.POST.get('source')
        dest_r = request.POST.get('destination')
        date_r = request.POST.get('date')
        bus_list = Bus.objects.filter(source=source_r, dest=dest_r, date=date_r)
        if bus_list:
            return render(request, 'list.html', locals())
        else:
            context["error"] = "Sorry no buses availiable"
            return render(request, 'findbus.html', context)
    else:
        return render(request, 'findbus.html')

def bookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        seats_r = int(request.POST.get('no_seats'))
        bus = Bus.objects.get(id=id_r)
        print(bus)
        if bus:
            # print('inside 1st if')
            # print(bus.rem)
            if  int(bus.rem) >= seats_r:
                # print('inside 2nd if')
                name_r = bus.bus_name
                cost = int(seats_r) * bus.price
                source_r = bus.source
                dest_r = bus.dest
                nos_r =bus.nos
                price_r = bus.price
                date_r = bus.date
                time_r = bus.time
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r =int( bus.rem) - seats_r
                print(rem_r)
                Bus.objects.filter(id=id_r).update(rem=rem_r)
                book = Book.objects.create(name=username_r, email=email_r, userid=userid_r, bus_name=name_r,
                                           source=source_r, busid=id_r,
                                           dest=dest_r, price=price_r, nos=seats_r, date=date_r, time=time_r)
                print('------------Book id-----------', book.id)


                return render(request, 'bookings.html', locals())
            else:
                context["error"] = "Sorry select fewer number of seats"
                return render(request, 'findbus.html', context)

        else:
                return render(request, 'findbus.html')

def  register(request):

    if request.method=='POST':
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password1==password2:

            if User.objects.filter(username=username).exists():
                 messages.info(request,'username taken')
                 return redirect('register')

            elif User.objects.filter(email=email).exists():
                      messages.info(request,'email taken')
                      return redirect('register')
            else:
                    user = User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
                    user.save();
                    print("user created")
                    return redirect('/')
        else:
              messages.info(request,'password is not matching')
              return redirect('register')
    else:
        return render(request, 'register.html')