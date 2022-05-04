from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category, Comments


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = (
        'id', 'title', 'views', 'category',  # отображаемые поля в админке
        'created_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')  # кликабельные поля
    search_fields = ('title', 'content')  # поля по которым можно осуществлять поиск
    list_editable = ('is_published',)  # редактирование в корне новостей
    list_filter = ('is_published', 'category')
    fields = (
        'title', 'category', 'content', 'preview_content',
        'photo', 'get_photo', 'created_at',
        'updated_at', 'views', 'is_published',
    )
    readonly_fields = ('get_photo', 'created_at', 'updated_at', 'views')
    save_on_top = True

    # добавляет миниатюру фотографии в админке
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="55px">')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')  # отображаемые поля в админке
    list_display_links = ('id', 'title')  # кликабельные поля
    search_fields = ('title',)  # поля по которым можно осуществлять поиск


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', 'news', 'content', 'created_at')
    readonly_fields = ('news', 'author')
    list_display_links = ('author', 'content', 'news')
    search_fields = ('author', 'content')
    list_filter = ('author', 'created_at')


# образование связи между админкой и моделью
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Новостной сайт'
