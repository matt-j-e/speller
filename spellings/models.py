from django.db import models
from accounts.models import CustomUser

class Link(models.Model):
	student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="pupil")
	school = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="school")

	def __str__(self):
		return f"{self.student} / {self.school}"


class WordList(models.Model):
	words = models.CharField(max_length=516)
	school = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	test_date = models.DateField()
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.school} / {self.test_date}"


class ResultList(models.Model):
	created_date = models.DateTimeField(auto_now_add=True)
	word_list = models.ForeignKey(WordList, on_delete=models.CASCADE)
	student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	score = models.SmallIntegerField()

	def __str__(self):
		return f"{self.student} / {self.created_date}"

