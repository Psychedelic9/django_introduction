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


def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    current_article = None
    previous_article_index = 0
    next_article_index = 0
    previous_article = None
    next_article = None
    for index, article in enumerate(all_article):
        if index == 0:
            previous_article_index = 0
            next_article_index = index + 1
        elif index == len(all_article) - 1:
            previous_article_index = index - 1
            next_article_index = index
        else:
            previous_article_index = index - 1
            next_article_index = index + 1
        if article.article_id == article_id:
            current_article = article
            previous_article = all_article[previous_article_index]
            next_article = all_article[next_article_index]
            break
    section_list = current_article.content.split('\n')
    return render(request, 'blog/detail.html',
                  {
                      'curr_article': current_article,
                      'section_list': section_list,
                      'previous_article': previous_article,
                      'next_article': next_article
                  }
                  )
