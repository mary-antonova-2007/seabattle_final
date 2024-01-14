from django.contrib import admin
from django.urls import path, include
from authorization.urls import urlpatterns as auth_patterns
from store.urls import urlpatterns as store_patterns
from quiz.urls import urlpatterns as quiz_patterns
from .views import main
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', main, name='main'),
    path('admin/', admin.site.urls),
    path('auth/', include(auth_patterns)),
    path('store/', include(store_patterns)),
    path('quiz/', include(quiz_patterns)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)