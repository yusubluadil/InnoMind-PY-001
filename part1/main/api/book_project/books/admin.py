from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'publishing_house_name', 'author_name', 'name', 'price', 'created_at')
    search_fields = ('name', 'publishing_house_name', 'author_name')
    list_filter = ('is_available',)
