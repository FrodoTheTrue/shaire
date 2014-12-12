from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),
    url(r'^change_name/$', 'user_profile.views.change_name'),
    url(r'^change_secondname/$', 'user_profile.views.change_secondname'),
    url(r'^change_sex/$', 'user_profile.views.change_sex'),
    url(r'^change_city/$', 'user_profile.views.change_city'),
    url(r'^change_vk/$', 'user_profile.views.change_vk'),
    url(r'^change_birthday/$', 'user_profile.views.change_birthday'),
    url(r'^settings/$', 'user_profile.views.settings'),
    url(r'^change_avatar/$', 'user_profile.views.change_avatar'),
    url(r'^(?P<username>.+)/$', 'user_profile.views.profile'),
)
