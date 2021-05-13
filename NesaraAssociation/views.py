from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import member
from .models import meeting
from .filters import memberfilter
from .forms import memberForm, CreateUserForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account successfully created!!')

            
            return redirect('login')

    context = {'form':form}
    return render(request,'user/register.html',context )
    

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method == 'GET':
            return render(request,'user/login.html',{'form':AuthenticationForm()})
        else:
            user=authenticate(request, username=request.POST['username'],password=request.POST['password'])
            if user is None:
                return render(request,'user/login.html',{'form':AuthenticationForm(),'error':'username OR password is incorrect'})
            
            else:
                login(request, user)
                return redirect('home')

def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request,'user/home.html')
  
@login_required(login_url='login')
def member_details(request):
    NesaraAssociation = member.objects
    myfilter = memberfilter(request.GET,queryset=NesaraAssociation)
    NesaraAssociation = myfilter.qs
    context={'NesaraAssociation':NesaraAssociation,'myfilter':myfilter}
    return render(request,'user/member_details.html',context)

@login_required(login_url='login')
def addmember(request):
    member1=member()
    if request.method == 'POST':
        if request.POST.get('member_id') and request.POST.get('member_name') and request.POST.get('address') and request.POST.get('phone_no') and request.POST.get('site_no'):
            member1.member_id=request.POST.get('member_id')
            member1.member_name=request.POST.get('member_name')
            member1.address=request.POST.get('address')
            member1.phone_no=request.POST.get('phone_no')
            member1.site_no=request.POST.get('site_no')
            member1.save()
            messages.success(request,'Record Saved Successfully...!')

    return render(request,'user/addmember.html',{'member':member1})