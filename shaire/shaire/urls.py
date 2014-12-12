from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shaire.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^3_14157_2_71828_adminka_anti_brute/', include(admin.site.urls)),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^profile/', include('user_profile.urls')),
    url(r'^invites/', include('alerts.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^im/', include('chat.urls')),
    url(r'^$', include('loginsys.urls')),
)
