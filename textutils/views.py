from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtxt = request.POST.get('text', 'default')

    rempunc = request.POST.get('rempunc', 'off')
    capf = request.POST.get('capf', 'off')
    remms = request.POST.get('remms', 'off')
    sentc = request.POST.get('sentc', 'off')
    lowc = request.POST.get('lowc', 'off')
    
    if(rempunc == 'on'):
        djana = ""
        for i in djtxt:
            if (i.isalnum() == True or i == ' '):
                djana = djana + i
        djtxt = djana
        
    if (capf == 'on'):
        djana = djtxt.upper()
        djtxt = djana

    if (remms == 'on'):
        djana = " ".join(djtxt.split())
        djtxt = djana

    if(sentc == 'on'):
        d1 = ""
        wrd1 = " ".join(djtxt.split())
        wrd2 = wrd1.split()
        for s in wrd2:
            d1 = d1 + " " + s[0].upper()+s[1:]

        djtxt = d1

    if(lowc == 'on'):
        djana = djtxt.lower()
        djtxt = djana

    charn=0
    for i in djtxt:
        if(i.isalnum()):
            charn+=1
    
    wrdn = len(djtxt.split())
    
    params = {'ana1' : djtxt,'ch' : charn, 'wrd' : wrdn}
    return render(request,'result.html',params)