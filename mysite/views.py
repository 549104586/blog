from django.shortcuts import render
from django.http import  HttpResponse
from . import models
from django.utils.timezone import  now,timedelta


# Create your views here.
def index(request):
   # art = models.Article.objects.create(title=now(),content='happy ending')
    print('------------------------------------------')
   # print(art.content)
   # art.save()
    article = models.Article.objects.all()
    print(article)
    return render(request,'index.html',{'article':article})

def showContent(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    content = {
        'article_title':article.title,
        'article_content':article.content
    }
    print(content)

    return render(request,'show.html',content)


def base(request):
    content={'good':'good'}
    return render(request,'base.html',content)