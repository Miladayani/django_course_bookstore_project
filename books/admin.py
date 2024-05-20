from django.contrib import admin

from books.models import Book, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'date_time')


admin.site.register(Book)
admin.site.register(Comment, CommentAdmin)