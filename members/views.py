from urllib import response
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from.models import Avilabe_data,Field
from .forms import FieldForm
from django.http import HttpResponse
from members.models import Avilabe_data
from django.http import HttpResponseServerError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages




def home(request):
    return render (request,'filter.html')
def details(request):
    if request.method == "POST":
        wardno = request.POST.get('ward_no')
        doorno = request.POST.get('door_no')
        newsubno = request.POST.get('new_subno')
        if wardno and doorno and newsubno:
            data = Avilabe_data.objects.filter(new_wardno=wardno, new_doorno=doorno, new_subno=newsubno)
        else:
            return HttpResponse("Invalid input. Please provide all fields.")
        filterd={'data':data}
        return render(request,'details.html',filterd)   
    else:
        return HttpResponse("Invalid data")
    
                    
   
def field(request):
    if request.method =='POST':
        form=FieldForm(request.POST)
        if form.is_valid():
            form.save()
    form = FieldForm()
    dict_form ={
        'form':form
    }
    return render(request,'field.html',dict_form)
def addMoredetail(request):
    if request.method == "POST":
        wardno =  request.POST.get('ward_no')
        newdoorno =  request.POST.get('new_doorno')
        newsubno=request.POST.get('new_subno')
        code =  request.POST.get('code')
        ownerphonenumber =  request.POST.get('ownerphonenumber')
        occupieraddress =  request.POST.get('occupier_address')
        groundfloor =  request.POST.get('ground_floor')
        firstfloor =  request.POST.get('first_floor')
        total =  request.POST.get('total')
        difference =  request.POST.get('difference')
        percentagedifference =  request.POST.get('percentage_difference')
        buildingusage =  request.POST.get('building_usage')
        remark =  request.POST.get('remark')
        en=Avilabe_data.objects.filter(new_wardno=wardno,new_doorno=newdoorno,new_subno=newsubno).update(code=code,owner_PhoneNumber=ownerphonenumber,occupier_address=occupieraddress,ground_floor =groundfloor,first_floor=firstfloor,total=total,difference=difference,percent_difference=percentagedifference,building_usage=buildingusage,remark=remark)
        # en.save()

    
    return render(request,'addMoredetails.html')
def edit(request):
    
        if request.method == 'GET':
            new_wardno =request.GET.get('new_wardno')
            new_doorno =request.GET.get('new_doorno')
            new_subno= request.GET.get('new_subno')
            print(new_wardno)
            print(new_doorno)
            print(new_subno)
            data = Avilabe_data.objects.filter(new_wardno=new_wardno,new_doorno=new_doorno,new_subno=new_subno)
            
            dict_data ={'data':data}
            print(dict_data)
        
        return render(request,'edit.html',dict_data)
def updatesave(request):   
    if request.method =='POST':
        newwardno =request.POST.get('ward_no')
        newdoorno =request.POST.get('new_doorno')
        newsubno =request.POST.get('new_subno')
        owneraddress =request.POST.get('owner_address')
        floorarea =request.POST.get('floor_area')
        buildingusage  =request.POST.get('building_usage')
        zone =request.POST.get('zone')
        roadtype =request.POST.get('roadtype')
        roadname =request.POST.get('road_name')
        bulidingage =request.POST.get('building_age')
        roofdetails =request.POST.get('roof_details')
        floordetails =request.POST.get('floordetails')
        ac =request.POST.get('Ac')
        modification =request.POST.get('modification')  
        en =Avilabe_data.objects.filter(new_wardno=newwardno,new_doorno=newdoorno,new_subno=newsubno).update(new_wardno=newwardno,new_doorno=newdoorno,new_subno=newsubno,owner_address=owneraddress,floor_area=floorarea,building_usage=buildingusage,zone=zone,road_type=roadtype,road_name=roadname,buliding_age=bulidingage,roof_details=roofdetails,floor_details=floordetails,Ac=ac,modification=modification)
        # print(en)
        # return HttpResponse('hi')
def login_view(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        return render(request, 'login.html') 
def social_survey(request):
    if request.method=='post':
        wardno=request.post.get['wardno']
        doorno   =request.post.get['dno']
        subno=request.post.get['suno']
        hname=request.post.get['houseownername']
        howner=request.post.get['gender']
        








# def logout_view(request):
#     logout(request)
#     return redirect('login')

# @login_required
# def home_view(request):
#     return render(request, 'home.html')    
        
        

        
    
    



