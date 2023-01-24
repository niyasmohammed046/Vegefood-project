from django.shortcuts import render
from books.models import categorydb,productdb

# Create your views here.
def fnindex(request):
    data=categorydb.objects.all()
    return render(request,"fnindex.html", {'data':data})

def fncontact(request):
    data=categorydb.objects.all()
    return render(request,"fncontact.html",{'data':data})
    
def fnabout(request):
    return render(request,"fnabout.html")

def displaycategorypage(request,itemcategory):
    data=categorydb.objects.all()
    products=productdb.objects.filter(PCategory=itemcategory)

    context={

        'data':data,
        'products':products
    }
    return render(request,"categorydisplay.html",context)


def registerlogin(request):
    return render(request,"register.html")

def singleproduct(request,dataid):
    data=productdb.objects.get(id=dataid)
    da=categorydb.objects.all()
    return render(request,"veg.html" ,{'dat':data,'da':da})
