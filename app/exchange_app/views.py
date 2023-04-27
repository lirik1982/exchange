from django.shortcuts import render
import requests


def exchange(request):
    response = requests.get(url="https://currate.ru/api/?get=currency_list&key=3259fd1fd93cf66b126c1626ae9c850a").json()
    currencies = response.get("data")
    tmp = []
    for cur in currencies:
        new = cur[:3]
        if new in tmp:
            continue
        else:
            tmp.append(new)

    print(request.method)
    print(tmp)

    if request.method == "POST":
        from_amount = float(request.POST.get('from_amount'))
        from_curr = request.POST.get('from_curr')
        to_curr = request.POST.get('to_curr')

        pair = from_curr + to_curr
        print(pair)
        req = "https://currate.ru/api/?get=rates&pairs=" + pair + "&key=3259fd1fd93cf66b126c1626ae9c850a"
        response = requests.get(url=req).json()
        get_rate = response.get("data")
        rate = get_rate[pair]
        print(get_rate, rate)
        converted_amount = from_amount * float(rate)
        context = {
            'currencies': tmp,
            'converted_amount': converted_amount,
        }
    else:
        print('\n**********\nget\n')
        context = {
            'currencies': tmp,
        }

    return render(request=request, template_name="exchange_app\index.html", context=context)
