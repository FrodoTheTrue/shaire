from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shaire.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^username=(?P<username>.+)\%firstname=(?P<firstname>.+)\%(?P<secondname>.+)\%(?P<gender>.+)/$', 'search.views.show_result'),
    url(r'^$', 'search.views.search'),
)