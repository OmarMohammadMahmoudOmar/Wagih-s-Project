from django.contrib import admin
from .models import Article, Author, Category, Tag, Subscribe, Comment, ArticleView

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Subscribe)
