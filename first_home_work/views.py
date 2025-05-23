from django.shortcuts import render

def first_home_work(request):
    if request.method == 'GET':
        context = {
        'emoji': '🧠',
        'text': 'Первый проект на Django',
        'run_string': 'hello world',
    }
    return render(request, template_name='index.html',context=context)