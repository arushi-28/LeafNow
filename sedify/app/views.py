from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# from .decorators import unauthenticated_user
from .forms import CreateUserForm ,donationForm
from django.db import connection
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import donation
from django.urls import reverse
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



# Create your views here.

def index(request):
    
    if request.method=='POST':
        form=donationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("succesfully donated")
                return redirect('/charge')
            except:
                pass
    else:
        form=donationForm()
    return render(request, 'index.html',{'form':form})


def charge(request):


	if request.method == 'POST':
		print('Data:', request.POST)

		amount = int(request.POST['amount'])

		

	return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'success.html', {'amount':amount})
# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')
def registerPage(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            
            
            
            messages.success(request,'Account was created for '+username)
            return redirect('login')
    
    context={'form':form}
    return render(request,"register_user.html",context)

# @unauthenticated_user
def loginPage(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.info(request,'Username or Password incorrect!!')
    context={}
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    return redirect("login")
@login_required(login_url='login')
def donate(request):
    return render(request,'index.html')
@login_required(login_url='login')
def about(request):
    return render(request,'about.html')


def render_pdf_view(request):
  
    template_path = 'pdf.html'

    context={}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def sell(request):
    return render(request,'se.html')
def sell1(request):
    return render(request,'sell.html')