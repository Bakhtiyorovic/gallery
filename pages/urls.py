from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# ViewSet routers 
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'images', ImageViewSet, basename='image')
router.register(r'contact_messages', ContactMessageViewSet, basename='contact_message')
router.register(r'timeline_categories', Timeline_categoryViewSet, basename='timeline_category')
router.register(r'about_descriptions', About_descriptionViewSet, basename='about_description')
router.register(r'about_blog_1s', About_blog_1ViewSet, basename='about_blog_1')
router.register(r'about_blog_2s', About_blog_2ViewSet, basename='about_blog_2')
router.register(r'about_tittle_1s', About_title_1ViewSet, basename='about_tittle_1')
router.register(r'about_tittle_2s', About_title_2ViewSet, basename='about_tittle_2')
router.register(r'about_tittle_3s', About_title_3ViewSet, basename='about_tittle_3')


#urls
urlpatterns = [
    path("api/", include(router.urls)),
    path("", Home, name = "home"),
    path("about/", About, name = "about"),
    path("contact/", Contact, name = "contact"),
    path('timeline/', Timeline_page, name = "timeline"),
]

