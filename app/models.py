from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def answer(self):
        return Answer.objects.filter(question=self, is_correct=True).first()
    
    def __str__(self):
        return self.title
    
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    title = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    