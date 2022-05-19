from django.contrib import admin
from blog.models import Post, Tag, Comment


class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ('text', 'author', 'published_at',)
    readonly_fields = ('author', 'published_at',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('post', 'author')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'published_at',)
    ordering = ('-published_at',)
    raw_id_fields = ('post', 'author',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at',)
    search_fields = ('title',)
    raw_id_fields = ('author', 'likes', 'tags',)
    inlines = [CommentsInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('title',)
