from django.shortcuts import render,loader
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from . import models
import datetime

# Create your views here.

@login_required(login_url='/master/login/')
def index(request):
    return HttpResponseRedirect('/master/dashboard/')

def login_view(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)
        if user is None:
            msg = "Invalid Login Details"
            try:
                ac = get_user_model()
                ac = ac.objects.get(username=username)
                if ac.is_active is False:
                    msg = "Account Not Active"
            except:
                msg = "No User Account Found"
        else:
            if user.is_active is True:
                login(request, user)
                return HttpResponseRedirect('/master/dashboard/')
            else:
                msg = "User account Not Active"

    template = loader.get_template('master/login.html')
    return HttpResponse(template.render({'msg':msg},request))

@login_required(login_url="/master/login/")
def dashboard(request):
    msg = ''
    questions = models.Question.objects.all().count()
    users = models.Participant.objects.all()
    diff = datetime.datetime.today() - datetime.timedelta(days=30)
    difft = datetime.datetime.today() - datetime.timedelta(days=7)
    difftt = datetime.datetime.today() - datetime.timedelta(days=1)
    usersmnth = users.filter(created_at__gte=diff).count()
    usersweek = users.filter(created_at__gte=difft).count()
    userstoday = users.filter(created_at__gte=difftt).count()
    sursus = users.filter(is_completed=True).count()
    surfa = users.filter(is_completed=False).count()
    template = loader.get_template('master/dashboard.html')
    return HttpResponse(template.render({'msg':msg,'mainp': 'dashboard','questions':questions,
    'usersmnth':usersmnth,'usersweek':usersweek,'userstoday':userstoday,
    'sursus':sursus,'surfa':surfa},request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/master/login/')

@login_required(login_url="/master/login/")
def questions(request):
    msg = ''
    if request.method == "POST" and 'ftitle' in request.POST:
        ftitle = request.POST.get('ftitle')
        fle = request.FILES['fle']
        f = models.Question()
        f.file_name = ftitle
        f.file = fle
        f.save()
        msg = "sucadd"
    if request.method == 'POST' and 'deleteid' in request.POST:
        try:
            models.Question.objects.get(id=request.POST.get('deleteid')).delete()
            msg = "sucdlt"
        except:
            msg = "not_dlt"
    files = models.Question.objects.all()
    template = loader.get_template('master/files.html')
    return HttpResponse(template.render({'msg':msg,'files':files,'page':'files'},request))



@login_required(login_url="/master/login/")
def participants(request):
    msg = ''
    files = models.Participant.objects.all()
    template = loader.get_template('master/participants.html')
    return HttpResponse(template.render({'msg':msg,'files':files,'page':'parti'},request))


@login_required(login_url="/master/login/")
def participant(request,id):
    msg = ''
    participant = models.Participant.objects.get(id=id)
    survey = models.Result.objects.filter(participant_id=id)
    data = {}
    for i in survey:
        if str(i.question_id) in data:
            data[str(i.question_id)]['ans'] = data[str(i.question_id)]['ans'] + [str(i.answer.choice),]
        else:
             data[str(i.question_id)] = {"question":i.question.title,"ans":[str(i.answer.choice),]}
    template = loader.get_template('master/participant.html')
    return HttpResponse(template.render({'msg':msg,'participant':participant,'survey':survey,'page':'parti','data':data},request))