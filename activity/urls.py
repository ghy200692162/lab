from django.conf.urls.defaults import * 

ACTIVITY_URL=r'(?P<slug>[-\w]+)/'

urlpatterns = patterns('activity.views',
        url(r'^create/$',                       'activity_create',     name='activity_create'),
        url(r'^activity_list/$',                'activity_list',       name='activity_list'),
        url(r'^%sdetail$' % ACTIVITY_URL,       'activity_detail',      name='activity_detail'),
        )
