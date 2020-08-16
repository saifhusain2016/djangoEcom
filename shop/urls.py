from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shopHome'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contractus'),
    path('productview/', views.productview, name='productView'),
    path('checkout/', views.checkout, name='checkout'),
    path('search/', views.search, name='search'),
    path('tracker/', views.tracker, name='tracker')
]
