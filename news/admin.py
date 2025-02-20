from django.contrib import admin
from news.models import Category, News
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'category')



admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
