from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, reverse
from .models import Article, Subscribe, ArticleView, Author
from django.db.models.query_utils import Q
from .forms import CommentForm
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    feautred_articles = Article.objects.filter(is_english=True).filter(
        is_feautred=True).order_by('-timestamp')[:5]
    latest_articles = Article.objects.filter(
        is_english=True).order_by('-timestamp')[:3]
    # trending_articles = Article.objects.filter(is_english=True).order_by('-view_count')[:3]

    context = {
        'feautred_articles_5': feautred_articles,
        'latest_articles_3': latest_articles,
    }
    if request.method == 'POST':
        newSubscibe = Subscribe()
        newSubscibe.name = request.POST['name']
        newSubscibe.email = request.POST['email']
        newSubscibe.save()

        return redirect(reverse('home'))

    return render(request, 'index.html', context)


def blog(request):
    queryset = Article.objects.filter(is_english=True)
    paginator = Paginator(queryset, 9)
    page_request_name = "page"
    page = request.GET.get(page_request_name)
    try:
        paginted_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginted_queryset = paginator.page(1)
    except EmptyPage:
        paginted_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginted_queryset,
        'page_request_name': page_request_name
    }
    return render(request, 'blog.html', context)


def error_404(request, exception):
    return render(request, '404.html')


def about(request):
    return render(request, 'about.html')


def search(request):
    article_list = Article.objects.filter(is_english=True)
    query = request.GET.get('q')

    if query:
        article_list = article_list.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    else:
        return redirect(reverse('blog'))

    context = {
        'query': 'You Searched for: ' + query.title(),
        'queryset': article_list
    }
    return render(request, 'search_result.html', context)


def article_detail(request, id):
    article = Article.objects.get(id=id)

    if request.user.is_authenticated:
        ArticleView.objects.get_or_create(user=request.user, article=article)

    commentForm = CommentForm(request.POST or None)
    if request.method == 'POST':
        if commentForm.is_valid():
            commentForm.instance.user = request.user
            commentForm.instance.article = article
            commentForm.save()
            return redirect(reverse('article', kwargs={"id": article.id}))

    context = {
        'article': article, 'form': commentForm
    }

    return render(request, 'article_detail.html', context)


def contact(request):

    if request.method == 'POST':
        send_mail(
            request.POST['name'],
            request.POST['content'],
            request.POST['email'],
            [settings.EMAIL_HOST_USER],
            fail_silently=False
        )

        return render(request, 'contact.html', {'message_name': request.POST['name']})

    return render(request, 'contact.html', {})


def author(request, id):
    author = Author.objects.get(id=id)
    author_articles = Article.objects.filter(author=author)

    context = {
        'author': author,
        'author_articles': author_articles
    }
    return render(request, 'author.html', context)
