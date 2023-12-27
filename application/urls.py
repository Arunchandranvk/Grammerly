"""
URL configuration for scanner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from application import views
app_name="application"

urlpatterns = [
    path('',views.base,name='base'),
    path('image/',views.image_upload,name='imageupload'),
    path('pdf/',views.pdf_upload,name='pdfupload'),
    path('text/',views.text_upload,name='textupload'),
    path('imageextract/',views.imageextract,name='imageextract'),
    path('pdfextract/',views.pdf_extract,name='pdfextract'),
    path('getdata/',views.getdata,name='getdata'),
    path('translate/',views.translation,name='translate'),
    path('gettext/',views.get_text,name='gettext'),
    path('texttranslate',views.text_translation,name='texttranslate')

]





