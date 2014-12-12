from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),
    #url(r'^captcha/', include('captcha.urls')),
    url(r'^confirm_email/(?P<user_key>\S+)/$', 'loginsys.views.confirm_email'),
    url(r'^login/$', 'loginsys.views.login'),
    url(r'^logout/$', 'loginsys.views.logout'),
    url(r'^register/$', 'loginsys.views.register'),
    url(r'^$', 'loginsys.views.main'),
)
