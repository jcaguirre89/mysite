from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from .models import Post, Topic

def search(request):
    keywords = request.GET.get('q')
    
    qs = Post.objects.filter(
                             pub_date__lte=timezone.now()
                             ).order_by('pub_date')
    
    if keywords:
        query = SearchQuery(keywords)
        title_vector = SearchVector('post_title', weight='A')
        content_vector = SearchVector('text', weight='B')
        vectors = title_vector + content_vector
        qs = qs.annotate(search=vectors).filter(search=query)
        qs = qs.annotate(rank=SearchRank(vectors, query)).order_by('-rank')
        
    return render(request,
                  'blog/index.html',
                  {'posts': qs})


def index(request):
    posts = Post.objects.filter(
                                pub_date__lte=timezone.now()
                                ).order_by('pub_date')
    return render(request,
                  'blog/index.html',
                  {'posts': posts})


def topic(request, topic):
    topicFilter = get_object_or_404(Topic, subject=topic)
    #topicFilter = Topic.objects.get(subject=topic)
    posts = Post.objects.filter(
                                topic=topicFilter, 
                                pub_date__lte=timezone.now()
                                ).order_by('pub_date')
    return render(request,
                  'blog/index.html',
                  {'posts': posts})


def tags(request, tag):
    posts = Post.objects.filter(
                                tags__contains=[tag],
                                pub_date__lte=timezone.now()
                                ).order_by('pub_date')
    return render(request,
                  'blog/index.html',
                  {'posts': posts})


def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request,
                  'blog/detail.html',
                  {'post': post})
