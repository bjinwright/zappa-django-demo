from django.contrib import admin

from .models import Page


class PageAdmin(admin.ModelAdmin):
    list_filter = ('active','created_by','date_created','last_updated')
    list_display = ('title','slug','active','created_by','date_created','last_updated')
    fields = ('title','slug','body','active')
    prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


admin.site.register(Page,PageAdmin)