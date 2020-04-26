from django.urls import path
from . import views

urlpatterns = [
    path('',views.accueil,name="accueil"),
    path('article/<int:id>-<slug:slug>$', views.lire, name='lire'),
    path('accueil', views.home,name="home"),
    path('article/<id_article>', views.view_article),
    path('articles/<int:year>/<int:month>', views.list_articles),
    path('redirection', views.view_redirection),
    path('date', views.date_actuelle,name='afficher_date'),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    path('contact/', views.contact, name='contact'),


]