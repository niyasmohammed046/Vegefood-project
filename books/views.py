from django.shortcuts import render,redirect
from books.models import bookdb,categorydb,productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User



def indexfn(request):
    return render(request,"index.html")

#category 

def categoryip(request):
    return render(request,"categoryinput.html")
def savecategory(request):
    if request.method=='POST':
        cty=request.POST.get('category')
        des=request.POST.get('description')
        img=request.FILES['image']
        obj=categorydb(Category=cty,Description=des,Image=img)
        obj.save()
        return redirect(categoryop)
def categoryop(request):
    data=categorydb.objects.all()
    return render(request,"categoryoutput.html",{'data':data})

def categoryedit(request,dataid):
    data=categorydb.objects.get(id=dataid)
    print (data)
    return render(request,"categoryedit.html",{'data':data})

def categoryupdate(request,dataid):
    if request.method=='POST':
        cty=request.POST.get('category')
        des=request.POST.get('description')
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=dataid).Image
    categorydb.objects.filter(id=dataid).update(Category=cty,Description=des,Image=file)
    return redirect(categoryop)
def categorydel(request,dataid):
    data=categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(categoryop)





def contact(request):
    return render(request,"contact.html")




#products

def productinput(request):
    data=categorydb.objects.all()
    return render(request,"productinput.html",{'data':data})

def saveproducts(request):
    if request.method=="POST":
     pd=request.POST.get('product')
     des=request.POST.get('description')
     pri=request.POST.get('price')
     cat=request.POST.get('category')
     img=request.FILES['image']
     obj=productdb(Product=pd,Description=des,PPrice=pri,PCategory=cat,Image=img)
     obj.save()
     return redirect(productinput)
def productoutput(request):
    data=productdb.objects.all()
    return render(request,"productoutput.html",{'data':data})
def editproduct(request,dataid):
    data=productdb.objects.get(id=dataid)
    da=categorydb.objects.all()
    print(data)
    return render(request,"productedit.html",{'data':data,'da':da})

def updateproduct(request,dataid):
    if request.method=='POST':
        pd=request.POST.get('product')
        cty=request.POST.get('category')
        des=request.POST.get('description')
        pri=request.POST.get('price')
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=dataid).Image
        productdb.objects.filter(id=dataid).update(Product=pd,PCategory=cty,PPrice=pri,Description=des,Image=file)
        return redirect(productoutput)

def productdel(request,dataid):
    data=productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(productoutput)




#login

def loginpage(request):
    return render(request,"loginpage.html")

def loginsave(request):
    if request.method=="POST":
        usrname=request.POST.get('uname')
        psd=request.POST.get('pwd')
        if User.objects.filter(username__contains=usrname).exists():
            user=authenticate(username=usrname,password=psd)
            if user is not None:
               login(request,user)
               request.session['uname']=usrname
               request.session['pwd']=psd
               return redirect(indexfn)
            else:
                return redirect(loginpage)
        else:
          return redirect (loginpage)



           
