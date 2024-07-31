from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def Clips(request):
    if request.COOKIES.get('login_success'):
        return render(request, 'clips/Clips.html', {'title': 'AnimeMoments'})
    else:
        return redirect('land')

