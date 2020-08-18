from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Blogger(models.Model):
    '''Model representing  author.'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length = 500)

    class Meta:
        ordering = ['user']
        
    def __str__(self):
        '''String representing Model object.'''
        return f'{self.user}'
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this author."""
        return reverse('blogger-detail', args=[str(self.id)]) 


class PostComment(models.Model):
    '''Model representing a post comment.'''
    date_time = models.DateTimeField(help_text = 'Date and time of comment')    
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, help_text = 'Author of comment')
    blog_post = models.ForeignKey('BlogPost', on_delete=models.CASCADE, help_text = 'Blog post of the comment')
    comment = models.TextField(help_text = 'Enter your comment here', max_length = 200)
    
    class Meta:
        ordering = ['date_time','commentor']

    def __str__(self):
        '''String representing Model object.'''
        date = self.date_time.date()
        time = self.date_time.time()
        return f'({self.date_time.strftime("%Y-%m-%d, %H:%M")}) - {self.comment}'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this comment."""
        return reverse('comment-detail', args=[str(self.id)]) 


class BlogPost(models.Model):
    ''' Model representing a blog post.'''
    date = models.DateField(help_text = 'Date of post')
    author = models.ForeignKey(Blogger,on_delete=models.CASCADE,help_text = 'Author of post')
    content = models.TextField(help_text = 'Enter your post here.', max_length = 1000)
    title = models.CharField(help_text = 'Title of post', max_length = 100)

    class Meta:
        ordering = ['-date','title']

    def __str__(self):
        '''String representing Model object.'''
        return f'{self.title} - {self.author} ({self.date})'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this blog."""
        return reverse('blog-detail', args=[str(self.id)]) 
