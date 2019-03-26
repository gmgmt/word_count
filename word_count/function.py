from django.http import HttpResponse   #   HttpResponse   返回一个响应
from django.shortcuts import render    #  返回一个网页

'''
在这里，最开始有个问题，原理是，首先http://127.0.0.1:8000/111/去到主页面，然后点击提交
按钮，通过home.html的<form action='count'>，跳转到count.html，其原理是改变网址，并非
在原网址后添加，所以统计结果网址必须手动把原网址路径加上
'''

def home(request):
    # return HttpResponse('hello')
    return render(request, 'home.html')


def count(request):
    user_text = request.GET['text']
    # print(len(request.GET['text'])) #  打印到控制台
    total_count = len(request.GET['text'])

    word_dict = {}
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sorted_dict = sorted(word_dict.items(), key=lambda i:i[1], reverse=True)

    return render(request, 'count.html', {'count':total_count,
                                          'word':word_dict,
                                          'sorted':sorted_dict,'text':user_text})


def about(request):
    # return HttpResponse('hello')
    return render(request, 'about.html')