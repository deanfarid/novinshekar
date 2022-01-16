from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class BlogContent(models.Model):
    title = models.OneToOneField('RelatedBlog' , on_delete=models.CASCADE , related_name='title')
    content = RichTextField(verbose_name='محتوا' , max_length=5000)

    def __str__(self):
        return self.title.name


class RelatedBlog(models.Model):
    name = models.CharField(verbose_name='نام بلاگ' , max_length=100)
    
    def __str__(self):
        return self.name