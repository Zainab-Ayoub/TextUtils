# i've created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get the text
    vartext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    # analyze the text
    # analyzed = vartext
    if removepunc == 'on':
        analyzed = ""
        punctuations = '''.,?!:;'"—-()[]{}…/&*@'''
        for char in vartext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'removed punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif fullcaps == 'on':
        analyzed = ""
        for char in vartext:
            analyzed += char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover == 'on':
        analyzed = ""
        for char in vartext:
            if char != '\n':
                analyzed += char
        params = {'purpose': 'removed newlines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(vartext):
            if vartext[index] == ' ' and vartext[index + 1] == ' ':
                pass
            else:
                analyzed += char
        params = {'purpose': 'removed newlines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error!')
