from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from Picture.models import FileUploaded
import json



# Create your views here.
  
#@csrf_exempt
class HandleData(View):
  
  def post(self, request, *args, **kwargs):
    #import pdb; pdb.set_trace()
    f = request.FILES['files[]']

    # writing to model
    thefile = FileUploaded(title = str(f.name), upFile=f, ct=str(f.content_type))
    
    
    name = thefile.upFile.name
    size = thefile.upFile.size
    # for some reason, url = thefile.upFile.url was not giving correct url
    # getting url for photo deletion
    file_delete_url = '/Picture/delete/'
  
    thefile.save() 
    
    
    # formatting JSON response
    res = {
      "files": [
        {
          "name": name,
          "size": size,
          "url": thefile.upFile.url,
          "deleteType": "POST",
          "thumbnailUrl": thefile.upFile.url,
          "deleteUrl": file_delete_url+str(thefile.pk)+'/',
        }
      ]
    }  
    return HttpResponse(json.dumps(res), content_type='application/json')
    
  
#@csrf_exempt   
class Delete(View):
  
  @method_decorator(csrf_exempt)
  def dispatch(self, *args, **kwargs):
    return super(Delete, self).dispatch(*args, **kwargs)
  
  def post(self, request, *arg, **kwargs): 
    
    picKey = kwargs.pop('pictureKey')
    #import pdb; pdb.set_trace()
    #print "picture key is " + str(pickey)
    image = get_object_or_404(FileUploaded, pk=picKey)
    
  
    res = {
      "files": [
        {
          image.title: True
        }
      ]
    } 
    #print res
    image.delete()
    
    return HttpResponse(json.dumps(res), content_type='application/json')
    

# using one view for both list and thumbnail urls, just changing the template_name in urls.py
class List(ListView):
  
  model = FileUploaded
  

    

