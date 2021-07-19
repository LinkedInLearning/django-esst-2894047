from django.shortcuts import render
from django.http import Http404

from .models import Notes

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def detail(request, pk):
    try: 
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("This note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note': note})