from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import current_datetime
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AGWebSite.views.home', name='home'),
    # url(r'^AGWebSite/', include('AGWebSite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', current_datetime),
)
