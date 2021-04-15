from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'update', 'get_photo',)
    list_filter = ('date',)
    search_fields = ('title', 'author',)
    list_display_links = ('title',)

    def get_photo(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width="50">')
        return 'Нет изображения'

    get_photo.short_description = 'Изображение'


admin.site.register(News, NewsAdmin)
