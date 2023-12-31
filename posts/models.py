from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = (
        ('writing', 'Writing in Progress'),
        ('ready_for_edits', 'Ready for Edits'),
        ('in_edits', 'In Edits'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    teaser_text = models.TextField()
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag , blank=True)
    slug = models.SlugField(null=False , unique=True, max_length=100)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail" , kwargs={"slug": self.slug})

class HomepageSection(models.Model):
    name = models.CharField(max_length=30, unique=True)
    posts = models.ManyToManyField(Post, through='HomepageSectionOrder')
    def __str__(self):
        return self.name

class HomepageSectionOrder(models.Model):
    section = models.ForeignKey(HomepageSection, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='homepagesectionorder_set')
    order = models.IntegerField()

    def __str__(self):
        return self.post.title

