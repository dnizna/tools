from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.conf import settings
import os
import time

def show_index(request):
  tp = get_template("index.html")
  html = tp.render(Context({}))
  return HttpResponse(html)


def file_download(request):
  basedir = settings.USER_CONFIG['FILE_DOWNLOAD_PATH']
  file_list = os.listdir(basedir)

  file_result = []
  for file_name in file_list:
    tmp = {}
    tmp['name'] = file_name 
    file_name = basedir + "/" + file_name

    tmp['size'] = os.path.getsize(file_name) / 1024
    tmp['time'] =  time.strftime("%Y-%m-%d %X",time.localtime(os.stat(file_name).st_ctime))
    tmp['isFile'] = os.path.isfile(file_name) 
    file_result.append(tmp)
    
  tp = get_template("file_download.html")
  html = tp.render(Context({ 'fileList' : file_result, "basedir" : basedir}))
  return HttpResponse(html);


def file_upload(request):
  tp = get_template("file_upload.html")
  html = tp.render(Context({}))
  return HttpResponse(html)



