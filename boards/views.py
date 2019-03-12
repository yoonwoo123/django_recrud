import pprint
from django.shortcuts import render, redirect
from .models import Board
# Create your views here.

def index(request):
    # pprint.pprint(request)
    # pprint.pprint(type(request))
    # pprint.pprint(dir(request))
    # print(request.scheme)
    # print(request.get_host())
    # print(request.get_full_path())
    # print(request.build_absolute_uri())
    # print(request.method)
    # pprint.pprint(request.META)
    boards = Board.objects.order_by('-id')
    return render(request, 'boards/index.html', {'boards' : boards})
    
def new(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        board = Board(title=title, content=content)
        board.save()
        return redirect('boards:index')
    else:
        return render(request, 'boards/new.html')
    
# def create(request):
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     board = Board(title=title, content=content)
#     board.save()
#     return redirect('boards:index')
    
def detail(request, pk):
    board = Board.objects.get(pk=pk)
    comments = board.comment_set.all()
    context = {
        'board' : board,
        'comments' : comments
    }
    return render(request, 'boards/detail.html', context)

def delete(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == "POST":
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)
        
def edit(request, pk):
    if request.method == "POST":
        board = Board.objects.get(pk=pk)
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        board = Board.objects.get(pk=pk)
        return render(request, 'boards/edit.html',{'board':board})

# def update(request, pk):
#     board = Board.objects.get(pk=pk)
#     board.title = request.POST.get('title')
#     board.content = request.POST.get('content')
#     board.save()
#     return redirect('boards:detail', board.pk)