from django.contrib import admin
from .models import User, Comment
from django.contrib.contenttypes.admin import GenericTabularInline

admin.site.site_header = 'ProfilerApp Admin'
admin.site.site_title = 'ProfilerApp Admin Area'
admin.site.index_title = 'Welcome to Profiler Admin Area'

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class UserAdmin(admin.ModelAdmin):
    list_display = ['user_name','user_lname','user_email','user_position','image_tag']
    search_fields = ['user_name','user_lname','user_email','user_position']
    inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'user_id', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(active=True)

admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)