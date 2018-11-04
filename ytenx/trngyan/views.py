# coding=utf-8
from django.http import Http404
from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page
from django.db.models import Q
from ytenx.helpers.paginator import Paginator
from django.core.paginator import InvalidPage, EmptyPage
from models import *

def triung_ngyan_qim_yonh(request, vertical=0):
  return render_to_response('trngyan/triung_ngyan_qim_yonh.html', {
    'cjeng_mux_pieux': CjengLyih.objects.all(),
    'yonh_mux_pieux': YonhBox.objects.all(),
    'vertical': vertical,
  })

def sieux_yonh(request, ziox, vertical=0):
  try:
    sieux_yonh = SieuxYonh.objects.get(ziox = ziox)
  except:
    raise Http404()

  return render_to_response('trngyan/sieux_yonh.html', {
    'sieux_yonh': sieux_yonh,
    'vertical': vertical,
  })

def sieux_yonh_pieux(request, vertical=0):
  cjeng = request.GET.get('cjeng')
  yonh = request.GET.get('yonh')
  ho = request.GET.get('ho')
  deuh = request.GET.get('deuh')
  
  query = Q()
  if cjeng:
    query &= Q(cjeng = CjengMux.objects.get(dzih = cjeng))
  if yonh:
    query &= Q(yonh_box = YonhBox.objects.get(mjeng = yonh))
  if deuh:
    query &= Q(deuh = deuh)
  if ho:
    query &= Q(ho = ho)
  
  sieux_yonh_pieux = SieuxYonh.objects.filter(query).order_by('ziox')
  paginator = Paginator(sieux_yonh_pieux, 15)
  try:
    sieux_yonh_pieux = paginator.page(request.GET)
  except (EmptyPage, InvalidPage):
    raise Http404()
  
  sieux_yonh_pieux.cjeng = cjeng
  sieux_yonh_pieux.yonh = yonh
  sieux_yonh_pieux.deuh = deuh
  sieux_yonh_pieux.ho = ho
  
  cjeng_pieux = []
  for lyih in CjengLyih.objects.all():
    cjeng_pieux.append(lyih)
    cjeng_pieux += lyih.cjengmux_set.all()
  
  yonh_pieux = YonhBox.objects.all()
  
  return render_to_response('trngyan/sieux_yonh_pieux.html', {
    'sieux_yonh_pieux': sieux_yonh_pieux,
    'cjeng_pieux': cjeng_pieux,
    'yonh_pieux': yonh_pieux,
    'vertical': vertical,
  })

def dzih(request, id, vertical=0):
  try:
    dzih = Dzih.objects.get(id=id)
  except:
    raise Http404()

  return render_to_response('trngyan/dzih.html', {
    'dzih': dzih,
    'vertical': vertical,
  })

def dzih_pieux(request):
  dzih_pieux = Dzih.objects.all()
  paginator = Paginator(dzih_pieux, 15)
  try:
    dzih_pieux = paginator.page(request.GET)
  except (EmptyPage, InvalidPage):
    raise Http404()
  return render_to_response('trngyan/dzih_pieux.html', {
    'dzih_pieux': dzih_pieux,
    'vertical': vertical,
  })

@cache_page(60 * 60 * 24)
def cjeng_mux_pieux(request, vertical=0):
  return render_to_response('trngyan/cjeng_mux_pieux.html', {
    'cjeng_mux_pieux': CjengLyih.objects.all(),
    'vertical': vertical,
  })

@cache_page(60 * 60 * 24)
def cjeng_mux(request, dzih, vertical=0):
  try:
    cjeng = CjengMux.objects.get(dzih = dzih)
  except:
    raise Http404()

  return render_to_response('trngyan/cjeng_mux.html', {
    'cjeng': cjeng,
    'vertical': vertical,
  })

@cache_page(60 * 60 * 24)
def yonh_mux_pieux(request, vertical=0):
  return render_to_response('trngyan/yonh_mux_pieux.html', {
    'yonh_mux_pieux': YonhBox.objects.all(),
    'vertical': vertical,
  })

@cache_page(60 * 60 * 24)
def yonh_mux(request, mjeng, vertical=0):
  try:
    yonh = YonhMux.objects.get(mjeng = mjeng)
  except:
    raise Http404()

  return render_to_response('trngyan/yonh_mux.html', {
    'yonh': yonh,
    'vertical': vertical,
  })

def cio(request, kyenh, jep, vertical=0):
  cio = Cio.objects.get(
    kyenh = kyenh,
    jep = jep,
  )
  
  return render_to_response('trngyan/cio.html', {
    'cio': cio,
    'vertical': vertical,
  })
