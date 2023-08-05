from django.contrib import admin

from .models import Product, Comment


class CommentsInline(admin.TabularInline):  # admin.StackedInline
    model = Comment
    fields = ['author', 'body', 'stars', 'active', ]
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active', 'datetime_modified', ]

    inlines = [CommentsInline, ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'stars', 'active', 'datetime_modified', ]
