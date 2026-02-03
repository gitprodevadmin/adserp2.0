from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from root.applist import CREATED_APPS
from django.conf.urls import handler404, handler500, handler403

handler404 = 'commonapp.views.error_404'
handler500 = 'commonapp.views.error_500'
handler403 = 'commonapp.views.error_403'

urlpatterns = [
    path('admin/', admin.site.urls),
] + [path(f'{app}/', include(f'{app}.urls')) for app in CREATED_APPS]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)