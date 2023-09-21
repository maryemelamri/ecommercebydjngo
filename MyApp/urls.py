from django.urls import path

from MyApp import views
from MyApp.views import index
from MyApp.views import product_list_view
from MyApp.views import product_detail_view

app_name ="MyApp"

urlpatterns = [
    path("", index, name="index"),
    path("products/", product_list_view, name="product-list"),
    path("products/<pid>", product_detail_view, name="product-detail")

]