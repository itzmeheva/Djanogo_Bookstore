from django.contrib import admin
from .models import Category, Author, Book, BookComment

class BookCommentStackedInline(admin.StackedInline):
    model = BookComment

class BookTabularInline(admin.TabularInline):
    model = BookComment
    extra = 0

class BookAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category', 'price', 'level', 'published']
    list_filter = ['published']
    search_fields = ['code', 'name']
    prepopulated_fields = {'slug': ['name']}
    fieldsets = (
        (None, {'fields': ['code', 'slug', 'name', 'description', 'level', 'price', 'published']}),
        ('Category', {'fields': ['category', 'author', ], 'classes': ['collapse']}),
    )
    inlines = [ BookTabularInline]

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
