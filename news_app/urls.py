
from django.urls import path, include
from .views import HomePageView, JahonPageView, UzbPageView, news_list, SportPageView, FanPageView, ContactView, \
    news_detail, NewsCreateView, NewsUpdateView, NewsDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('news/', news_list, name="news_all"),
    # path('news/<int:id>/', news_detail, name="news_detail_page"),
    path('news/<slug:news>/', news_detail, name="news_detail_page"),
    path('uzbekistan/', UzbPageView.as_view(template_name='news/uzb.html'), name="uzbekistan"),
    path('jahon/', JahonPageView.as_view(template_name='news/jahon.html'), name="jahon"),
    path('sport/', SportPageView.as_view(template_name='news/sport.html'), name="sport"),
    path('fan-texnika/', FanPageView.as_view(template_name='news/fan-texnika.html'), name="fan-texnika"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('news/<slug>/create/', NewsCreateView.as_view(), name="news_create"),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name="news_update"),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name="news_delete"),
]