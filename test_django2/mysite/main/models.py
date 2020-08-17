from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    img = models.ImageField()
    dataCreat = models.DateTimeField()
    cateogry = models.CharField(max_length=20)
    
    def __str__(self):#db에title로 저장 
        return self.title 
    
    
class Question(models.Model):

    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

    def __str__(self):#db에title로 저장 
        return self.question_text 
        
    
class Choice(models.Model):

    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    
    def __str__(self):#db에title로 저장 
        return self.choice_text 
    

    #Mentor 사용자 db
class Mentor(models.Model):
    name = models.CharField(max_length=50)
    is_male = models.BooleanField(default=True) 
    age = models.IntegerField()
    college_name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    # categogry = models.CharField(max_length=20)
    category = models.BooleanField(default=True) # checkbox계열 

    
    def __str__(self):#db에title로 저장
        
        return self.title     
    

# #Mentee 사용자 db
# class Mentee(models.Model):
#     name = models.CharField(max_length=50)
#     gender = models.BooleanField(default=True) 
#     age = models.IntegerField()
#     college_name = models.CharField(max_length=50)
#     major = models.CharField(max_length=50)
#     # categogry = models.CharField(max_length=20)
#     categogry = models.BooleanField(default=True) # checkbox계열 

    
#     def __str__(self):#db에title로 저장
        
#         return self.title     


class Board(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    dataCreat = models.DateTimeField()
    
    def __str__(self):
        return self.title

