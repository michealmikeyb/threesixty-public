from django.http import JsonResponse
from django.contrib.auth.models import User

from userManagement.models import RegistrationRequest

def delete_user(request):
    if request.user.is_superuser:
        user = User.objects.filter(id=request.POST.get('id'))
        if user.exists():
            user.delete()
            return JsonResponse({'success': 'Successfully deleted user'})
        return JsonResponse({'error': 'user not found'})
    return JsonResponse({'error': 'access denied'})

def registration_link(request):
    if request.user.is_superuser:
        rid = RegistrationRequest.objects.create().rid
        link = request.get_host()+'/register?rid='+str(rid)
        return JsonResponse({'link': link})
    return JsonResponse({'error': 'access denied'})
