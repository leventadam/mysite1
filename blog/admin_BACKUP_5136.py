from django.contrib import admin
<<<<<<< HEAD
from .models import Post
=======
from .models import Post, Comment
>>>>>>> 2066ac1db9492623372d6d5caaef2157587087e6
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish','status')
	list_filter = ('status', 'created', 'publish', 'author')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ['status', 'publish']
<<<<<<< HEAD
=======

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'post', 'created', 'active')
	list_filter = ('active', 'created', 'updated')
	search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)
>>>>>>> 2066ac1db9492623372d6d5caaef2157587087e6
admin.site.register(Post, PostAdmin)