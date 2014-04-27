from blog.models import Article, Tag, Classification
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404


def blog_list(request):
    blogs = Article.objects.all().order_by('-publish_time')
    tags = Tag.objects.all()
                
    return render_to_response('blog_list.html', {"blogs": blogs, "tags": tags}, context_instance=RequestContext(request))


def blog_detail(request, id=''):
    try:
        blog = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    return render_to_response("blog_show.html", {"blog": blog}, context_instance=RequestContext(request))


def blog_filter(request, id=''):
    tags = Tag.objects.all()
    tag = Tag.objects.get(id=id)
    blogs = tag.blog_set.all()
    return render_to_response("blog_show.html", {"blogs": blogs, "tag": tag, "tags": tags})


def blog_show_comment(request, id=''):
    blog = Article.objects.get(id=id)
    return render_to_response('blog_comments_show.html', {"blog": blog})