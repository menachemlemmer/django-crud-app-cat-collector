from re import T
from django.contrib import admin
from .models import Cat, Feeding, Toy

admin.site.register(Cat)
admin.site.register(Feeding)
admin.site.register(Toy)

# Register your models here.
