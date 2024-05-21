from django.contrib import admin

from books.models import Book, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'date_time', 'recommend', 'is_active')


admin.site.register(Book)
admin.site.register(Comment, CommentAdmin)