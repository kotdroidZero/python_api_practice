from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable':"this is sent"
    }
    return render(request,'index.html',context)
    # return HttpResponse('this is home page yes')


def about(request):
    return HttpResponse('this is about page')


def services(request):
    return HttpResponse('this is services page')


def contact(request):
    return render(request,'contact.html')