from django.contrib import admin
from django.urls import path, include
from .feeds import LatestPostFeed 
from .views import post_detail_api, post_list_api
from . import views

app_name="blog"

urlpatterns = [
    path('chisiamo/', views.chisiamo, name='chi_siamo'),
    path('lavoraconnoi/', views.lavora_con_noi, name='lavora_con_noi'),
    path('mappa/', views.mappa, name='mappa'),
    path('registrati/', views.registrati, name='registrati'),
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('product_list/', views.post_list, name='post_list'),
    path('cert_list/', views.cert_list, name="cert_list"),
    path('certificato/<slug:nome_certificato>', views.cert_list, name="certificato"),
    path('serv_list/', views.serv_list, name="serv_list"), 
    path('servizio/<slug:nome>', views.serv_list, name="servizio"),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_per_tag'),
    path('post_detail/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('feed/', LatestPostFeed(), name='post_feed'),
    path('api_detail/<int:pk>/', post_detail_api.as_view()),
    path('api_list/',post_list_api.as_view()),
]
