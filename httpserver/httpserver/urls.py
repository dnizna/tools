from django.conf.urls import patterns, include, url
from httpserver.view import show_index, file_download, file_upload

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ('^index/$', show_index),
    ('^filedownload/$', file_download),
    ('^fileupload/$', file_upload),
    # Examples:
    # url(r'^$', 'httpserver.views.home', name='home'),
    # url(r'^httpserver/', include('httpserver.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
