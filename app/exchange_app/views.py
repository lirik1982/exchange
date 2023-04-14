from django.shortcuts import render

# Create your views here.

def exchange(request):
    name = 'kirill'
    context = {
        'name': name,
    }

    return render(request=request, template_name="exchange_app\index.html", context=context)


