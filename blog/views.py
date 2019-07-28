from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
from blog.models import Article


def hello_world(request):
    return HttpResponse("Hello World")


def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = 'title: %s,brief_content: %s,content: %s,article_id: %s,publish_date: %s' % (
        title, brief_content, content, article_id, publish_date)
    return HttpResponse(return_str)


def get_index_page(requst):
    all_article = Article.objects.all()
    return render(requst, 'blog/index.html',
                  {
                      'article_list': all_article
                  })


def get_detail_page(requst):
    curr_article = Article.objects.all()[0]
    section_list = curr_article.content.split('\n')
    return render(requst, 'blog/detail.html',
                  {
                      'curr_article': curr_article,
                      'section_list':section_list
                  }
                  )
