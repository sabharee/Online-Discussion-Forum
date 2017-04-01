from django.shortcuts import render
from django.http import HttpResponse
from forumapp.models import Topic
def home(request):
    return HttpResponse("<h1>TOPIC</h1>")
def index(request):
    return HttpResponse("index page")
def list_topics(request):
    topic_list = Topic.objects.all()
    result='</br>'.join(topic.topic_name for topic in topic_list)
    return HttpResponse(result)
#def post(request):



# Create your views here.
