from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import request
import os
from django.core.files import File
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from rest_framework.views import APIView
from kek.serialization import reg_seria , auth_seria
from django.shortcuts import get_object_or_404, render
from .models import User
# Create your views here.
#
def Test(request):

    # print(type(request.FILES['profile']))
    data = request.FILES['profile']  # or self.files['image'] in your form

    path = default_storage.save('tes_video.MOV', ContentFile(data.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)
    return Response({'Video':'Send'})



class Registr(APIView):
# @api_view(['GET'])
    def post(self,request):
        # был post стал get для heroku

        serializer = reg_seria(data=request.query_params)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Greate user regist':True})
        else:
           return Response({"Error":"CHECK"})
# class Auth(APIView):
@api_view(['POST'])
def geT(request):

    print(request.GET['login_user'])
        # serializer = auth_seria(data=Request.query_params)

    # user_log =get_object_or_404(User, login_user = request.query_params.get('login_user'))
    try :
         User.objects.get(login_user = request.query_params.get('login_user'),
                          password=request.query_params.get('password')
                         )
         return Response({'Успешно'})


    except:
        return Response({'Неверные логин и пароль!'})
    # pas = get_object_or_404(User,password=request.query_params.get('password'))


    # return Response({'User':'auth'})
        # serializer = auth_seria(data=request.query_params)
        # # print(request.query_params)
        #
    print('DSAD')
        # print(serializer)
        # if serializer.is_valid(raise_exception=True):
        #     print('DSAD')
        #     print(serializer.check())
        #
        #     return Response({'Greate user regist': 'True'})
        # else:
        #     return Response({"Error": "CHECK"})