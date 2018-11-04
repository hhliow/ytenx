# coding=utf-8
from django.conf.urls import patterns

urlpatterns = patterns('',
  (r'^$', 'ytenx.trngyan.views.triung_ngyan_qim_yonh'),
  (r'^sieux/$', 'ytenx.trngyan.views.sieux_yonh_pieux'),
  (r'^sieux/(?P<ziox>\d{1,4})/$', 'ytenx.trngyan.views.sieux_yonh'),
  (r'^dzih/$', 'ytenx.trngyan.views.dzih_pieux'),
  (r'^dzih/(?P<ziox>.+)/$', 'ytenx.trngyan.views.dzih'),
  (r'^cjeng/$', 'ytenx.trngyan.views.cjeng_mux_pieux'),
  (r'^cjeng/(?P<ziox>.+)/$', 'ytenx.trngyan.views.cjeng_mux'),
  (r'^yonh/$', 'ytenx.trngyan.views.yonh_mux_pieux'),
  (r'^yonh/(?P<ziox>.+)/$', 'ytenx.trngyan.views.yonh_mux'),
  (r'^cio/(?P<ziox>\d{1,1})/(?P<ziox2>\d{1,3})/$', 'ytenx.trngyan.views.cio'),
)
