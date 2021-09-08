from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from . models import *
# Create your views here.
def firstpg(request):
    return render(request, 'firstpg.html')
def alogin(request):
    if request.method=='POST':
        try:
            auname=request.POST['auname']
            apass=request.POST['apassword']
            admin=Alogin.objects.get(ausername=auname, apassword=apass)
            request.session['aid']=admin.id
            return redirect('admin')
        except:
            return render(request, 'alogin.html', {'msg':'Invalid Credentials'})    
    return render(request, 'alogin.html')    
def login(request):
    if request.method=='POST':
        try:
            uname=request.POST['uname']
            password=request.POST['password']
            logininfo=Login.objects.get(username=uname, password=password, status='active')
            request.session['id']=logininfo.id
            return redirect('homepage')
        except:
            return render(request, 'login.html', {'msg':'Invalid Userdetails'})    
    return render(request, 'login.html')
def cracc(request):
    if request.method=='POST':
        try:
            sname=request.POST['name']
            scontact=request.POST['contact']
            semail=request.POST['email']
            suname=request.POST['uname']
            spassword=request.POST['password']
            check_username_exist=Login.objects.filter(username=suname).exists() 
            if not check_username_exist:
                logindata=Login(username=suname, password=spassword)
                logindata.save()
                request.session['id']=logindata.id
                stud_data=Studentreg(name=sname, contact=scontact, email=semail, loginid=logindata, status='active')
                stud_data.save()
                return redirect('homepage')
            else:
                return render(request, 'crtacc.html', {'msg':'Username already exists, Please sign in again'})     
        except Exception as error:
            return render(request, 'crtacc.html', {'msg':error})    
    return render(request, 'crtacc.html')  
def cracc2(request):
    usrname=request.GET['uname']
    ucheck=Login.objects.filter(username=usrname).exists() 
    print(ucheck)
    if ucheck:
        return JsonResponse({
            'msg':True
         })
    else:
        return JsonResponse({
            'msg':False
        })        
def admin(request):
    adminid=request.session['aid']
    admdata=Alogin.objects.get(id=adminid)
    return render(request, 'admin.html',{'admin':admdata})    
def active(request):
    logdetails=Login.objects.filter(status='active') 
    activestud=Studentreg.objects.filter(status="active")
    return render(request, 'active.html',{'active':activestud, 'logactive':logdetails}) 
def inactivate(request,inactiveid):
    uplogstatus=Login.objects.filter(id=inactiveid).update(status='inactive')
    updtstatus=Studentreg.objects.filter(id=inactiveid).update(status='inactive')  
    return redirect('active')     
def inactive(request):
    logdetails=Login.objects.filter(status='inactive') 
    inactivestud=Studentreg.objects.filter(status="inactive")
    return render(request, 'inactive.html', {'inactive':inactivestud}) 
def activate(request,activeid):
    uplogstatus=Login.objects.filter(id=activeid).update(status='active')
    updtstatus=Studentreg.objects.filter(id=activeid).update(status='active')  
    return redirect('inactive')  
def homepage(request):
    logindetails=request.session['id']
    studlogin=Login.objects.get(id=logindetails)
    studdetails=Studentreg.objects.get(loginid=logindetails)
    return render(request, 'homepage.html',{'stud':studdetails, 'logdata':studlogin})  
def updateprofile(request):
    logindetails=request.session['id']
    if request.method=='POST':
        try:
            updname=request.POST['ename']
            updcntct=request.POST['ecntct']
            updemail=request.POST['eemail']
            upduname=request.POST['euname']
            updpass=request.POST['epass']
            Login.objects.filter(id=logindetails).update(username=upduname, password=updpass)
            Studentreg.objects.filter(loginid=logindetails).update(name=updname, contact=updcntct, email=updemail)
            studlogin=Login.objects.get(id=logindetails)
            studdetails=Studentreg.objects.get(loginid=logindetails)
            return render(request, 'homepage.html',{'stud':studdetails, 'logdata':studlogin})
        except Exception as error:  
            return render(request, 'homepage.html', {'msg':error})  
    else:
        studlogin=Login.objects.get(id=logindetails)
        studdetails=Studentreg.objects.get(loginid=logindetails)
        return render(request, 'homepage.html',{'stud':studdetails, 'logdata':studlogin}) 
def signout(request):
    del request.session['id']
    return redirect('firstpg')
def asignout(request):
    del request.session['aid']  
    return redirect('firstpg')
        
              