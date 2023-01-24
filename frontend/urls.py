from django.urls import path
from frontend import views
urlpatterns=[
    path('',views.fnindex,name="fnindex"),
    path('fncontact/',views.fncontact,name="fncontact"),
    path('fnabout/',views.fnabout,name="fnabout"),
    path('displaycategorypage/<itemcategory>/',views.displaycategorypage,name="displaycategorypage"),
    path('registerlogin/',views.registerlogin, name="registerlogin"),
    path('singleproduct/<int:dataid>/',views.singleproduct,name="singleproduct")
]