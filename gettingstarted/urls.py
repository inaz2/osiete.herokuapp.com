from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^popular', hello.views.popular, name='popular'),
    url(r'^latest', hello.views.latest, name='latest'),
    url(r'^ask', hello.views.ask, name='ask'),
    url(r'^topic/(\d+)', hello.views.topic, name='topic'),
    url(r'^answer/(\d+)', hello.views.answer, name='answer'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
