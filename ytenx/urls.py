# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = patterns('',
  url(r'^kyonh/', include('ytenx.kyonh.urls'), {'vertical': 0}),
  url(r'^tcyts/', include('ytenx.tcenghyonhtsen.urls'), {'vertical': 0}),
  url(r'^pyonh/', include('ytenx.pyonh.urls'), {'vertical': 0}),
  url(r'^trngyan/', include('ytenx.trngyan.urls'), {'vertical': 0}),
  url(r'^dciangx/', include('ytenx.dciangxkox.urls'), {'vertical': 0}),
  url(r'^byohlyuk/', include('ytenx.byohlyuk.urls')),
  url(r'^$', 'ytenx.views.index_page', {'vertical': 0}),
  url(r'^about$', 'ytenx.views.about_page', {'vertical': 0}),
  url(r'^zim$', 'ytenx.views.zim', {'vertical': 0}),
  url(r'^sriek$', 'ytenx.views.kiemx_sriek', {'vertical': 0}),
  url(r'^v/kyonh/', include('ytenx.kyonh.urls'), {'vertical': 1}),
  url(r'^v/tcyts/', include('ytenx.tcenghyonhtsen.urls'), {'vertical': 1}),
  url(r'^v/pyonh/', include('ytenx.pyonh.urls'), {'vertical': 1}),
  url(r'^v/trngyan/', include('ytenx.trngyan.urls'), {'vertical': 1}),
  url(r'^v/dciangx/', include('ytenx.dciangxkox.urls'), {'vertical': 1}),
  url(r'^v/byohlyuk/', include('ytenx.byohlyuk.urls'), {'vertical': 1}),
  url(r'^v$', 'ytenx.views.index_page', {'vertical': 1}),
  # url(r'^v/about$', 'ytenx.views.about_page', {'vertical': 1}),
  url(r'^v/zim$', 'ytenx.views.zim', {'vertical': 1}),
  url(r'^v/sriek$', 'ytenx.views.kiemx_sriek', {'vertical': 1}),
)

urlpatterns += staticfiles_urlpatterns()
