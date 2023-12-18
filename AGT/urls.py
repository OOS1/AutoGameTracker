from django.urls import path 
from . import views 
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"), 
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # Include media files route as well
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)