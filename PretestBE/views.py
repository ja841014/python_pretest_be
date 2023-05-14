
import json
from django.db import transaction
from PretestBE.models import User
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseServerError




def user(request):

    if request.method == 'GET':
        users = []
        try:
            users_obj = User.objects.all();
            for user in users_obj:
                users.append({
                    'id': user.id,
                    'name': user.name,
                    'point': user.point,
                })
        except Exception as e:
            return HttpResponseServerError(f"An error occurred: {str(e)}")
        else:
            return JsonResponse({'users': users})

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('name')
        except Exception as e:
            return HttpResponseServerError(f"An error occurred: {str(e)}")
            
        with transaction.atomic():
            user = User.objects.create(name = username)
            user.save()
            
        return HttpResponse('User created')



def modify_points(request):
    try:
        data = json.loads(request.body)
        user = User.objects.get(id=int(data["id"]) )
        point = int(data["point"])
    except Exception as e:
        return HttpResponseServerError(f"An error occurred: {str(e)}")

    with transaction.atomic():
        if point < 0 and user.point < abs(point):
            user.point = 0
        else:
            user.point += point
        user.save()

    return HttpResponse('User modify_points')