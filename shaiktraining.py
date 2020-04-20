from django.http import HttpResponse
from django.shortcuts import render
import operator
def ram(request):
    return render(request,"countwords.html")
def aboutus(request):
    return render(request,"aboutus.html")
def count(request):
    mess=request.GET["message"]
    wl=mess.split()
    #print(wl
    wlcount={}
    for word in wl:
        if word in wlcount:
            wlcount[word] += 1
        else:wlcount[word]=1
    sort1=sorted(wlcount.items(),key=operator.itemgetter(1),reverse=True)





    return render(request,"count.html",{"msg":mess,"length":len(wl),"abc":wlcount,'cba':sort1})




#def ram(request):
    #return render(request,"ram.html",{"shaik":"8179726957"})
#def ram(request):
    #return HttpResponse("hai shaik baba vali")

#def wel(request):
    #return HttpResponse("<h1> I LOVE MY MAM AND DADDY</h1>")
