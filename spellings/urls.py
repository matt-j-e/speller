from django.urls import path
from spellings import views as spellings_app_views
from accounts import views as accounts_app_views

urlpatterns = [
	path('', spellings_app_views.index, name='index'),
	path('add_word_list', spellings_app_views.add_word_list, name='add_word_list'),
	path('schools/', spellings_app_views.schools, name='schools'),
	path('profile/<int:student_id>', spellings_app_views.profile, name='profile'),
	path('practice/<int:word_list_id>', spellings_app_views.practice, name='practice'),
	path("link/<int:school_id>", spellings_app_views.link, name='link'),
	path('save_result', spellings_app_views.save_result, name='save_result'),
	path('register/', accounts_app_views.register, name='register'),
	path('register/school', accounts_app_views.register_school, name='register_school'),
]
