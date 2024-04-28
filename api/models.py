from django.db import models
import json
class AIModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    num_classes = models.IntegerField(default=0)
    precision = models.TextField(default='[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]')
    recall  = models.TextField(default='[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]')
    f1_score = models.TextField(default='[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]')
    support = models.TextField(default='[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]')
    accuracy = models.DecimalField(decimal_places=2,max_digits=5,default=0.0)
    macro_avg = models.DecimalField(decimal_places=2,max_digits=5,default=0.0)
    wieghted_avg = models.DecimalField(decimal_places=2,max_digits=5,default=0.0)
    confusion_matrix = models.ImageField(upload_to='images/',null=True)
    architecture = models.JSONField(default=dict)
    model_file = models.FileField(upload_to='models/')
    dataset = models.CharField(max_length=100,default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def set_precision(self, array):
        self.precision = json.dumps(array)

    def get_precision(self):
        return json.loads(self.precision)
    
    def set_recall(self, array):
        self.recall = json.dumps(array)

    def get_recall(self):
        return json.loads(self.recall)
    
    def set_f1_score(self, array):
        self.f1_score = json.dumps(array)

    def get_f1_score(self):
        return json.loads(self.f1_score)
    
    
    def set_support(self, array):
        self.support = json.dumps(array)

    def get_support(self):
        return json.loads(self.support)
    

    def __str__(self):
        return self.name