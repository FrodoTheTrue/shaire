from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),
    url(r'^(?P<user_id>.+)/(?P<type_message>.+)/$', 'alerts.views.send_invite'),
    url(r'^my_invites/$', 'alerts.views.check_invites'),
)

