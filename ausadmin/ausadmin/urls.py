"""ausadmin URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from adminside import views as adminside_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', adminside_views.signupform),
    url(r'ad/', adminside_views.signupform),
    url(r'.*addcat.html/$', adminside_views.addcat),
    url(r'.*viewcat.html/$', adminside_views.viewcat),
    url(r'.*additem.html/$', adminside_views.additem),
    url(r'.*viewitem.html/$', adminside_views.viewitem),
    url(r'.*viewuser.html/$', adminside_views.viewuser),
    url(r'.*viewsuggs.html/$', adminside_views.viewsuggs),
    url(r'.*delete/(?P<part_id>[0-9]+)/$',adminside_views.delfunction,name= 'delid'),
    url(r'.*deletee/(?P<part_id>[0-9]+)/$',adminside_views.delitem,name= 'delitem'),
    url(r'.*deleteuser/(?P<part_id>[0-9]+)/$',adminside_views.deluser,name= 'deluser'),
    
   
]

#^ begining $ end string ' a must be start of. any char *anynumber fotimes

