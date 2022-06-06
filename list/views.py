import hashlib
import json
import os
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from list.models import Login, TODOIList

from list.serializers import InformationSerializer, LoginSerializer, TODOIListSerializer 


@csrf_exempt
def viewall(request):
    todolist = TODOIList.objects.all()
    todolist_serializer=TODOIListSerializer(todolist,many=True)
    return JsonResponse(todolist_serializer.data,safe=False)

@csrf_exempt
def view(request,ID):
    todolist = TODOIList.objects.filter(Id = ID)
    todolist_serializer=TODOIListSerializer(todolist,many=True)
    return JsonResponse(todolist_serializer.data,safe=False)

@csrf_exempt
def addItemInTodoList(request,Email):
    login = Login.objects.filter(Email =Email)
    serializer=LoginSerializer(login,many=True)
    login_serializer1 = json.dumps(serializer.data)
    login_serializer = json.loads(login_serializer1)
    for data_ in login_serializer:
     if data_['Roles']=='Admin':
            prod=TODOIList()
            prod.Title=request.POST.get('Title')
            prod.Description=request.POST.get('Description')
            prod.save()
            return JsonResponse("Added Successfully",safe=False)
    return JsonResponse("HTTP 401: Unauthorized error",safe=False)

@csrf_exempt
def updateItemOfTodoList(request,ID,Email):
    if request.method=='POST':
        login = Login.objects.filter(Email = Email)
        serializer=LoginSerializer(login,many=True)
        login_serializer1 = json.dumps(serializer.data)
        login_serializer = json.loads(login_serializer1)
        for data_ in login_serializer:
            if data_['Roles']=='Admin':
                TODOIList.objects.filter(Id = ID).update(
                Title=request.POST.get('Title'),
                Description=request.POST.get('Description'),
                )
                return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("HTTP 401: Unauthorized error",safe=False)

@csrf_exempt
def delete(request,Email,ID):
    if request.method=='DELETE':
        print(Email)
        login = Login.objects.filter(Email = Email)
        serializer=LoginSerializer(login,many=True)
        login_serializer1 = json.dumps(serializer.data)
        login_serializer = json.loads(login_serializer1)
        for data_ in login_serializer:
            print(data_['Roles'])
            if data_['Roles']=='Admin':
                todolists=TODOIList.objects.get(Id=ID)
                todolists.delete()
                return JsonResponse("Deleted Successfully",safe=False)
        return JsonResponse("HTTP 401: Unauthorized error",safe=False)
        

@csrf_exempt
def login(request):
        login = Login.objects.filter(Email = request.POST.get('Email'))
        serializer=LoginSerializer(login,many=True)
        login_serializer1 = json.dumps(serializer.data)
        login_serializer = json.loads(login_serializer1)
        for item in login_serializer:
            #checking given input is matching with databse or not if yes then give permission to going on next page else login failure
            sha_salt = item['Salt']
            Encrypted_Password = hashlib.pbkdf2_hmac('sha256', request.POST.get('Password').encode('utf-8'), bytes(sha_salt, 'utf-8'), 100000)
            if item['Password'] == str(Encrypted_Password):
                print("Success")
                information_serializer=InformationSerializer(login,many=True)
                return JsonResponse(information_serializer.data,safe=False)
        return JsonResponse("Password Authentication Failed",safe=False)



@csrf_exempt
def add(request):
        # Saving information into Executive login details page
        frProd = Login()
        frProd.FirstName=request.POST.get('FirstName')
        frProd.LastName=request.POST.get('LastName')
        frProd.Email=request.POST.get('Email')
        frProd.IsActive=request.POST.get('IsActive')
        frProd.Roles=request.POST.get('Roles')
        #  Getting the password and doing incruption of it
        sha_salt = os.urandom(32)
        frProd.Salt = sha_salt
        new_key = hashlib.pbkdf2_hmac('sha256', request.POST.get('Password').encode('utf-8'), bytes(str(sha_salt), 'utf-8'), 100000)
        frProd.Password= new_key
        frProd.save()
        
        return JsonResponse("Added Successfully",safe=False)

