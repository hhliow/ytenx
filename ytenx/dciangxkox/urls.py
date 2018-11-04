# coding=utf-8
from django.conf.urls import patterns

urlpatterns = patterns('',
  (r'^$', 'ytenx.dciangxkox.views.dciangx_kox'),
  (r'^dzih/$', 'ytenx.dciangxkox.views.dzih_pieux'),
  (r'^dzih/(?P<id>.+)/$', 'ytenx.dciangxkox.views.dzih'),
  (r'^cjeng/$', 'ytenx.dciangxkox.views.cjeng_byo_pieux'),
  (r'^cjeng/(?P<mjeng>.+)/$', 'ytenx.dciangxkox.views.cjeng_byo'),
  (r'^yonh/$', 'ytenx.dciangxkox.views.yonh_box_pieux'),
  (r'^yonh/(?P<mjeng>.+)/$', 'ytenx.dciangxkox.views.yonh_box'),
)
