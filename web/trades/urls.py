from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('trades.apps.main.urls')),
    path(r'todo/', include('trades.apps.todo.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)