from django.conf.urls import patterns, include, url
<<<<<<< HEAD
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
=======

>>>>>>> origin/master
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.home', name='home'),
    url(r'^contato/$', 'core.views.contato', name='contato'),
<<<<<<< HEAD
    url(r'^delete/(?P<id>\d+)/$', 'core.views.delete_task', name='delete_task'),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
=======
    #url(r'^$', 'core.views.tasks', name='tasks'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
>>>>>>> origin/master
