from django.contrib import admin

from .models import Post, Category


class PostsAdmin(admin.ModelAdmin):
    list_filter = ('active','created_by','date_created','last_updated')
    list_display = ('title','slug','active','created_by','date_created','last_updated')
    fields = ('title','slug','body','active','categories')
    prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

class CategoryAdmin(PostsAdmin):
    fields = ('title','slug','active')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostsAdmin)