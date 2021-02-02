from django.urls import path
from .views import home, mylogout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('logout/', mylogout, name='mylogout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
