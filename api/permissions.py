from django.contrib.auth.models import User
from users.models import UserPermissions
from users.models import Permission

'''
checkAccept получает запрос и проверяемую привелегию,берёт пользователя из запроса и проверяет существует ли вообще запрошенная привелегия, а затем имеится ли запись назначающая данную привелегию пользователю
'''
def checkAccept(request, permission):
    try:
        permission = Permission.objects.get(permission=permission)
    except Permission.DoesNotExist:
        accept = False
    else:
        if UserPermissions.objects.filter(user=request.user, permission=permission).exists():
            accept = True
        else:
            accept = False
    return accept