from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.naive_bayes import GaussianNB
import joblib

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18)], null=True)
    years_married = models.PositiveIntegerField(null=True)
    religiousness = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    # occupation = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)], null=True)
    rating_of_marriage = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/affairsModel.joblib')
        self.predictions = ml_model.predict([[self.age, self.years_married, self.religiousness, self.rating_of_marriage]])
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
