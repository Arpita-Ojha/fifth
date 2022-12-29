from django.shortcuts import render

# Create your views here.

def park(request):

    dict={'name':'ParkJimin'}

    return render(request,'park.html',context=dict)