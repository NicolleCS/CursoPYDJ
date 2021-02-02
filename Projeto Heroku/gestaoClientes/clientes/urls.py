from django.urls import path
from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', persons_list, name='person_list'),
    path('new/', persons_new, name='person_new'),
    path('update/<int:id>', persons_update, name='person_update'),
    path('delete/<int:id>', persons_delete, name='person_delete')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
