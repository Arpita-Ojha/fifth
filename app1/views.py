from django.shortcuts import render

# Create your views here.

def kim(request):

    dict={'name':'Kimtaehyung'}

    return render(request,'kim.html',context=dict)
