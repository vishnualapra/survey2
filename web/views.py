from django.shortcuts import render,loader
from django.http import HttpResponse
from master import models
import json
import requests
import urllib

# Create your views here.
def index(request):
    files = []
    temp ='web/login.html'
    msg = ""
    sucf = 1
    alert = ''
    url = str(request.scheme)+"://"+ request.get_host() +"/api/survey/"

    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers)
    survey_data = json.loads(response.text)
    required_count = 0
    for i in survey_data:
        if i['is_mandatory'] is True:
            required_count = required_count + 1
    if request.method == 'POST' and 'name' in request.POST:
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            try:
                user = models.Participant.objects.get(email=email)
                request.session['id'] = user.id
                request.session['name'] = user.full_name
                request.session['email'] = user.email
                if user.is_completed is True:
                    msg = "already_completed"
                    temp ='web/login.html'
                else:
                    msg = "not_completed"
                    temp = 'web/index.html'

            except:
                user = models.Participant()
                user.full_name = name
                user.email = email
                user.save()
                request.session['id'] = user.id
                request.session['name'] = user.full_name
                request.session['email'] = user.email
                msg = "started"
                temp = 'web/index.html'

        except:
            msg = "error"
            temp ='web/login.html'

    if request.method == 'POST' and 'subm' in request.POST:
        result = request.POST
        count = 0
        answers = []
        for key,value in result.items():
            if key == 'csrfmiddlewaretoken' or key == 'subm':
                pass
            else:
                answers = answers + result.getlist(key)
            if key[0] == "M":
                count = count + 1
        if count == required_count:
            for i in answers:
                chc = models.Choises.objects.get(id=i)
                url =  str(request.scheme)+"://"+ request.get_host() +"/api/result/"

                payload  = "participant="+ str(request.session['id']) +"&question=" + str(chc.question_id) + "&answer=" + str(i) 
                headers = {
                    'Content-Type': "application/x-www-form-urlencoded",
                    'cache-control': "no-cache"
                    }

                response = requests.request("POST", url, data=payload, headers=headers)
            user = models.Participant.objects.get(id=request.session['id'])
            user.is_completed = True
            user.save()
            msg = "completed"
            temp ='web/login.html'
        else:
            msg = "not_completed"
            alert = 'suc'
            temp = 'web/index.html'
    template = loader.get_template(temp)
    return HttpResponse(template.render({'msg':msg,'sucf':sucf,'survey_data':survey_data,'alert':alert},request))