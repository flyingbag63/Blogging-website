from django.shortcuts import render, get_object_or_404
from blog.models import Blogger, BlogPost, PostComment
from django.contrib.auth.models import User
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from blog.forms import AddCommentForm

import datetime


# Create your views here.

def get_blogs_and_comments(request, context):
    user = request.user
    if not user.is_authenticated:
        return
    try:
        curr_blogger = Blogger.objects.get(id=user.id)
        blogs_written = BlogPost.objects.filter(author=curr_blogger).count()
    except:
        blogs_written = 0

    comments_written = PostComment.objects.filter(commentor=user).count()

    context['blogs_written'] = blogs_written
    context['comments_written'] = comments_written

def add_comment(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    user = request.user

    if request.method == 'POST':
        form = AddCommentForm(request.POST)

        if form.is_valid():
            comment_object = PostComment(date_time=datetime.datetime.now(), commentor=user, blog_post=blog, comment=form.cleaned_data['comment'])
            comment_object.save()

            return HttpResponseRedirect(reverse('blog-detail', args=[blog.id]))
    else:
        form = AddCommentForm(initial={})

    context = {
        'form': form,
        'blog': blog
        }

    get_blogs_and_comments(request, context)

    return render(request,'blog/add_comment.html', context=context)
        

def index(request):
    '''View function for home page.'''

    user = request.user
    
    total_bloggers = Blogger.objects.all().count()
    total_blogs = BlogPost.objects.all().count()
    total_users = User.objects.exclude(is_superuser=True).count()
    averge_comments_per_blog = PostComment.objects.all().count()//total_blogs
    average_comments_per_user = PostComment.objects.all().count()//total_users

    context = {
        'total_bloggers': total_bloggers,
        'total_blogs': total_blogs,
        'total_users': total_users,
        'averge_comments_per_blog': averge_comments_per_blog,
        'average_comments_per_user': average_comments_per_user,
        }

    get_blogs_and_comments(request, context)

    return render(request, 'index.html', context=context)

class BlogListView(generic.ListView):
    model = BlogPost
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        get_blogs_and_comments(self.request, context)
        return context

class BlogDetailView(generic.DetailView):
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['comments'] = BlogPost.objects.get(pk=self.object.id).postcomment_set.all
        get_blogs_and_comments(self.request, context)
        return context

class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(BloggerListView, self).get_context_data(**kwargs)
        get_blogs_and_comments(self.request, context)
        return context

class BloggerDetailView(generic.DetailView):
    model = Blogger

    def get_context_data(self, **kwargs):
        context = super(BloggerDetailView, self).get_context_data(**kwargs)
        context['blogs'] = Blogger.objects.get(pk=self.object.id).blogpost_set.all
        get_blogs_and_comments(self.request, context)
        return context
