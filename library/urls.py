from django.contrib import admin
from django.urls import path,include
import books.urls
import frontend.urls
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from library import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/',include(books.urls)),
    path('',include(frontend.urls))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
