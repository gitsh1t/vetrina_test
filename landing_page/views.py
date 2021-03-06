#generali
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count 
from django.contrib import messages
from django.contrib.auth import get_user_model
from django_email_verification import send_email
#blog
#tag engine
from taggit.models import Tag
#paginator per blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#modelli per gestire i post del blog
from .models import Post, Commenti, slider_1, slider_2, home_gallery, titoli_landing_page, content_chisiamo, content_mappa, candidato, link_footer, banner_lavora_con_noi,content_lavora_con_noi,Servizi,Certificati, img_hero
#autenticazione e registrazione
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm
#form vari
from .forms import nome_utente, password, EmailPostForm, FormCommenti, registrazione, lavoraconnoi
#chat
from django.core.mail import send_mail
import socket
#API REST
#framework
from rest_framework import generics
#serializzatore
from .serializers import post_serializer

#classi per API REST
#lista Post API
class post_list_api(generics.ListAPIView):
    #query da visualizzare
    queryset = Post.objects.all()
    #serializzazione query
    serializer_class = post_serializer
    
#dettagli Post API
class post_detail_api(generics.RetrieveAPIView):
	#query da visualizzare
	queryset = Post.objects.all()
	#serializzazione query
	serializer_class = post_serializer
#lista servizi
def serv_list(request,nome=None):
    hero = img_hero.objects.filter(current = True).first()
    servizi = Servizi.objects.all()
    titoli = titoli_landing_page.objects.filter(current=True).first()
    footer = link_footer.objects.filter(current=True).first()
    #dettaglio servizio
    if nome:
        nome_servizio = get_object_or_404(Servizi, slug=nome)
        template = loader.get_template('landing_page/servizio.html')
        return render(request, 'landing_page/servizio.html', {'nome_servizio':nome_servizio , 'footer':footer , 'titoli':titoli,})      
    template = loader.get_template('landing_page/serv_list.html')
    return render(request, 'landing_page/serv_list.html', {'servizi':servizi, 'footer':footer, 'titoli':titoli, })

#lista certificati
def cert_list(request,nome_certificato=None):
    hero = img_hero.objects.filter(current = True).first()
    certificati = Certificati.objects.all()[:5]
    titoli = titoli_landing_page.objects.filter(current=True).first()
    footer = link_footer.objects.filter(current=True).first()
    #dettaglio certificato
    if nome_certificato:
        certificato = get_object_or_404(Certificati, slug=nome_certificato)
        template = loader.get_template('landing_page/certificato.html')
        return render(request, 'landing_page/certificato.html', {'certificato': certificato , 'footer':footer, 'titoli':titoli, 'hero': hero })
    template = loader.get_template('landing_page/serv_list.html')
    return render(request, 'landing_page/cert_list.html', {'certificati':certificati, 'footer':footer , 'titoli':titoli, 'hero': hero})

#home page e link homepage
def index(request):
    hero = img_hero.objects.filter(current = True).first()
    slide1 = slider_1.objects.filter(current=True).first()
    slide2 = slider_2.objects.filter(current=True).first()
    galleria = home_gallery.objects.filter(current=True).first()
    titoli = titoli_landing_page.objects.filter(current=True).first()
    footer = link_footer.objects.filter(current=True).first()
    template = loader.get_template('landing_page/index.html')
    return render(request, 'landing_page/index.html', {'slide1': slide1, 'slide2': slide2, 'galleria' : galleria, 'titoli':titoli, 'footer':footer, 'hero' : hero })

def chisiamo(request):
    hero = img_hero.objects.filter(current = True).first()
    galleria_chisiamo = Post.objects.all()
    footer = link_footer.objects.filter(current=True).first()
    titoli = titoli_landing_page.objects.filter(current=True).first()
    contenuto = content_chisiamo.objects.filter(current=True).first()
    template = loader.get_template('landing_page/chi_siamo.html')
    return render(request, 'landing_page/chi_siamo.html', {'galleria_chisiamo' : galleria_chisiamo, 'contenuto' : contenuto, 'footer':footer , 'titoli':titoli, 'hero': hero})
def mappa(request):
    hero = img_hero.objects.filter(current = True).first()
    footer = link_footer.objects.filter(current=True).first()
    titoli = titoli_landing_page.objects.filter(current=True).first()
    contenuto = content_mappa.objects.filter(current=True).first()
    template = loader.get_template('landing_page/mappa.html')
    return render(request, 'landing_page/mappa.html', {'contenuto' : contenuto, 'footer':footer  , 'titoli':titoli, 'hero': hero})
    


