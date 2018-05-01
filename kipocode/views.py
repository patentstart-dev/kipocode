from django.views.decorators.http import require_POST

from django.http import JsonResponse
from django.http import HttpResponse

import json

from .kipocode import kipocode_get
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST
def kipocode_ask_http(request):

    person_type = request.POST.get('person_type', None)
    socialcode = request.POST.get('socialcode', None)
    # input_name = request.POST.get('input_name', None)

    print(person_type)
    print(socialcode)


    kipocode = kipocode_get(person_type, socialcode)

    print("-----------------------------")
    print(kipocode)
    print("-----------------------------")

    context = { 'kipocode' : kipocode }

    print(context)

    print(json.dumps(context))

    return HttpResponse(json.dumps(context), content_type="application/json")
    #return HttpResponse(kipocode)
