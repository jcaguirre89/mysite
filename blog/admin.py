from django.contrib import admin
from .models import Post, Topic


class PostInline(admin.TabularInline):
    model = Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Image', {'fields': ['image']}),
        ('Post Details',               {'fields': ['topic', 'pub_date', 'post_title','summary', 'tags','text']}),
        ('Date information', {'fields': ['created_at', 'last_update'], 'classes': ['collapse']}),
    ]
    readonly_fields = ('created_at', 'last_update', 'views')

class TopicAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Subject', {'fields': ['subject']}),
        ]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
