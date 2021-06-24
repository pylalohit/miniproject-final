from .models import product, userdetails, wishlist
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth

def cover(request):
    return render(request,'cover.html') 

def buyerlogin(request):
    return render(request,'buyerlogin.html')

#def buyersignup(request):
    #return render(request,'buyersignup.html')

def sellerlogin(request):
    return render(request,'sellerlogin.html')

#def sellersignup(request):
    #return render(request,'sellersignup.html')

def sellerprofile(request):
    return render(request,'sellerprofile.html')

def addproduct(request):
    return render(request,'addproduct.html')

def buyersignupvalidate(request):
    if request.method == 'POST' :
        fn = request.POST['bsfirstname']
        ln = request.POST['bslastname']
        un = request.POST['bsusername']
        phn = request.POST['bsphonenumber']
        em = request.POST['bsemail']
        pwd1 = request.POST['bspassword']
        pwd2 = request.POST['bspassword2']

        if fn == "" or ln == "" or em == "" or pwd1 == "" or pwd2 == "" or phn == "":
            messages.info(request,'Fill all the required feilds')   
            return redirect('buyerlogin') 
            
        elif len(pwd1) < 8:
            messages.info(request,'Password must be atleast 8 characters long')
            return redirect('buyerlogin')
        else:
            if pwd1 == pwd2:
                if User.objects.filter(username=un).exists():
                    messages.info(request,'Username Taken')
                    return redirect('buyerlogin')
                elif User.objects.filter(email=em).exists():
                    messages.info(request,'Email Taken')
                    return redirect('buyerlogin')
                else :
                    user = User.objects.create_user(username = un,password = pwd1 ,first_name = fn,last_name = ln,email = em,is_staff = False)
                    user.save()
                    id = User.objects.get(username=un).pk
                    user_detail = userdetails(user_id = id,username = un, email = em,shopname = "none",passkey = "00" , phonenumber = phn , is_buyer = True , is_seller = False)
                    user_detail.save()
                    wlist = wishlist(user_id = id,list = 'None')
                    wlist.save()
                    messages.info(request,'User created')
                    return redirect('buyerlogin')
            else :
                messages.info(request,'passwords mismatch')
                st = "buyerlogin"
                return redirect(st)

def buyerloginvalidate1(request):
    if request.user.is_authenticated :
        det = userdetails.objects.all()
        return render(request,'loggedin.html',{'det':det})
        
def buyerloginvalidate(request):

    if request.method == 'POST':
        un = request.POST['blusername']
        em = request.POST['blemail']
        pwd = request.POST['blpassword']
        obj = userdetails.objects.get(username=un)
        if (obj is not None and obj.username == un and obj.email == em and obj.is_seller == False and obj.is_buyer == True and obj.passkey == '00'):
            user = auth.authenticate(username=un,email=em,password=pwd)
            if user is not None:
                auth.login(request, user)
                
                return redirect(buyerloginvalidate1)
            else:
                messages.info(request,'invalid credentials')
                return redirect('buyerlogin')
        else :
            return redirect('buyerlogin')
    else :

        return redirect('buyerlogin')
    

def sellersignupvalidate(request):
    if request.method == 'POST' :
        fn = request.POST['ssfirstname']
        ln = request.POST['sslastname']
        un = request.POST['ssusername']
        phn = request.POST['ssphonenumber']
        em = request.POST['ssemail']
        pwd1 = request.POST['sspassword']
        pwd2 = request.POST['sspassword2']
        shopname = request.POST['ssshopname']

        if fn == "" or ln == "" or em == "" or pwd1 == "" or pwd2 == "" or phn == "" or shopname == "":
            messages.info(request,'Fill all the required feilds')   
            return redirect('sellerlogin') 
            
        elif len(pwd1) < 8:
            messages.info(request,'Password must be atleast 8 characters long')
            return redirect('sellerlogin')
        else:
            if pwd1 == pwd2:
                if User.objects.filter(username=un).exists():
                    messages.info(request,'Username Taken')
                    return redirect('sellerlogin')
                elif User.objects.filter(email=em).exists():
                    messages.info(request,'Email Taken')
                    return redirect('sellerlogin')
                else :
                    user = User.objects.create_user(username = un,password = pwd1 ,first_name = fn,last_name = ln,email = em,is_staff = True)
                    user.save()
                    id = User.objects.get(username = un ).pk
                    user_detail = userdetails( user_id = id , username = un, email = em,shopname = shopname,passkey = "09" , phonenumber = phn , is_buyer = False , is_seller = True)
                    user_detail.save()
                    messages.info(request,'User created')
                    return redirect('sellerlogin')
            else :
                messages.info(request,'passwords mismatch')
                st = "sellerlogin"
                return redirect(st)

def sellerloginvalidate1(request):
    if request.user.is_authenticated :
        current_user = request.user
        uname = current_user.username
        id = current_user.id
        obj = userdetails.objects.get(username=uname)
        shnp = obj.shopname
        phnb = obj.phonenumber
        products = product.objects.all()
        return render(request,'sellerprofile.html',{'shopname':shnp,'phonenumber':phnb,'products':products,'id':id,})


def sellerloginvalidate(request):
    if request.method == 'POST':
        un = request.POST['slusername']
        em = request.POST['slemail']
        pwd = request.POST['slpassword']
        pk = request.POST['passkey']
        obj = userdetails.objects.get(username=un)
        if (obj is not None and obj.username == un and obj.email == em and obj.is_seller == True and obj.is_buyer == False and obj.passkey == '09'):
            user = auth.authenticate(username=un,email=em,password=pwd)
            if user is not None:
                auth.login(request, user)
                return redirect(sellerloginvalidate1)
            else:
                messages.info(request,'invalid credentials')
                return redirect('sellerlogin')
        else :
            return redirect('sellerlogin')
    else :

        return redirect('sellerlogin')

def viewusers(request):
    det = userdetails.objects.all()
    return render(request,'viewusers.html',{'det':det})

    
    
def addproductvalidate(request):
    if request.method == 'POST' :
        pid = request.POST['productid']
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
                return render(request,'sellerprofile.html')
            else:
                return redirect('sellerprofile')
    else :
        return redirect('sellerprofile')

def wish_list(request):
    if request.method == "POST" :
        wl = request.POST['wlist']
        current_user = request.user
        id = current_user.id
        obj = wishlist.objects.get(user_id = id)
        obj.list = wl
        obj.save()
        return redirect(buyerloginvalidate1)

def selectseller(request):
    id = request.POST['sid']
    id = int(id)
    us = userdetails.objects.get(user_id = id)
    shopname = us.shopname
    prd = product.objects.all()
    return render(request,'viewseller.html',{'prod':prd,'idr':id,'shopname':shopname})
    

def buyerlogout(request):
    auth.logout(request)
    return redirect('/')

def sellerlogout(request):
    auth.logout(request)
    return redirect('/')