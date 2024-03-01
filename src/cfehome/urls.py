from django.conf import settings
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # do not do this in prod
    from django.conf.urls.static import static
    # Try Django
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
