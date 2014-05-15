import json

from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from tagging.models import Tag


def list_tags(request):
    try:
        tags = Tag.objects.filter(name__istartswith=request.GET['term']).values_list('name', flat=True)
    except MultiValueDictKeyError:
        tags = []
    return JsonResponse([x.encode('utf-8') for x in tags])


class JsonResponse(HttpResponse):
    """
    HttpResponse descendant, which return response with ``application/json`` content_type.
    """
    def __init__(self, data):
        super(JsonResponse, self).__init__(content=json.dumps(data), content_type='application/json')
