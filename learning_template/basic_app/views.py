from django.shortcuts import render


def index(request):
    contect_dict = {'text':'hello world', 'number':100}
    return render(request, 'basic_app/index.html', contect_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_template.html')
