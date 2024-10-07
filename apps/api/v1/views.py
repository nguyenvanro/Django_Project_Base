from django.http import HttpResponse


def test_example(request):
    return HttpResponse("Hello, world. You're at the polls index.")