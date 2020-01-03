from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), default=None, on_delete=models.CASCADE)
    title = models.CharField('title', max_length=128)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    preview_text = models.TextField('preview text', max_length=512, blank=True)
    content = models.TextField('content', max_length=4096, blank=True)
    slug = models.SlugField('slug', max_length=100)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title

    @property
    def preview(self):
        return self.preview_text or self.content[:512].rsplit(' ', 1)[0]
