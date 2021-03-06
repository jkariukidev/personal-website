from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

from autoslug.fields import AutoSlugField

User = get_user_model()


class Post(models.Model):
    """Post model"""
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title', unique=True, editable=True)
    header_image = models.ImageField(null=True, blank=False, upload_to="images")
    body = RichTextField(blank=True, null=True)
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50, default='Uncategorized')
    snippet = models.CharField(max_length=255, default='')
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )

    def get_absolute_url(self):
        """
        Return the canonical URL of the post.
        """
        return reverse('website:article-detail', args=[self.slug])

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title + ' | ' + str(self.author)


class PostComment(models.Model):
    """
    Comment for blog posts.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'


class EmailMessage(models.Model):
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=300)


