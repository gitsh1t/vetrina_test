from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from colorful.fields import RGBColorField


class img_hero(models.Model):
    img = models.ImageField(upload_to="hero/%y%m%d")
    titolo_header = models.CharField(max_length=150, blank=True, default='EMMEGÌ2000')
    current = models.BooleanField(default=False)
    colore_titolo = RGBColorField(default='black') 
    class Meta:
        verbose_name = "header"
        verbose_name_plural = "headers"    
    
class publishedmanager(models.Manager):
    def get_queryset(self):
        return super(publishedmanager,self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'),)
    title = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    image = models.ImageField(upload_to='img/%y/%m/%d', blank=True)
    tags = TaggableManager()
    
    class Meta:
        ordering = ('-publish', )
        verbose_name = "prodotto"
        verbose_name_plural = "prodotti"
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
        
    
    def __str__(self):
        return self.title
    
    objects = models.Manager()
    published = publishedmanager()

#----------------------------------------------------------------------------------------------#

class Servizi(models.Model):
    nome_serv = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='ServiceImg/', blank=True)
    
    def __str__(self):
        return self.nome_serv
    class Meta:
        verbose_name = "servizio"
        verbose_name_plural = "servizi"
    
class Certificati(models.Model):
    nome_cert = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='CertificateImg/', blank=True)
    
    def __str__(self):
        return self.nome_cert
    class Meta:
        verbose_name = "certificato"
        verbose_name_plural = "certificati"
    
class home_gallery(models.Model):
    img1 = models.ImageField(upload_to ='home-gallery/1', blank=True)
    img2 = models.ImageField(upload_to ='home-gallery/2', blank=True)
    img3 = models.ImageField(upload_to ='home-gallery/3', blank=True)
    img4 = models.ImageField(upload_to ='home-gallery/4', blank=True)
    img5 = models.ImageField(upload_to ='home-gallery/5', blank=True)
    img6 = models.ImageField(upload_to ='home-gallery/6', blank=True)
    img7 = models.ImageField(upload_to ='home-gallery/7', blank=True)
    img8 = models.ImageField(upload_to ='home-gallery/8', blank=True)
    img9 = models.ImageField(upload_to ='home-gallery/9', blank=True)
    img10 = models.ImageField(upload_to ='home-gallery/10', blank=True)
    updated = models.DateTimeField(auto_now=True)
    current = models.BooleanField(default=False)
    class Meta:
        verbose_name = "galleria home"
        verbose_name_plural = "gallerie home"


class slider_1(models.Model):
    image_prima_slide = models.ImageField(upload_to ='img-slider-1/1', blank=True)
    image_seconda_slide = models.ImageField(upload_to ='img-slider-1/2', blank=True)
    image_terza_slide = models.ImageField(upload_to ='img-slider-1/3', blank=True)
    descrizione_prima_slide = models.CharField(max_length=20, blank=True)
    descrizione_seconda_slide = models.CharField(max_length=20, blank=True)
    descrizione_terza_slide = models.CharField(max_length=20, blank=True)
    titolo_prima_slide = models.CharField(max_length=20, blank=True)
    titolo_seconda_slide = models.CharField(max_length=20, blank=True)
    titolo_terza_slide = models.CharField(max_length=20, blank=True)
    content_prima_slide = models.TextField(blank=True)
    content_seconda_slide = models.TextField(blank=True)
    content_terza_slide = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    current = models.BooleanField(default = False)
    class Meta:
        verbose_name = "primo slider"
        verbose_name_plural = "primo slider"

class slider_2(models.Model):
    image_prima_slide = models.ImageField(upload_to ='img-slider-2/1', blank=True)
    image_seconda_slide = models.ImageField(upload_to ='img-slider-2/2', blank=True)
    image_terza_slide = models.ImageField(upload_to ='img-slider-2/3', blank=True)
    descrizione_prima_slide = models.CharField(max_length=20, blank=True)
    descrizione_seconda_slide = models.CharField(max_length=20, blank=True)
    descrizione_terza_slide = models.CharField(max_length=20, blank=True)
    titolo_prima_slide = models.CharField(max_length=20, blank=True)
    titolo_seconda_slide = models.CharField(max_length=20, blank=True)
    titolo_terza_slide = models.CharField(max_length=20, blank=True)
    content_prima_slide = models.TextField(blank=True)
    content_seconda_slide = models.TextField(blank=True)
    content_terza_slide = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    current = models.BooleanField(default = False)
    class Meta:
         verbose_name = "secondo slider"
         verbose_name_plural = "secondo slider"
         
