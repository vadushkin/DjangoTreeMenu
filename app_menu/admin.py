from django.contrib import admin

from .models import TreeMenu, TreeMenuCategory


class TreeMenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name', 'verbose_name')


class TreeMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'path', 'parent')
    fields = ('name', 'category', 'path', 'parent')


admin.site.register(TreeMenu, TreeMenuAdmin)
admin.site.register(TreeMenuCategory, TreeMenuCategoryAdmin)
