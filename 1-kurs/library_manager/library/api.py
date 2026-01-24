from django.http import JsonResponse
from django.contrib.auth.models import User

def check_username(request):
    username = request.GET.get('username', '')
    if len(username) < 3:
        return JsonResponse({'available': None, 'message': ''})
    
    exists = User.objects.filter(username=username).exists()
    if exists:
        return JsonResponse({'available': False, 'message': 'Bu username band'})
    else:
        return JsonResponse({'available': True, 'message': 'Username mavjud'})
