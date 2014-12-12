from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment')
    url(r'^check_new/$', 'chat.views.check_new'),
    url(r'^send_message/$', 'chat.views.send_message'),
    url(r'^(?P<user_to>.+)/$', 'chat.views.show_dialog'),
    #url(r'^show_messages/$', 'chat.views.show_messages'),
    url(r'^$', 'chat.views.chat_list'),
)