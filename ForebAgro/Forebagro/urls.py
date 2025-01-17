"""Forebagro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
                url(r"^$", views.HomePage.as_view(), name="home"),
                url(r"^about-us/$", views.AboutPage.as_view(), name="about"),
                url(r"^contact-us/$", views.ContactPage, name="contact"),
                url(r"^app/", include('accounts.urls', namespace="accounts")),
                url(r"^admin/", admin.site.urls),
                url(r"^accounts/", include("django.contrib.auth.urls")),
                url(r'^clientele/', include("clientele.urls", namespace="clientele")),
                url(r'^contact/', include("contact.urls", namespace="contact")),
                url(r'^transactions/', include("transactions.urls", namespace="transactions")),
                url(r'^products/', include("products.urls", namespace="products")),
                url(r'^constants/', include("constant.urls", namespace="constants")),
]
