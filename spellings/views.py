import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from spellings.models import Link, WordList, ResultList
from accounts.models import CustomUser
from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _


class NewWordListForm(ModelForm):
	class Meta:
		model = WordList
		fields = ['test_date', 'words']
		widgets = {
			'words': Textarea(attrs={'cols': 80, 'rows': 4, 'placeholder': 'Commma-separated. E.g. apple, banana, cherry'})
		}
		labels = {
			'test_date': _('Date of test (yyyy-mm-dd)'),
		}


def index(request):
	if not request.user.is_authenticated:
		return redirect('login')
	if request.user.is_teacher:
		context = {'links': Link.objects.filter(school=request.user)}
	else:
		try:
			school = Link.objects.get(student=request.user).school
		except Link.DoesNotExist:
			school = None
		context = {'word_lists': WordList.objects.filter(school=school).order_by('-test_date')}
	return render(request, 'spellings/index.html', context)


@login_required()
def schools(request):
	return render(request, 'spellings/schools.html', {'schools': CustomUser.objects.filter(is_teacher=True)})


def profile(request, student_id):
	results = ResultList.objects.filter(student=student_id).order_by('-created_date')
	return render(request, 'spellings/profile.html', {
		'results': results,
		'word_lists': to_set(results),
		'student': CustomUser.objects.get(id=student_id)
		})


def to_set(results):
	''' Converts results QuerySet to a reversed set of unique word lists '''
	lists_set = set()
	lists_list = []
	for r in results:
		lists_set.add(r.word_list)
	print(lists_set)
	for i in lists_set:
		lists_list.append(i)
	lists_list.reverse()
	print(lists_list)
	return lists_list


def practice(request, word_list_id):
	word_list = WordList.objects.get(id=word_list_id)
	return render(request, 'spellings/practice.html', {'word_list': word_list})


def add_word_list(request):
	if not request.user.is_teacher:
		return redirect('login')
	if request.method == 'POST':
		print(request.POST)
		# NEED TO HANDLE/VALIDATE THE POST DATA, ADD THE SCHOOL IDENTIFIER AND SAVE TO DATABASE
		# MAYBE SAVE POST DATA FIRST WITHOUT A COMMIT, ADD SCHOOL DATA THEN SAVE WITH COMMIT.
		# https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/#the-save-method
		form = NewWordListForm(data=request.POST)
		if form.is_valid:
			l = form.save(commit=False)
			l.school = request.user
			l.save()
			return redirect('index')
	else:
		return render(request, 'spellings/add_word_list.html', {'form': NewWordListForm()})



def link(request, school_id):
    new_link = Link.objects.create(student=request.user, school=CustomUser.objects.get(id=school_id))
    if new_link:
        return redirect("index")

@csrf_exempt
def save_result(request):
	# saved = ResultList.objects.create(word_list=word_list_id, student=request.user, score=score)
	# This needs to be formatted to accept JSON asynchronously
	# Refer to 'compose' method in Mail CS50W Project
	if request.method != 'POST':
		return JsonResponse({'error': 'POST request required'}, status=400)
	# extract data from request
	data = json.loads(request.body)
	student = data.get('student_id')
	word_list = data.get('word_list_id')
	score = data.get('score')

	print(student)
	print(word_list)
	print(score)

	saved = ResultList.objects.create(
		word_list=WordList.objects.get(id=word_list),
		student=CustomUser.objects.get(id=student),
		score=score 
		)

	return JsonResponse({'message': 'Saved'}, status=201)




