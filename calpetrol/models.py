from django.db import models


class Classification(models.Model):
   
    class_text = models.CharField(max_length=200,default='class_quiz')
    #date = models.DateField(("Date"), default=datetime.date.today)
    
    def __str__(self):
        return self.class_text


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    choice_correct = models.CharField(max_length=200)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    #date = models.DateField(("Date"), default=datetime.date.today)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text
 
class Player(models.Model):
    name_player = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name_player
