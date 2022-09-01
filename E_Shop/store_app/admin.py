from django.contrib import admin

# Register your models here.
from .models import *

class ImageTublerinLine(admin.TabularInline):
    model = Images

class TagTubelerinLine(admin.TabularInline):
    model = Tag

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageTublerinLine,TagTubelerinLine]



admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Product,ProductAdmin)
