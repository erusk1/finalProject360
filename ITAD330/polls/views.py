from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import JsonResponse
import json
import requests

# Create your views here.

#class MapView(View):
#    template_name = "project_content/map.html"

#    def get(self,request):
#        context = {

#        }

#        return render(request, self.template_name, context)

def index(request):
    #locations = []
    #data = {'lat':9.3418808}
    #lat={'lat':9.3418808}
    #locations.append(data)
    #lat = response.json()
    #context = {"locations": locations}
    def getList():
        url = "https://data.mongodb-api.com/app/data-mavhj/endpoint/data/v1/action/find"
        payload = json.dumps({
            "collection": "shipwrecks",
            "database": "sample_geospatial",
            "dataSource": "ServerlessInstance0",
        })
        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'kQ8GUFCMl0zw1BJrBWYtZjz6Ioxd6Ye1Q2ao5kQ0RFAbNg4EG2AIkqdZVbS9kUFE',
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print("Hello")
        #print(response)
        parsed_payload = json.loads(response.text)
        #print(parsed_payload)
        #lat1 = {}
        
        # for x in parsed_payload:             
        #     lat1['lat{}'.format(x)] = parsed_payload[x]['latdec'] 
        #     lat1['lon{}'.format(x)] = parsed_payload[x]['londec']
        # for x in parsed_payload_f:
        #     record(x) = parsed_payload_f[x]
        #         parsed_payload_f = parsed_payload['documents'][:5]
        #         #print(parsed_payload_f)
        #         record1=parsed_payload_f[0]
        #         record2=parsed_payload_f[1]
        #         record3=parsed_payload_f[2]
        #         record4=parsed_payload_f[3]
        #         record5=parsed_payload_f[4]
        # lat1={'lat1':record1['latdec'], 'lon1':record1['londec'],
        #         'lat2':record2['latdec'], 'lon2':record2['londec'],
        #         'lat3':record3['latdec'], 'lon3':record3['londec'],
        #         'lat4':record4['latdec'], 'lon4':record4['londec'],
        #         'lat5':record5['latdec'], 'lon5':record5['londec']}
    #lon1={'lon1':parsed_payload['document']['londec']}
    
     #   print(lat1)
    #print(lon1)
    #return render(request, "index.html", lat1)
    
    #return JsonResponse({'lat' : lat})


#class IndexView(TemplateView):
#    template_name = "index.html"

