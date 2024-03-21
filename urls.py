from django.urls import path
urlpatterns=[
    path('',views.home,name='home'),
    path(' ',views.produit,name='produits')
]