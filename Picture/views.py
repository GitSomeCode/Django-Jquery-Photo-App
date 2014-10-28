from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from Picture.models import FileUploaded
import json



# Create your views here.
def formview(request):
  return render(request, "Picture/index.html")
  
#@csrf_exempt
def handledata(request):
  
  if request.method == 'POST':
    
    f = request.FILES['files[]']

    # writing to model
    thefile = FileUploaded(title = str(f.name), upFile=f, ct=str(f.content_type))
    #import pdb; pdb.set_trace()
    
    name = thefile.upFile.name
    size = thefile.upFile.size
    # for some reason, url = thefile.upFile.url was not giving correct url
    #getting url for photo deletion
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
    
    print json.dumps(res, indent = 2)   
    
    return HttpResponse(json.dumps(res), content_type='application/json')
  else:
    res = {'error':'noJsonResponse'}
    return HttpResponse(json.dumps(res), content_type='application/json')
    
    print res
    
@csrf_exempt   
def delete(request, pk):
    
  image = get_object_or_404(FileUploaded, pk=pk)
  
  res = {
    "files": [
      {
        image.title: True
      }
    ]
  } 
  print res
  image.delete()

  return HttpResponse(json.dumps(res), content_type='application/json')
  
  
def list(request):
  images = FileUploaded.objects.all()
  return render(request, "Picture/list.html", {'images': images})
  
    

