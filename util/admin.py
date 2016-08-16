from django.contrib import admin


class UtilAdmin(admin.ModelAdmin):
    list_filter = ('created_by','date_added','last_updated')
