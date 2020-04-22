from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect
from blog.models import Article


# Create your views here.

def home(request):
    return render(request,'blog/accueil.html',locals())

def view_article(request, id_article):
    if id_article>100:
         raise Http404
    return redirect(view_redirection)

def view_redirection(request):
    return HttpResponse(""" Vous avez été redirigé.""")

def list_articles(request, year, month):
    return redirect("http://www.djangoproject.com")


def date_actuelle(request):
    return render(request,'blog/date.html',{'date': datetime.now()})

def addition(request, nombre1, nombre2):
    total = nombre1+nombre2
    return render(request,'blog/addition.html',locals())

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all()  # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

def lire(request, id):
    """ Afficher un article complet """
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'blog/lire.html', {'article': article})