from django.conf.urls import patterns, include, url 
from address.views import insertbook, allbook,deleteok, update,insertauthor,allauthor,insertauthor_ok,search,find,detail
from django.contrib import admin 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings
admin.autodiscover() 
urlpatterns = patterns('', 
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_PATH}),
    url(r'^insertbook/$',insertbook),
    url(r'^allbook/$',allbook),
    url(r'^deleteok/$',deleteok),
    url(r'^update/$',update),
    url(r'^insertauthor/$',insertauthor),
    url(r'^insertauthor_ok/$',insertauthor_ok),
    url(r'^search/$',search),
    url(r'^search/search/$',find),
    url(r'^allauthor/$',allauthor),
    url(r'^detail/$',detail),
    url(r'^admin/', include(admin.site.urls)), 
)


urlpatterns += staticfiles_urlpatterns()