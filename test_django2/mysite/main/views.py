from django.shortcuts import render, redirect
from .models import Post, Board, Question


def index(request):
    postAll = Post.objects.all() # 전체 게시물 들어감
    return render(request, 'main/index.html', {'postAll':postAll}) # 사용자의 질의와 함께 렌더링

def mentor(request):
    data = Question.objects.all()
    return render(request, 'main/mentor.html', {'data': data})

def mentee(request):

    return render(request, 'main/mentee.html')

def board(request):
    boardAll = Board.objects.all() # 전체 게시물 들어감
    return render(request, 'main/board.html', {'boardAll': boardAll})

def about(request):

    return render(request, 'main/about.html')

def new(request):
    return render(request, 'main/new.html')

def postcreate(request):
    if request.method =='POST':
        blog = Board()
        blog.title = request.POST['title']
        blog.contents = request.POST['contents']
        #blog.pub_date = timezone.datetime.now()
        blog.save()
        return render(request, 'main/board.html')

        #return redirect('main/board.html')
                
def result(request):
    return render(request, 'main/result.html')

def recommend(request):
    return render(request, 'main/recommend.html')

def comment(request):
    return render(request, 'main/comment.html')

