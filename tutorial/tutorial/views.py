from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def login_redirect(request):
    return redirect('account/login')
