from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('writing', 'Writing in Progress'),
        ('ready_for_edits', 'Ready for Edits'),
        ('in_edits', 'In Edits'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    teaser_text = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class HomepageSection(models.Model):
    name = models.CharField(max_length=30, unique=True)
    posts = models.ManyToManyField(Post, through='HomepageSectionOrder')

class HomepageSectionOrder(models.Model):
    section = models.ForeignKey(HomepageSection, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='homepagesectionorder_set')
    order = models.IntegerField()