class titoli_landing_page(models.Model):
    scritta_centrale_pagina = models.CharField(max_length=50)
    colore_scritta_centrale = RGBColorField(default='black') 
    titolo_catalogo_prodotti = models.CharField(max_length=50)
    colore_titolo_catalogo = RGBColorField(default='blue')
    updated = models.DateTimeField(auto_now=True)
    current = models.BooleanField(default=False)
    class Meta:
        verbose_name = "titoli su landing page"
        verbose_name_plural = "titoli su landing page"
        
class content_chisiamo(models.Model):
    titoli = models.CharField(max_length=100)
    contenuto = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    current = models.BooleanField(default=False)
    class Meta:
         verbose_name = "contenuti pagina 'Chi Siamo'"
         verbose_name_plural = "contenuti pagina 'Chi Siamo'"
class content_mappa(models.Model):
    titolo = models.CharField(max_length=50)
    sottotitolo = models.CharField(max_length=100)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    current = models.BooleanField(default=False)
    api_key_mappa = models.CharField(max_length=250)
    api_key_captcha = models.CharField(max_length=250, default='nokey')
    class Meta:
        verbose_name = "contenuti pagina 'Mappa' e api key Captcha"
        verbose_name_plural = "contenuti pagina 'Mappa' e api key Captcha"

class candidato(models.Model):
    ruoli = (
        ('1','INFORMATICO'),
        ('2','MECCANICO'),
        ('3','SALDATORE'),
        ('4','ELETTRICISTA'),      
    )
    anni_di_esperienza = (
        ('1','nessuna esperienza'),
        ('2','meno di un anno'),
        ('3','1 anno o più'),
    )
    
    scelta_ruolo = models.CharField(
        choices=ruoli,
        default='1',
        max_length=1,
    )
    esperienza = models.CharField(
        choices=anni_di_esperienza,
        default='1',
        max_length=1,
    )
    nome_candidato = models.CharField(max_length=120)
    cognome_candidato = models.CharField(max_length=120)
    indirizzo_candidato = models.CharField(max_length=120)
    email_candidato = models.EmailField()
    cellulare_candidato = models.CharField(max_length=10)
    cv = models.FileField(upload_to='candidati/curricula/cv_%y%m%d')
    class Meta:
        verbose_name = "candidato per assunzioni"
        verbose_name_plural =  "candidati per assunzione" 
    
class link_footer(models.Model):
    numero_telefonico_1 = models.CharField(max_length=10)
    numero_telefonico_2 = models.CharField(max_length=10)
    indirizzo_mail = models.EmailField()
    partita_IVA = models.CharField(max_length=11)
    titolo_link_1 = models.CharField(max_length=30)
    titolo_link_2 = models.CharField(max_length=30)
    titolo_link_3 = models.CharField(max_length=30)
    link_1 = models.CharField(max_length=100)
    link_2 = models.CharField(max_length=100)
    link_3 = models.CharField(max_length=100)
    logo = models.ImageField(upload_to ='Logo/%y%m%d', blank=True)
    current = models.BooleanField(default=False)
    class Meta:
        verbose_name = "gestione footer"
        verbose_name_plural = "gestione footer"    
    
class banner_lavora_con_noi(models.Model):
    immagine = models.ImageField(upload_to ='Banner_chisiamo/%y%m%d', blank=True)
    titolo_banner = models.CharField(max_length=50)
    sottotitolo_banner = models.CharField(max_length=100)
    current = models.BooleanField(default=False)
    class Meta:
        verbose_name = "banner pagina 'lavora con noi"
        verbose_name_plural = "banner pagina 'lavora con noi"

class content_lavora_con_noi(models.Model):
    titolo_paragrafo_1 = models.CharField(max_length=30)
    titolo_paragrafo_2 = models.CharField(max_length=30)
    paragrafo_1 = models.TextField()
    paragrafo_2 = models.TextField()
    current = models.BooleanField(default=False)
    class Meta:
        verbose_name = "contenuti pagina 'lavora con noi'"
        verbose_name_plural = "contenuti pagina 'lavora con noi'"
#----------------------------------------------------------------------------------------------#

class nuovo_utente(models.Model):
    user = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE )
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    cellulare = models.CharField(max_length=25, blank=True)
    email = models.EmailField()
    creazione = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user
        
    
class Commenti(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='commenti')
    nome = models.CharField(max_length=80)
    email = models.EmailField()
    corpo = models.TextField()
    creato = models.DateTimeField(auto_now_add=True)
    aggiornato = models.DateTimeField(auto_now=True)
    attivo = models.BooleanField(default=True)

    class Meta:
        ordering = ('creato',)
    
    def __str__(self):
        return f'Commento pubblicato da {self.nome} sul post {self.post}'
        
        