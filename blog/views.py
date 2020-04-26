from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect, get_object_or_404
from blog.models import Article
from .forms import ContactForm
# Create your views here.

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'blog/contact.html', locals())



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

def lire(request, id,slug):
    """ Afficher un article complet """
    article = get_object_or_404(Article,id=id,slug=slug)

    return render(request, 'blog/lire.html', {'article': article})