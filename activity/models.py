from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink

class Activity(models.Model):

    name = models.CharField(blank=False,max_length=255)
    slug = models.SlugField(unique=True,help_text="Used for the Group URL: http://example.com/groups/the-club/")
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)
    creator = models.ForeignKey(User,related_name='created_activity')
    modified = models.DateTimeField(auto_now=True)

    @permalink 
    def get_absolute_url(self):
        return ('activity:activity_detail',None,{'slug':self.slug})


