from django.shortcuts import render,redirect
from django.contrib.auth.decorators  import login_required
from django.http import Http404

from  .models import Topic, Entry
from  .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    # the main page of the learning logs
    return render(request,'learning_logs/index.html')

@login_required
def topics(request):
    #show all the topics
    topics =Topic.objects.filter(owner=request.user).order_by('date_added')
    #topics=Topic.objects.order_by('date_added')
    context= {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    # make  sure the request topic belongs to the current user
    if topic.owner != request.user:
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added')
    context= {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
    # add new topic
    if request.method !='POST':
        # will build a new form as no data subbmit
        form = TopicForm()
    else:
        # deal with the data for post
        form =TopicForm(data=request.POST)
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owner =request.user
            new_topic.save()
            
            #form.save()
            return redirect('learning_logs:topics')
        # show null form or point out the data of form is invalid
    context ={'form': form}
    return render(request,'learning_logs/new_topic.html',context )

@login_required
def new_entry(request,topic_id):
    #add new entry for specific topic
    topic = Topic.objects.get(id=topic_id)
    if request.method !='POST':
        # building a null form
        form=EntryForm()
    else:
        form= EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return redirect('learning_logs:topic',topic_id=topic_id)
        
    #show null form or point out the data is invalid
    context={'topic': topic,'form': form}
    return render(request,'learning_logs/new_entry.html',context)
        
@login_required        
def edit_entry(request,entry_id):
    #edit the existing entries
    entry = Entry.objects.get(id=entry_id)
    topic=entry.topic
    if topic.owner != request.user:
        raise Http404
    
    if request.method !='POST':
        # the first request
        form = EntryForm(instance=entry)
    else:
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_id=topic.id)
    
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)

    # my try here
#def learning_logs(request):
#    return render(request,'learning_logs/index.html')
