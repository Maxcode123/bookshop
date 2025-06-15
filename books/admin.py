from django.contrib import admin

from books.models import BookAuthor, BookGenre, Book


class BookAuthorInline(admin.TabularInline):
    model = BookAuthor
    extra = 1


class BookGenreInline(admin.TabularInline):
    model = BookGenre
    extra = 1


class BookAdmin(admin.ModelAdmin):
    inlines = [BookGenreInline, BookAuthorInline]


admin.site.register(Book, BookAdmin)
