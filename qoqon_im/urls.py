from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.static import serve

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('favicon.ico', serve, {'path': 'favicon.ico', 'document_root': settings.BASE_DIR / 'static'}),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('news/', include('news.urls')),
    path('staff/', include('staff.urls')),
    path('gallery/', include('gallery.urls')),
    path('achievements/', include('achievements.urls')),
    path('contact/', include('contact.urls')),
    path('faq/', include('faq.urls')),
    prefix_default_language=True,
)

handler404 = 'core.views.handler404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



