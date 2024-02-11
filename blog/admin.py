from django.contrib import admin

from blog.models import Post, User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'post_count', 'password']
    search_fields = ['first_name', 'last_name', 'username']
    # list_filter = ['post_count']
    list_display_links = ['username', 'password']
    def get_post_count(self):
        return self.post_count

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'is_active', 'published']
    search_fields = ['author', 'is_active']
    date_hierarchy = 'published'