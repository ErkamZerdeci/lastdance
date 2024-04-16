from django.shortcuts import render, HttpResponse
import openai

# Create your views here.
def a(request):
    if request.method == 'GET':
        API_KEY = open("API_KEY.txt",'r').read()
        story_content = open("SYSTEM_CONTENT.txt", 'r').read()
        openai.api_key = API_KEY
        chat_log = []
        chat_log.append({'role': 'system', 'content': story_content})
        chat_log.append({'role' : 'user', 'content': "Start the story"})
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = chat_log
        )
        ai_response = response['choices'][0]['message']['content']
        ai_response = ai_response.strip('/n').strip()
        chat_log.append({'role': 'assistant', 'content': ai_response})
        return HttpResponse(chat_log)
    else:
        return HttpResponse("empty")

def b(request):
    return HttpResponse("Hello b!!!")