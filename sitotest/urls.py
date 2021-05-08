from django.contrib import admin
from django.urls import include,path
from django.contrib.sitemaps.views import sitemap
from landing_page.sitemaps import PostSitemap
from django.conf import settings
from django.conf.urls.static import static

sitemaps = { 'posts' : PostSitemap }

urlpatterns = [
    path('adminactions/', include('adminactions.urls')),
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls','jet-dashboard')),
    path('admin/', admin.site.urls),
    path('landing_page/' ,include('landing_page.urls', namespace='landing_page')),
    path('login/' ,include('login.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('landing_page.urls')),
    path('sitemap.xml', sitemap, {'sitemaps' : sitemaps}, name='django.contrib.sitemaps.views.sitemap' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
