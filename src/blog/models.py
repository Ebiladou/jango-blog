from django.db import models
from django.utils.text import slugify

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    ('archived', 'Archived'),
)

class Blog_category (models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.name

class Blog_post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    category = models.ForeignKey(Blog_category, on_delete=models.CASCADE, related_name='posts')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comments (models.Model):
    post = models.ForeignKey(Blog_post, on_delete=models.CASCADE, related_name="comments")
    email = models.EmailField(blank=True, null=True, max_length=254)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE, 
        related_name='replies')
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'