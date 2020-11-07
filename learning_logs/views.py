from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request) -> HttpResponse:
    """The Home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def check_topic_owner(request, topic) -> None:
    if topic.owner != request.user:
        raise Http404


@login_required
def topics(request) -> HttpResponse:
    """The `Topics` page for Learning Log. This will show all the Topics."""
    all_topics = Topic.objects.filter(owner = request.user).order_by('date_added')
    context = { 'topics': all_topics }
    return render(request, 'learning_logs/topics.html', context)


@login_required
def single_topic(request, topic_id) -> HttpResponse:
    """Show a single topic & all it's entries."""
    topic = get_object_or_404(Topic, id = topic_id)
    # Make sure the topic belongs to the current user.
    check_topic_owner(request, topic)

    entries = topic.entry_set.order_by('-date_added')
    context = { 'topic': topic, 'entries': entries }
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        form = TopicForm() # No data has been submitted through the form, so create a blank form.
    else:
        form = TopicForm(data = request.POST) # In this case, the POST data has been submitted, 
        # so process the data.

        if form.is_valid():
            new_topic = form.save(commit = False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form.
    context = { 'form': form }
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry, associated with a topic."""
    topic = get_object_or_404(Topic, id = topic_id)

    if request.method != 'POST':
        form = EntryForm() # No POST data has been submitted, so create a blank form.
    else:
        form = EntryForm(data = request.POST) # POST data has been submitted, so process the data.
        if form.is_valid():
            if topic.owner == request.user:
                new_entry = form.save(commit = False)
                new_entry.topic = topic
                new_entry.save()
            return redirect('learning_logs:topic', topic_id = topic_id)

    # Display a blank/invalid form.
    context = { 'topic': topic, 'form': form }
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """
    Let the user edit their existing entry,\n
    which is associated with a topic.
    """
    entry = get_object_or_404(Entry, id = entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)

    if request.method != 'POST':
        # Initial request, pre populate the form with the current entry.
        form = EntryForm(instance = entry)
    else:
        # POST data has been submitted, process data.
        form = EntryForm(instance = entry, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id = topic.id)

    context = { 'entry': entry, 'topic': topic, 'form': form }
    return render(request, 'learning_logs/edit_entry.html', context)

