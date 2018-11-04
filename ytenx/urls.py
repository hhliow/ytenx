# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = patterns('',
  url(r'^kyonh/', include('ytenx.kyonh.urls')),
  url(r'^tcyts/', include('ytenx.tcenghyonhtsen.urls')),
  url(r'^pyonh/', include('ytenx.pyonh.urls')),
  url(r'^trngyan/', include('ytenx.trngyan.urls')),
  url(r'^dciangx/', include('ytenx.dciangxkox.urls')),
  url(r'^byohlyuk/', include('ytenx.byohlyuk.urls')),
  url(r'^$', 'ytenx.views.index_page'),
  url(r'^about$', 'ytenx.views.about_page'),
  url(r'^zim$', 'ytenx.views.zim'),
  url(r'^sriek$', 'ytenx.views.kiemx_sriek'),
  url(r'^<int:vertical>/kyonh/', include('ytenx.kyonh.urls')),
  url(r'^<int:vertical>/tcyts/', include('ytenx.tcenghyonhtsen.urls')),
  url(r'^<int:vertical>/pyonh/', include('ytenx.pyonh.urls')),
  url(r'^<int:vertical>/trngyan/', include('ytenx.trngyan.urls')),
  url(r'^<int:vertical>/dciangx/', include('ytenx.dciangxkox.urls')),
  url(r'^<int:vertical>/byohlyuk/', include('ytenx.byohlyuk.urls')),
  url(r'^<int:vertical>/$', 'ytenx.views.index_page'),
  url(r'^<int:vertical>/about$', 'ytenx.views.about_page'),
  url(r'^<int:vertical>/zim$', 'ytenx.views.zim'),
  url(r'^<int:vertical>/sriek$', 'ytenx.views.kiemx_sriek'),
)

urlpatterns += staticfiles_urlpatterns()
