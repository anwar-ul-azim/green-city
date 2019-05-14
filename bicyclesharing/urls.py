from . import views
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from ckeditor_uploader import views as ckviews
from django.views.decorators.cache import never_cache
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns = i18n_patterns (
    path(_('admin/'), admin.site.urls),
    path('', views.home, name='home'),
    path(_('about/'), views.about, name='about'),
    path(_('cycles/'), include('cycles.urls')),
    path(_('users/'), include('users.urls')),
    path(_('posts/'), include('posts.urls')),
    path(_('payments/'), include('payments.urls')),
    path(_('faq/'), views.faq, name='faq'),
    path('ckeditor/upload/', ckviews.upload, name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(ckviews.browse), name='ckeditor_browse'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    url(r'oauth/', include('social_django.urls', namespace='social')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    prefix_default_language= False
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)