from django.shortcuts import render,HttpResponse
from home.models import task

# Create your views here.
def home(request):
    # render(request,'index.html',context = {'success' : True})
    if request.method == 'POST':
        name = request.POST['name'],
        discription=request.POST['discription']
        # print(name,discription)
        ins = task(name=name,discription=discription)
        ins.save()                                                           
        return render(request,'index.html',context = {'success' : True})
    return render(request,'index.html')
def about(request):
    t = task.objects.all()
    return render(request, 'about.html', context={"t":t})
    # alltask=task.objects.all()
    # for i in alltask:
        # print(i.discription)
    # dict = {"tasks": alltask}
    # print(dict)
    return render(request,'about.html')