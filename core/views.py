from django.shortcuts import render


def handler404(request):
        data = {}
        return render(request,'core/404.html', data)
