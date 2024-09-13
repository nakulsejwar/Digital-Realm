from django.contrib import admin
from .models import Post, Category, Comment

admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)


    class Media:
        js = ('https://cdn.jsdelivr.net/npm/@tinymce/tinymce-webcomponent@2/dist/tinymce-webcomponent.min.js', 'js/main.js',)

admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Comment) 