from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User , auth
from .models import product, userdetails
# Create your views here.

def home(request):
    return render(request,'home.html')



def authenticate(request):
    return render(request,'sellerlogin.html')

def sellerprofile(request):
    return render(request,'mystore.html')

def addproduct(request):
    return render(request,'addproduct.html')

def viewsellers(request):
    det = userdetails.objects.all()
    return render(request,'viewsellers.html',{'det':det})

def mystore(request):
    if request.user.is_authenticated :
        current_user = request.user
        uname = current_user.username
        id = current_user.id
        obj = userdetails.objects.get(username=uname)
        shnp = obj.shopname
        phnb = obj.phonenumber
        products = product.objects.all()
        return render(request,'mystore.html',{'shopname':shnp,'phonenumber':phnb,'products':products,'id':id,})

def addproductvalidate(request):
    if request.method == 'POST' :
        pid = request.POST['productid']
        if product.objects.filter(pid=pid).exists():
                    messages.info(request,'Pid already exists.')
                    return redirect('addproduct')
        pname = request.POST['productname']
        pdescription = request.POST['productdescription']
        pavailable = request.POST['productavailability']
        pquantity = request.POST['productquantity']
        pprice = request.POST['productprice']

        if pid == "" or pname == "" or pdescription == "" or  pquantity == "" or pprice == "" :
            messages.info(request,'fill all the fields')
            return redirect('sellerprofile')
        else:
            current_user = request.user
            id = current_user.id
            prod = product(user_id=id,pid = pid, pname = pname, pdescription = pdescription , pprice = pprice,pavailability = pavailable, pquantity = pquantity)
            if prod is not None:
                prod.save()
                messages.info(request,'added successfully')
                return redirect('mystore')
            else:
                return redirect('sellerprofile')
    else :
        return redirect('sellerprofile')


def updateproduct(request):
    if request.method == 'POST' :
        pid = request.POST['productid']
        pname = request.POST['productname']
        pdescription = request.POST['productdescription']
        pavailable = request.POST['productavailability']
        pquantity = request.POST['productquantity']
        pprice = request.POST['productprice']
    
    if pid != "" :

        obj = product.objects.get(pid=pid)
        if (obj != None):
            if pname != "":
                obj.pname = pname
                obj.save()
            if pdescription != "":
                obj.pdescription = pdescription
                obj.save()
            if pavailable != "":
                obj.pavailability = pavailable
                obj.save()
            if pquantity != "":
                obj.pquantity = pquantity
                obj.save()
            if pprice != "":
                obj.pprice = pprice
                obj.save()
            
            return redirect('mystore')

        else :
            messages.info(request,'please enter the valid pid')
            return redirect('updateproduct')
    else :
        messages.info(request,'please enter the valid pid')
        return redirect('updateproduct')

def selectseller(request):
    id = request.POST['sid']
    id = int(id)
    us = userdetails.objects.get(user_id = id)
    shopname = us.shopname
    prd = product.objects.all()
    return render(request,'viewsellerstore.html',{'prod':prd,'idr':id,'shopname':shopname})

def signupverifying(request):

        if request.method == 'POST' :
            fn = request.POST['ssfullname']
            add = request.POST['ssaddress']
            un = request.POST['ssusername']
            phn = request.POST['ssphonenumber']
            em = request.POST['ssemail']
            pwd1 = request.POST['sspassword']
            pwd2 = request.POST['sspassword2']
            shopname = request.POST['ssshopname']

            if fn == "" or add == "" or em == "" or pwd1 == "" or pwd2 == "" or phn == "" or shopname == "":
                messages.info(request,'Fill all the required feilds')   
                return redirect('authenticate') 
                
            elif len(pwd1) < 8:
                messages.info(request,'Password must be atleast 8 characters long')
                return redirect('authenticate')
            else:
                if pwd1 == pwd2:
                    if User.objects.filter(username=un).exists():
                        messages.info(request,'Username Taken')
                        return redirect('authenticate')
                    elif User.objects.filter(email=em).exists():
                        messages.info(request,'Email Taken')
                        return redirect('authenticate')
                    else :
                        user = User.objects.create_user(username = un,password = pwd1 ,first_name = fn,email = em)
                        user.save()
                        id = User.objects.get(username = un ).pk
                        user_detail = userdetails( user_id = id , username = un, email = em,shopname = shopname,passkey = "09" , phonenumber = phn , address = add)
                        user_detail.save()
                        messages.info(request,'User created')
                        return redirect('authenticate')
                else :
                    messages.info(request,'passwords mismatch')
                    st = "sellerlogin"
                    return redirect('authenticate') 
        else :   
            return redirect('authenticate')

def loginverifying(request):
    if request.method == 'POST':
        un = request.POST['slusername']
        pwd = request.POST['slpassword']
        pk = request.POST['passkey']
        if ( pwd == '' or pk == '' or  un == "" ):
            messages.info(request,'Fill all the fields required')
            return redirect('authenticate')
        else :
            obj = userdetails.objects.get(username=un)
            if (obj is not None and obj.username == un and obj.passkey == '09'):
                user = auth.authenticate(username=un,password=pwd)
                if user is not None:
                    auth.login(request, user)
                    return redirect('mystore')
                else:
                    messages.info(request,'invalid credentials')
                    return redirect('authenticate')
            else :
                return redirect('authenticate')
    else :

        return redirect('authenticate')



def logout(request):
    auth.logout(request)
    return redirect('/')