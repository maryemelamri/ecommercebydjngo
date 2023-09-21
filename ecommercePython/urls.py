from django.contrib import admin
from django.urls import path, include
from MyApp.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("MyApp.urls")),
    path("user/", include("userauths.urls")),
]



