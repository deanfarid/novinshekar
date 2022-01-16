from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.BlogContent)
admin.site.register(models.RelatedBlog)

