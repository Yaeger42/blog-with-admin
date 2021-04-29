from django.contrib import admin
from posts.models import Post 

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'category', 'created')
    search_fields = ('title', 'category')
    list_filter = ('created', 'lastUpdated')
