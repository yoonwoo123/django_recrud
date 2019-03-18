import pprint
from django.shortcuts import render, redirect
from .models import Board, Comment
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
        board.image = request.FILES.get('image')
        board.video = request.FILES.get('video')
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
    
def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    comments = board.comment_set.all()  
    context = {                             
        'board' : board,
        'comments' : comments
    }
    return render(request, 'boards/detail.html', context)

def delete(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == "POST":
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)
        
def edit(request, board_pk):
    if request.method == "POST":
        board = Board.objects.get(pk=board_pk)
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        board = Board.objects.get(pk=board_pk)
        return render(request, 'boards/edit.html',{'board':board})

# def update(request, pk):
#     board = Board.objects.get(pk=pk)
#     board.title = request.POST.get('title')
#     board.content = request.POST.get('content')
#     board.save()
#     return redirect('boards:detail', board.pk)

def comments_create(request, board_pk):
    if request.method == "POST":
        # 1. 댓글 달 게시물을 가져온다
        board = Board.objects.get(pk=board_pk)
        # 2. 댓글을 저장한다.
        comment = Comment()
        comment.content = request.POST.get('content')
        comment.board = board
        comment.save()
    return redirect('boards:detail', board.pk) # board.pk = comment.board_id 와 동일
    
def comments_delete(request, board_pk, comment_pk):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
    return redirect('boards:detail', board_pk)