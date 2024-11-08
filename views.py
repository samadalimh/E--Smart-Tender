from django.shortcuts import render,redirect
from myapp.models import UserLogin,OtpCodeNew,AddContractors,AddTender,AddCategory,AddMaterialUsages,NewTenderProgress
import smtplib
import random

from django.core.files.storage import FileSystemStorage
from tender.settings import BASE_DIR
import os

 # Create your views here.
def index(request):
    return render(request,'index.html')

def user_home(request):
    return render(request,'user_home.html')

def admin_home(request):
    return render(request,'admin_home.html')



def AddTender(request):
    if request.method=="POST":
        location = request.POST.get('t1')
        company = request.POST.get('t2')
        tender_type = request.POST.get('t3')
        total_budget = request.POST.get('t4')
        start_date = request.POST.get('t5')
        end_date = request.POST.get('t6')
        year = request.POST.get('t7')
        AddTender.objects.filter(location=location,company=company,tender_type=tender_type,total_budget=total_budget,start_date=start_date,end_date=end_date,year=year)
        return redirect('AddTender.html')
    return render(request,'AddTender.html')


def AddCategory(request):
    return render(request,'AddCategory.html')

def AddMaterialUsages(request):

    if request.method == "POST" and request.FILES['file']:
            name = request.POST.get('t1')
            qualification= request.POST.get('t2')
            experience= request.POST.get('t3')
            address = request.POST.get('t4')
            mobile_no= request.POST.get('t5')
            email= request.POST.get('t6')
            profile_photo = request.FILES['file']
            status = request.POST.get('t7')
            fs = FileSystemStorage()
            filename = fs.save(profile_photo.name,profile_photo)
            upload_file_url = fs.url(filename)
            pat = os.path.join(BASE_DIR, '/media/'+filename)
            AddContractors.objects.create(name=name, qualification=qualification, experience=experience, address=address, mobile_no=mobile_no,email=email,status=status,profile_photo=profile_photo)
            return redirect('upload_view')
    return render(request,'Contractor.html')

def UserLogin(request):
    return render(request,'UserLogin.html')
def AddTenderBooking(request):
    return render(request,'AddTenderBooking.html')
def AddComplaint(request):
    if request.method == "POST" and request.FILES['file']:
            contractor_id = request.POST.get('t1')
            about_work= request.POST.get('t2')
            suggestions= request.POST.get('t3')
            AddComplaint.objects.create(contractor_id=contractor_id, about_work=about_work, suggestions=suggestions)
            return redirect('upload_view')
    return render(request,'AddComplaint.html')
def NewTenderProgress(request):
    if request.method == "POST" and request.FILES['file']:
            contractor_id = request.POST.get('t1')
            tender_id= request.POST.get('t2')
            work_per= request.POST.get('t3')
            entry_date = request.POST.get('t4')
            upload_photo = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(upload_photo.name,upload_photo)
            upload_file_url = fs.url(filename)
            pat = os.path.join(BASE_DIR, '/media/'+filename)
            NewTenderProgress.objects.create(contractor_id=contractor_id, tender_id=tender_id, work_per=work_per, entry_date=entry_date, upload_photo=upload_photo)
            return redirect('upload_view')
    return render(request,'NewTenderProgress.html')


def login(request):
    if request.method=="POST":
        uname=request.POST.get('t1')
        password=request.POST.get('t2')
        count=UserLogin.objects.filter(username=uname).count()
        if count>=1:
            udata=UserLogin.objects.get(username=uname)
            upass=udata.password
            utype=udata.utype
            if upass==password:
                if utype=="user":
                    return redirect('user_home')
                if utype=="admin":
                    return redirect('admin_home')
            else:
                return render(request,'login.html',{'msg':'invalid password'})
        else:
            return render(request,'login.html',{'msg':'invalid username'})
    return render(request,'login.html')


def login_view(request):
    udict=UserLogin.objects.all()
    return render(request,'login_view.html',{'udict':udict})

def login_del(request,pk):
    udata=UserLogin.objects.get(id=pk)
    udata.delete()
    return redirect('login_view')

def forgotpass(request):
    if request.method=="POST":
        email=request.POST.get('t1')
        request.session['uname']=email
        count=UserLogin.objects.filter(username=email).count()
        if count>=1:
            otp=random.randint(1000,9999)
            OtpCodeNew.objects.create(otp=otp,status='active')
            content="Your OtpCode is-"+str(otp)
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('twaheern2@gmail.com', 'zyae prmf iqzq sjtr')
            mail.sendmail('twaheern2@gmail.com', email, content)
            mail.close()
            return redirect('OtpCode')
        else:
            return render(request,'forgotpass.html',{'msg':'invalid email'})


    return render(request,'forgotpass.html')

def OtpCode(request):
    if request.method=="POST":
        otp=request.POST.get('t1')
        count=OtpCodeNew.objects.filter(otp=otp).count()
        if count>=1:
            return redirect('resetpass')
        else:
            return render(request, 'OtpCode.html',{'msg':'invalid OtpCode'})

    return render(request,'OtpCode.html')

def resetpass(request):
    uname=request.session['uname']
    if request.method=="POST":
        newpass=request.POST.get('t1')
        cpass=request.POST.get('t2')
        if newpass==cpass:
            UserLogin.objects.filter(username=uname).update(password=newpass)
            return redirect('login')
        else:
            return render(request,'resetpass.html',{'msg':'both newpass and confirm pass must be same'})
    return render(request,'resetpass.html')



def  Contractor(request):
    if request.method == "POST" and request.FILES['file']:
            name = request.POST.get('t1')
            qualification= request.POST.get('t2')
            experience= request.POST.get('t3')
            address = request.POST.get('t4')
            mobile_no= request.POST.get('t5')
            email= request.POST.get('t6')
            profile_photo = request.FILES['file']
            status = request.POST.get('t7')
            fs = FileSystemStorage()
            filename = fs.save(profile_photo.name,profile_photo)
            upload_file_url = fs.url(filename)
            pat = os.path.join(BASE_DIR, '/media/'+filename)
            AddContractors.objects.create(name=name, qualification=qualification, experience=experience, address=address, mobile_no=mobile_no,email=email,status=status,profile_photo=profile_photo)
            return redirect('upload_view')
    return render(request,'Contractor.html')

def upload_photo(request):
    return render(request,'upload_photo.html')


def upload_view(request):
    udata=AddContractors.objects.all()
    return render(request,'upload_view.html',{'udata':udata})