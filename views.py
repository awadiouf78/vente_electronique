from django.shortcuts import render
from django.http import HttpRespone
# Create your views here.
def produits(requests):
    produits = category.objects.all()
    return produits(requests,'category/liste_produits.html',{'produits':category})
