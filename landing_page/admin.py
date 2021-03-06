from django.contrib import admin
from django.contrib.admin import site
from .models import Post, Commenti, slider_1, slider_2, home_gallery, titoli_landing_page, content_chisiamo, content_mappa, candidato, link_footer, banner_lavora_con_noi, content_lavora_con_noi, Servizi, Certificati, img_hero    
import adminactions.actions as actions

actions.add_to_site(site)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title','body')
    prepopulated_fields = {'slug' : ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status','publish')
    
@admin.register(slider_1)
class immagini_slider(admin.ModelAdmin):
    list_display = ('id', 'current', 'image_prima_slide', 'image_seconda_slide', 'image_terza_slide', 'descrizione_prima_slide', 'descrizione_seconda_slide', 'descrizione_terza_slide')
    ordering = ('updated','current')
@admin.register(slider_2)
class immagini_slider(admin.ModelAdmin):
    list_display = ( 'id', 'current', 'image_prima_slide', 'image_seconda_slide', 'image_terza_slide', 'descrizione_prima_slide', 'descrizione_seconda_slide', 'descrizione_terza_slide')
    orering = ('updated','current')
@admin.register(home_gallery)
class immagini_gallery(admin.ModelAdmin):
    list_display = ('id', 'current', 'img1', 'img2', 'img3', 'img4', 'img5', 'img6', 'img7', 'img8', 'img9', 'img1')
    ordering = ('updated','current')
    
@admin.register(titoli_landing_page)
class titoli_landing_page(admin.ModelAdmin):
    list_display = ('id', 'current', 'scritta_centrale_pagina', 'colore_scritta_centrale', 'titolo_catalogo_prodotti', 'colore_titolo_catalogo')
    
@admin.register(content_chisiamo)
class contenuti_chi_siamo(admin.ModelAdmin):
    list_display = ('id','current', 'titoli', 'contenuto')

@admin.register(content_mappa)
class contenuti_mappa(admin.ModelAdmin):
    list_display = ('id', 'current', 'titolo', 'sottotitolo', 'content','api_key_mappa', 'api_key_captcha')
	
@admin.register(candidato)
class candidati(admin.ModelAdmin):
    list_display = ('id', 'scelta_ruolo','esperienza' ,'nome_candidato', 'cognome_candidato', 'indirizzo_candidato', 'email_candidato', 'cellulare_candidato', 'cv')	
	
@admin.register(link_footer)
class link_footer(admin.ModelAdmin):
    list_display = ('id', 'current', 'numero_telefonico_1', 'numero_telefonico_2', 'indirizzo_mail', 'partita_IVA', 'titolo_link_1', 'titolo_link_2', 'titolo_link_3', 'link_1', 'link_2', 'link_3', 'logo')

@admin.register(banner_lavora_con_noi)
class banner_lavora_con_noi(admin.ModelAdmin):
    list_display = ('id', 'current', 'immagine', 'titolo_banner', 'sottotitolo_banner')

@admin.register(content_lavora_con_noi)
class content_lavora_con_noi(admin.ModelAdmin):
    list_display = ('id', 'current', 'titolo_paragrafo_1', 'paragrafo_1', 'titolo_paragrafo_2', 'paragrafo_2')

@admin.register(Servizi)
class Servizi(admin.ModelAdmin):
    list_display = ('id', 'nome_serv', 'slug', 'body')
    
@admin.register(Certificati)
class Certificati(admin.ModelAdmin):
    list_display = ('id', 'nome_cert', 'slug', 'body')    
    
@admin.register(img_hero)
class header(admin.ModelAdmin):
    list_display = ('id', 'img', 'titolo_header', 'colore_titolo', 'current')


