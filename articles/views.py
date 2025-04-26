from django.shortcuts import render, get_object_or_404

from .models import Article, Comment

# Create your views here.

def home_view(request):
    """
    Renders the homepage with the 5 most recent blog posts.
    """
    articles = Article.objects.order_by("-id")[:5]
    return render(request, "home.html", {"articles": articles})

def article_list_view(request):
    """
    Display the full list of blog posts.
    """
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "article_list.html", context)

def article_detail_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = Comment.objects.filter(article_id=article_id).select_related("user")

    context = {"article": article, "comments": comments}
    return render(request, "article_detail.html", context)