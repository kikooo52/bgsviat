from django.contrib import admin

from .models import MyBlog

class MyBlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'created', 'tag_list']
    list_filter = ['tags']

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

admin.site.register(MyBlog, MyBlogAdmin)