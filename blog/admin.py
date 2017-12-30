from django.contrib import admin
from .models import Post, Topic
from markdownx.admin import MarkdownxModelAdmin
from imagekit.admin import AdminThumbnail



#class ImageInline(admin.TabularInline):
#    model = Image

class PostInline(admin.TabularInline):
    model = Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Image', {'fields': ['image']}),
        ('Post Details',               {'fields': ['topic', 'post_title','summary', 'keywords','text']}),
        ('Date information', {'fields': ['created_at', 'posted_at', 'last_update'], 'classes': ['collapse']}),
    ]
    #admin_thumbnail = AdminThumbnail(image_field='thumbnail')
    readonly_fields = ('created_at', 'last_update', 'views')
#    inlines = [ImageInline]



class TopicAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Subject', {'fields': ['subject']}),
        ]
    inlines = [PostInline]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
#admin.site.register(Post, MarkdownxModelAdmin)
