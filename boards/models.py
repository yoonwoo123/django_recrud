from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length = 10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.id}: {self.title}'

class Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) # 만들어질때 1번
    updated_at = models.DateTimeField(auto_now=True) # 저장될때만 1번
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    # on_delete는 참조하는 객체가 사라질 경우 설정
    # CASCADE : 같이 삭제
    # SET_NULL : NULL 값으로 변경(NOT NULL인 경우 불가능)
    # SET_DEFAULT : DEFAULT으로 변경(DEFAULT값 없으면 불가능)
    # PROTECT : 삭제 불가
    def __str__(self):
        return f'<Board({self.board_id}):Comment({self.id})-{self.content}>'
        # 7번글의 id가 1인 댓글
        # <Board(12):Comment(1)>