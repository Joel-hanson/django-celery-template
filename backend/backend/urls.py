from common import urls as common_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("common/", include(common_urls), name="common"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
