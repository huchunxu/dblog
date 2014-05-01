from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from blog.models import Article, Tag, Author
from blog.forms import BlogForm, TagForm
import re


def blog_list(request):
    blogs = Article.objects.all().order_by('-publish_time')
    tags = Tag.objects.all()
    return render_to_response('blog_list.html',
           {"blogs": blogs, "tags": tags}, context_instance=RequestContext(request))


def blog_del(request, id=""):
    try:
        blog = Article.objects.get(id=id)
    except Exception:
        raise Http404
    if blog:
        blog.delete()
        return HttpResponseRedirect("/blog/bloglist/")
    blogs = Article.objects.all()
    return render_to_response("blog_list.html", {"blogs": blogs})


def blog_show(request, id=''):
    try:
        blog = Article.objects.get(id=id)
        tags = Tag.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render_to_response("blog_show.html",
           {"blog": blog, "tags": tags}, context_instance=RequestContext(request))


def blog_filter(request, id=''):
    tags = Tag.objects.all()
    tag = Tag.objects.get(id=id)
    blogs = tag.article_set.all().order_by('-publish_time')
    return render_to_response("blog_filter.html", {"blogs": blogs, "tag": tag, "tags": tags})


def blog_show_comment(request, id=''):
    blog = Article.objects.get(id=id)
    return render_to_response('blog_comments_show.html', {"blog": blog})


def blog_search(request):
    tags = Tag.objects.all()
    if 'search' in request.GET:
        search = request.GET['search']
        blogs = Article.objects.filter(caption__icontains=search).order_by('-publish_time')
        return render_to_response('blog_filter.html',
            {"blogs": blogs, "tags": tags}, context_instance=RequestContext(request))
    else:
        blogs = Article.objects.order_by('-id')
        return render_to_response("blog_list.html", {"blogs": blogs, "tags": tags},
            context_instance=RequestContext(request))


def blog_add(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        tag = TagForm(request.POST)
        if form.is_valid() and tag.is_valid():
            cd = form.cleaned_data
            cdtag = tag.cleaned_data
            tagname = cdtag['tag_name']
            tagnamelist = re.split(',| ', tagname)
            for taglist in tagnamelist:
                if taglist != '':
                    Tag.objects.get_or_create(tag_name=taglist.strip())
            title = cd['caption']
            author = Author.objects.get(id=1)
            content = cd['content']
            blog = Article(caption=title, author=author, content=content)
            blog.save()
            for taglist in tagnamelist:
                if taglist != '':
                    blog.tags.add(Tag.objects.get(tag_name=taglist.strip()))
                    blog.save()
            id = Article.objects.order_by('-id')[0].id
            return HttpResponseRedirect('/blog/%s' % id)
    else:
        form = BlogForm()
        tag = TagForm()
    return render_to_response('blog_add.html',
        {'form': form, 'tag': tag}, context_instance=RequestContext(request))


def blog_update(request, id=""):
    id = id
    if request.method == 'POST':
        form = BlogForm(request.POST)
        tag = TagForm(request.POST)
        if form.is_valid() and tag.is_valid():
            cd = form.cleaned_data
            cdtag = tag.cleaned_data
            tagname = cdtag['tag_name']
            #tagnamelist = tagname.split(',| ')
            tagnamelist = re.split(',| ', tagname)
            for taglist in tagnamelist:
                Tag.objects.get_or_create(tag_name=taglist.strip())
            title = cd['caption']
            content = cd['content']
            blog = Article.objects.get(id=id)
            if blog:
                blog.caption = title
                blog.content = content
                blog.save()
                for taglist in tagnamelist:
                    blog.tags.add(Tag.objects.get(tag_name=taglist.strip()))
                    blog.save()
                tags = blog.tags.all()
                for tagname in tags:
                    tagname = unicode(str(tagname), "utf-8")
                    if tagname not in tagnamelist or tagname == '':
                        notag = blog.tags.get(tag_name=tagname)
                        blog.tags.remove(notag)
            else:
                blog = Article(caption=blog.caption, content=blog.content)
                blog.save()
            return HttpResponseRedirect('/blog/%s' % id)
    else:
        try:
            blog = Article.objects.get(id=id)
        except Exception:
            raise Http404
        form = BlogForm(initial={'caption': blog.caption, 'content': blog.content}, auto_id=False)
        tags = blog.tags.all()
        if tags:
            taginit = ''
            for x in tags:
                taginit += str(x) + ' '
            tag = TagForm(initial={'tag_name': taginit})
        else:
            tag = TagForm()
    return render_to_response('blog_add.html',
        {'blog': blog, 'form': form, 'id': id, 'tag': tag},
        context_instance=RequestContext(request))
