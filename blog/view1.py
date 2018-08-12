from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# def index(request):
#     return HttpResponse("你好")


def index(request):
    print(request.path,'path') 
    print(request.method, 'method')
    print(request.body, 'body')
    print(request.GET, 'GET')
    print(request.POST, 'POST')
    print(request.COOKIES, 'COOKIES')
    print(request.get_full_path(), 'fullpath')
    return render(request, 'index.html')
    # http: // 127.0.0.1: 8000/test?pl = 123/
    # /test path
    # GET method
    # b'' body
    # <QueryDict: {'pl': ['123']} > GET
    # <QueryDict: {} > POST
    # {'csrftoken': '1kAtvNvum4UKK9P8CR3gAtvT5adsBhdemn8zIcUI6QXMt2lbMraxy590rN9RKdhy', 'sessionid': 'itmfmu7gqt2zlkxgb6u7cw4k27gk3aqf'} COOKIES
    # /test?pl = 123 fullpath



