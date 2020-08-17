#I have created this file
from django.http import HttpResponse
from django.shortcuts import render


# for HomePage
def index(request):
    return render(request, 'index.html')

#for Various Operation Over Input Text
def analyze(request):
    # Taking the inputted Text
    inputText = request.POST.get('inputText', 'default')
    cnt = 0

    #Checking for the checkboxes Value
    charCount = request.POST.get('charCount','off')
    capitalize = request.POST.get('capitalize', 'off')
    removePunc = request.POST.get('removePunc','off')
    extraSpaceRemove = request.POST.get('extraSpaceRemove','off')
    newLineRemove = request.POST.get('newLineRemove','off')

    if(charCount == 'on'):
        cnt += 1
        index = 0
        for char in inputText:
            index = index + 1
        parameter = {'Purpose':'Count Character','Analysed_Text':index}

    if(capitalize == 'on'):
        cnt += 1
        analysed = ""
        for char in inputText:
                analysed = analysed + char.upper()
        parameter = {'Purpose': 'Capitalize Text', 'Analysed_Text': analysed}
        inputText = analysed

    if(removePunc == 'on'):
        cnt += 1
        analysed = ""
        punctuationList = ''';:!@#$^-[]{}()_&*~`''';
        for char in inputText:
            if not char in punctuationList:
                analysed = analysed + char
        parameter = {'Purpose': 'Remove Punctuations', 'Analysed_Text': analysed}
        inputText = analysed

    if(extraSpaceRemove == 'on'):
        cnt += 1
        analysed = ""
        for i,char in enumerate(inputText):
            if not (inputText[i] == " " and inputText[i+1] == " "):
                analysed = analysed + char
        parameter = {'Purpose': 'Remove Extra Space', 'Analysed_Text': analysed}
        inputText = analysed

    if(newLineRemove == 'on'):
        cnt += 1
        analysed = ""
        for char in inputText:
            if char != '\n' and char != '\r':
                analysed = analysed + char
        parameter = {'Purpose': 'Remove New Line', 'Analysed_Text': analysed}
        inputText = analysed

    if cnt >= 2:
        parameter = {'Purpose': 'Operations', 'Analysed_Text': analysed}
    if(charCount == 'off' and removePunc == 'off' and newLineRemove == 'off' and extraSpaceRemove == 'off' and capitalize == 'off'):
        str = '''
        <center><h1 style="color:black; font-size:40px;margin-top:180px;">Welcome to <span style="color:RED;font-size:50p">TextRoller</span></h1></center>
        <center><h3 style="color:black; font-size:20px;margin-top:10px;"> Please Select Some Options!!</h3></center>''';

        return HttpResponse(str);
    return render(request,'analyse.html',parameter)
