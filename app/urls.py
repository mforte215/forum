from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("articles", views.articleListView, name='articles'),
    path("article/<slug:slug>", views.articleDetail, name='article_detail'),
    path("experience", views.experienceView, name="experience"),
    path("contact", views.contactView, name='contact')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
