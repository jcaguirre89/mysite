from django.db import models
from markdownx.models import MarkdownxField
from django.utils import timezone
from django.utils.html import mark_safe
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Topic(models.Model):
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.subject   

class Post(models.Model):
    text = models.TextField(null=False, blank=True)
    #text = MarkdownxField()
    post_title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(default=timezone.now)
    last_update = models.DateField(auto_now=True)    
    summary = models.CharField(max_length = 450)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    tags = ArrayField(models.CharField(max_length=50), default=list) 
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='blog')


    #string for name
    def __str__(self):
        return self.post_title
    
    def get_absolute_url(self):
        return '/blog/'+str(self.id)+'/'
"""
class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField()
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})

"""


#class Image(models.Model):
#    post = models.ForeignKey(Post, on_delete=models.CASCADE)



    #def was_published_recently(self):
    #    now=timezone.now()
    #    return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    #was_published_recently.admin_order_field = 'pub_date'
    #was_published_recently.boolean = True
    #was_published_recently.short_description = 'Published recently?'
    
    