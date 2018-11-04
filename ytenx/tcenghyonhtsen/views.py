# coding=utf-8
from django.http import Http404
from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page
from ytenx.helpers.paginator import Paginator
from django.core.paginator import InvalidPage, EmptyPage
from models import SieuxYonh, YonhBux, YonhMiuk, Cio

def index_page(request, vertical=0):
  return render_to_response('tcenghyonhtsen/index.html', {
    'vertical': vertical,
  })

def sieux_yonh_page(request, ziox, vertical=0):
  try:
    sieux_yonh = SieuxYonh.objects.get(ziox=ziox)
  except:
    raise Http404()

  return render_to_response('tcenghyonhtsen/sieux_yonh.html', {
    'sieux_yonh': sieux_yonh,
    'vertical': vertical,
  })

def sieux_yonh_list_page(request, vertical=0):
  sieux_yonh_list = SieuxYonh.objects.all()
  paginator = Paginator(sieux_yonh_list, 15)
  try:
    sieux_yonh_list = paginator.page(request.GET)
  except (EmptyPage, InvalidPage):
    raise Http404()
  return render_to_response('tcenghyonhtsen/sieux_yonh_list.html', {
    'sieux_yonh_list': sieux_yonh_list,
    'vertical': vertical,
  })

@cache_page(60 * 60 * 24)
def yonh_miuk_list_page(request, vertical=0):
  return render_to_response('tcenghyonhtsen/yonh_miuk_list.html', {
    'yonh_bux_list': YonhBux.objects.all(),
    'vertical': vertical,
  })

def yonh_miuk_page(request, mjeng, vertical=0):
  yonh_miuk = YonhMiuk.objects.get(dzih = mjeng)

  return render_to_response('tcenghyonhtsen/yonh_miuk.html', {
    'yonh_miuk': yonh_miuk,
    'vertical': vertical,
  })

def cio_page(request, kyenh, jep, vertical=0):
  cio = Cio.objects.get(
    kyenh = kyenh,
    jep = jep,
  )
  
  return render_to_response('tcenghyonhtsen/cio.html', {
    'cio': cio,
    'vertical': vertical,
  })
