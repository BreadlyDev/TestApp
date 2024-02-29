from django.shortcuts import render
from main_page.models import UserTest
from django.contrib.auth.decorators import login_required

def display_all_results(request):
    user_tests = UserTest.objects.all().order_by('-right_answers')  # Sort in descending order
    return render(request, 'pages/results.html', {'user_tests': user_tests})



@login_required
def display_user_results(request):
    current_user = request.user
    print(current_user)
    user_tests = UserTest.objects.filter(user=current_user)
    return render(request, 'pages/user-results.html', {'user_tests': user_tests})
