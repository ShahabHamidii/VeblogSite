from django.contrib import admin
from . import models



@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author')
    list_filter = ('status', 'author')
    list_editable = ('status',)
    search_fields = ('title',)
admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Message)
admin.site.register(models.Like)

