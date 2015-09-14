#from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#)

from django.conf.urls import patterns, include, url
from mysite.views import hello, home_page, num_add, time_add

urlpatterns = patterns('',
    url(r'^hello/$',hello),
    url(r'^$',home_page),
    url(r'^num/add/(\d+)/$',num_add),
    url(r'^time/add/(\d{1,2})/$',time_add),
)
