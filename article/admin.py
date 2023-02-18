from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .forms import ArticleForm
from .models import Article


class ArticleFormAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        return ArticleForm


admin.site.register(Article, ArticleFormAdmin)
