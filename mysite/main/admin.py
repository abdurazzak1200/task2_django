from django.contrib import admin
from .models import Books,Genre,Comment
# Register your models here.
admin.site.register(Books)
admin.site.register(Genre)
admin.site.register(Comment)