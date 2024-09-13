from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField 

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})
 
 
class Post(models.Model):
    title = models.CharField(max_length=200)
    header_image = models.ImageField(null=True, blank=True,upload_to="images/")
    content = RichTextField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=255,default='uncategorised')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
   
 
    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})
 
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)