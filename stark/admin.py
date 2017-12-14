from django.contrib import admin
from app01 import models
# Register your models here.
class AuthorConfig(admin.ModelAdmin):
    list_display = ["id","username"]

admin.site.register(models.Author)