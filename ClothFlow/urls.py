
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.defaults import page_not_found
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),

]
