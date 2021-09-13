import random, string
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.views.decorators.csrf import csrf_exempt
from .models import URL


def shortit(long_url):
    N=10
    s=string.ascii_lowercase+string.ascii_uppercase+string.digits
    url_id= ''.join(random.choices(s, k=N))

    if not URL.objects.filter(hash=url_id).exists():
        create=URL.objects.create(full_url=long_url, hash=url_id)
        return url_id
    else:
        shortit(url)



@csrf_exempt
def short_url(request):
    long_url=request.POST.get('url')
    hash=shortit(long_url)
    current_site=get_current_site(request)

    data= {
        "success": True,
        "id": hash,
        "link": "http://{}/{}".format(current_site, hash),
        "long_url": long_url
    }
    return JsonResponse(data)















