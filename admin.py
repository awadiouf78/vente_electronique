from django.contrib import admin

# Register your models here.
from .models import client,produit,
admin.site.Register(client)
admin.site.Register(produit)