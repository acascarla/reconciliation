from django.contrib import admin


class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'iswc')
    search_fields = ['title', 'iswc']
    ordering = ['title', 'iswc']
