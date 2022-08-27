from django.shortcuts import redirect,render


def Base(request):
    return render(request,'main/base.html')