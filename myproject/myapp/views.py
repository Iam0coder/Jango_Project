from django.http import HttpResponse


def data_view(request):
    return HttpResponse("<h1>Data Page</h1><p>This is the data page.</p>")


def test_view(request):
    return HttpResponse("<h1>Test Page</h1><p>This is the test page.</p>")
