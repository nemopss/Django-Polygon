
from django.urls import reverse
import hashlib
import uuid
import os
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.utils.text import slugify
from mdeditor.fields import MDTextField


class MarkdownContent(models.Model):
    title = models.CharField(max_length=100)
    markdown_content = MDTextField()

    def __str__(self):
        return f"{self.title}, {self.markdown_content}"


class Image(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    file_name = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to='images/')
    mime_type = models.CharField(max_length=100, null=False)
    md5_hash = models.CharField(max_length=100, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # paper = models.ForeignKey('Paper', related_name='images', on_delete=models.CASCADE)  # Внешний ключ на модель Paper

    @property
    def storage_filename(self):
        _, ext = os.path.splitext(self.file_name)
        return f"{self.id}{ext}"

    @property
    def url(self):
        return reverse('image', kwargs={'image_id': self.id})
    
    def __str__(self):
        return f"{self.id}, {self.file_name}, {self.mime_type}, {self.md5_hash}, {self.created_at}"
    

class Paper(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    content = MDTextField()
    author = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}, {self.title}, {self.content}, {self.created_at}"

