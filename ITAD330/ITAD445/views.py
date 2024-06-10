from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

#class MapView(View):
#    template_name = "project_content/map.html"

#    def get(self,request):
#        context = {

#        }

#        return render(request, self.template_name, context)

def index(request):
    {{ value|json_script:"hello-data" }}
    return render(request, "index.html")

#class IndexView(TemplateView):
#    template_name = "index.html"