from django.views.decorators.http import require_POST

from django.http import JsonResponse

import json

from .kipocode import kipocode_get
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST
def kipocode_ask_http(request):

    person_type = request.POST.get('person_type', None)
    socialcode = request.POST.get('socialcode', None)
    # input_name = request.POST.get('input_name', None)

    kipocode = kipocode_get(person_type, socialcode)

    context = { 'kipocode' : kipocode }

    return JsonResponse(context)