def registrati(request):
    hero = img_hero.objects.filter(current = True).first()
    footer = link_footer.objects.filter(current=True).first()
    contenuto = content_mappa.objects.filter(current=True).first()
    titoli = titoli_landing_page.objects.filter(current=True).first()
    form = 	registrazione()
    if request.method == "POST":
        form = registrazione(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
                      #Conferma creazione account via email#
                      #da completare#
            #-----------------------------------------------------------#            
            #email = form.cleaned_data.get("email")
            #user = get_user_model().objects.create(username=usernameT, password=password, email=email)
            #user.is_active = False  # Example
            #send_email(user)
            #-----------------------------------------------------------#
            
            messages.success(request, 'Account creato,benvenuto,' + username + '!')
            return redirect('/landing_page/')
    return render(request, 'landing_page/registrati.html', {'form' : form, 'contenuto' : contenuto, 'footer':footer , 'titoli':titoli, 'hero': hero})  

def lavora_con_noi(request):
    hero = img_hero.objects.filter(current = True).first()
    titoli = titoli_landing_page.objects.filter(current=True).first()
    footer = link_footer.objects.filter(current=True).first()
    contenuto = content_lavora_con_noi.objects.filter(current=True).first()
    banner = banner_lavora_con_noi.objects.filter(current=True).first()
    if request.method == 'POST':
        forml = lavoraconnoi(request.POST, request.FILES)
        if forml.is_valid():
            forml.save()
            return redirect('/landing_page/')
    else:
        forml = lavoraconnoi()
    return render(request, 'landing_page/lavora_con_noi.html', {'forml' : forml, 'footer':footer, 'contenuto':contenuto, 'banner':banner , 'titoli':titoli, 'hero': hero}) 






    
#gestione login
def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'landing_page/index.html', c)
def logout(request):
    logout(request)
    redirect('landing_page/index')
#autenticazione dei dati inseriti in "login"
def authentication(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')
#gestione post
#lista post
#-------------------------------------------------------------------------------------------------------------------------------------------------------#
def post_list(request, tag_slug=None):
    hero = img_hero.objects.filter(current = True).first()
    titoli = titoli_landing_page.objects.filter(current=True).first()
    footer = link_footer.objects.filter(current=True).first()
    object_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list =  object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'landing_page/post/list.html', {'page': page, 'posts': posts, 'tag': tag, 'footer':footer , 'titoli':titoli, 'hero': hero})
#-------------------------------------------------------------------------------------------------------------------------------------------------------#
#view post singolo
def post_detail(request, year, month, day, post):
    hero = img_hero.objects.filter(current = True).first()
    titoli = titoli_landing_page.objects.filter(current=True).first()
    footer = link_footer.objects.filter(current=True).first()
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    #lista di commenti attivi sul blog 
    commenti = post.commenti.filter(attivo=True)
    new_comment = None
    
    if request.method == 'POST':
        #?? stato postato un commento
        form_commento = FormCommenti(data=request.POST)
        if form_commento.is_valid():
            #creazione di un oggetto commento senza salvataggio su db#
            nuovo_commento = form_commento.save(commit=False)
            #assegna il post corrente al commento# 
            nuovo_commento.post = post
            #salvataggio del commento su db#
            nuovo_commento.save()
            #lista di post simili#
            post_tags_ids = post.tags.values_list('id', flat=True)
            post_simili = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
            post_simili = post_simili.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]
            return render(request, 'landing_page/post/detail.html', {'post' : post, 'commenti' : commenti, 'nuovo_commento' : nuovo_commento, 'form_commento' : form_commento, 'post_simili' : post_simili, 'footer':footer , 'titoli':titoli, 'hero': hero})
    else:
        form_commento = FormCommenti()
        #lista di post simili#
        post_tags_ids = post.tags.values_list('id', flat=True)
        post_simili = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
        post_simili = post_simili.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]
        return render(request, 'landing_page/post/detail.html', {'post' : post, 'commenti' : commenti, 'form_commento' : form_commento, 'post_simili' : post_simili, 'footer':footer , 'titoli':titoli, 'hero': hero})
#condivisione post via e-mail
def post_share(request, post_id):
    hero = img_hero.objects.filter(current = True).first()
    titoli = titoli_landing_page.objects.filter(current=True).first()
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
        #validazione dati nel form
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            titolo = f"{cd['name']} vorrebbe farti leggere questo: {post.title}"
            messaggio = f"{post_url}\n\n {cd['comments']}"
                                 #invio effettivo mail# 
            #-----------------------------------------------------------------#
            send_mail(titolo,messaggio,'espositogerardo94@gmail.com',[cd['to']])
            #-----------------------------------------------------------------#
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'landing_page/post/share.html',{'post' : post, 'form' : form, 'sent' : sent, 'hero': hero })
