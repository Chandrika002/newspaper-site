from django.contrib import admin
from articles.models import Article
from articles.models import Article, Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "publish_date")

admin.site.register(Article, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "article")


admin.site.register(Comment, CommentAdmin)