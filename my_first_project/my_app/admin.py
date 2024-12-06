from django.contrib import admin

# Register your models here.
from .models import Book,Author2
admin.site.register(Book)


admin.site.register(Author2)