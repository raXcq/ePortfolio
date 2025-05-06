from django.urls import path
from .views import home, about, resume, portfolio, services, contact


urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("resume/", resume, name="resume"),
    path("portfolio/", portfolio, name="portfolio"),
    path("services/", services, name="services"),
    path("contact/", contact, name="contact"),
]
