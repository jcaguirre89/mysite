from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Topic(models.Model):
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.subject   


class Post(models.Model):
    text = models.TextField(null=False, blank=True)
    post_title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(default=timezone.now)
    last_update = models.DateField(auto_now=True)    
    summary = models.CharField(max_length=450)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    tags = ArrayField(models.CharField(max_length=50), default=list) 
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='blog')

    #string for name
    def __str__(self):
        return self.post_title
    
    def get_absolute_url(self):
        return '/blog/'+str(self.id)+'/'

    