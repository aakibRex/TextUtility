from django.http import HttpResponse
from django.shortcuts import render
import string


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("All about HELLO!")


def sites(request):
    return HttpResponse(''' <a href = "http://geeksforgeeks.org/">GeeksForGeeks</a> ''')


def analyze(request):
    # global params
    djtext = request.POST.get('raw_text', 'default')
    remove_punc_checkbox = request.POST.get('removepunc', 'off')
    caps_checkbox = request.POST.get('caps', 'off')
    spaceremover_checkbox = request.POST.get('spaceremover', 'off')
    duplicate_checkbox = request.POST.get('duplicate', 'off')
    counter_checkbox = request.POST.get('counter', 'off')
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    analyzed = ""
    if remove_punc_checkbox == 'on':
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if caps_checkbox == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': ' capitalization', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if spaceremover_checkbox == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed extra spaces', 'analyzed_text': analyzed}
        djtext = analyzed
    if duplicate_checkbox == "on":
        analyzed = ""
        limit = (len(djtext) - 2)
        for index, char in enumerate(djtext):
            if index > limit: break
            if djtext[index] != djtext[index + 1]:
                analyzed = analyzed + char

        params = {'purpose': 'Removed duplicates', 'analyzed_text': analyzed}
        djtext = analyzed
    if counter_checkbox == "on":
        count = 0
        for char in djtext:
            count = count + 1
        params = {'purpose': 'Character counted', 'Total_characters': count}
    return render(request, 'analyze.html', params)
