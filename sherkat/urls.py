
from django.contrib import admin 
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/' , include('customer.urls')),
    path('post/' , include('post.urls')),

]


urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

#showing pics
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
