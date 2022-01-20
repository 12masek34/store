from django.urls import path, include
from .views import *

urlpatterns = [
    path('reg/', register, name='reg'),
    path('login/', login_form, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', index, name='index'),
    path('<int:pk>/', category, name='category'),
    path('add_product/', add_product, name='add_product'),
    path('product/<int:pk>', product, name='product'),
]
