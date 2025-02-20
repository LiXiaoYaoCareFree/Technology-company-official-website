from django.contrib import admin
from .models import Slide

class SlideAdmin(admin.ModelAdmin):
    list_display = ['id','image','title','content']


admin.site.register(Slide,SlideAdmin)
