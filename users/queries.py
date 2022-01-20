def user_is_auth(request):
    if request.user.is_authenticated:
        user = True
    else:
        user = False
    return user