from django.contrib import admin
from .models import Category, Article

# admin.site.register([Article, Category])

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_filter = ('created_at', 'author')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title', 'author', 'content')
    list_display_links = ('id', 'title')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('name', )
