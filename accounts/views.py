from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import auth
from accounts.models import scholarship_info
from manager.models import Scholarship
from django.contrib import messages
from django.db.models import F
#from django.db.models.manager import objects

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            username = request.POST["username"]
            password = request.POST["password1"]
            email = request.POST["email"]

            user = User.objects.create_user(username, email, password)
            user.save()
            auth.login(request, user)
            return redirect('/index/')
        return render(request, 'accounts/signup.html')
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        #id, pw 없을 때 팝업

        if user is not None:
            auth.login(request, user)
            return redirect('/index/')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect'}) #!!!!!!!!!!!!

    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/index/')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    if request.method == "POST":
        if request.POST.get('성적장학', '') == '성적':
            return render(request, 'service1.html')
        else:
            return render(request, 'result.html')

        if request.POST.get('복지장학', '') == '복지':
            return render(request, 'service2.html')
        else:
            return render(request, 'result.html')

        if request.POST.get('개인활동장학', '') == '개인활동':
            return render(request, 'service3.html')
        else:
            return render(request, 'result.html')

        if request.POST.get('특수장학', '') == '특수':
            return render(request, 'service4.html')
        else:
            return render(request, 'result.html')
    else:
        return render(request, 'result.html')

#@login_required
def register(request):
    if request.method == "POST":
        username = request.user.username
        income = request.POST['소득분위']
        credit = request.POST['성적정보']
        grade = request.POST['학년']
        taken_credit = request.POST['이수학점']
        univ_name = request.POST['college']
        department_stype = request.POST['지원계열']
        disability = request.POST['장애여부']
        national_merit = request.POST['보훈']
        apply_stype = request.POST['입학유형']

        is_user_in_db = scholarship_info.objects.filter(uid=username)
        if is_user_in_db.count() == 0:
            scholarship_info(uid=username, income=income, grade=credit, year=grade,
                            credit=taken_credit, school=univ_name, major=department_stype,
                            impaired=disability, merit=national_merit, regular_decision=apply_stype).save()
        else:
            messages.info(request, 'You already registered your scholarship information')
            return redirect('/register/')

        return redirect('/index/')
    else:
        return render(request, 'register.html')

def need_login(request):
    return render(request, 'need_login.html')

def service1(request):
    username = request.user.username
    
    user_info = get_object_or_404(scholarship_info, uid=username)
    temp_dict = user_info.__dict__
    school_name = temp_dict["school"]
    grade_value = temp_dict["grade"]
    year_value = temp_dict["year"]
    credit_value = temp_dict["credit"]
    income_value = temp_dict["income"]
    impaired_value = temp_dict["impaired"]
    merit_value = temp_dict["merit"]
    major_value = temp_dict["major"]
    regular_decision_value = temp_dict["regular_decision"]

    result_table = Scholarship.objects.filter(school=school_name).filter(Q(grade__lte=grade_value)|Q(grade__isnull=True)).filter(Q(year=year_value)|Q(year__isnull=True)).filter(Q(credit__lte=credit_value)|Q(credit__isnull=True)).filter(Q(income__gte=income_value)|Q(income__isnull=True)).filter(Q(impaired=impaired_value)|Q(impaired__isnull=True)).filter(Q(merit=merit_value)|Q(merit__isnull=True)).filter(Q(major=major_value)|Q(major__isnull=True)).filter(Q(regular_decision=regular_decision_value)|Q(regular_decision__isnull=True)).filter(stype='성적')

    context = {
        'result_table': result_table,
    }
    return render(request, 'service1.html', context)

def service2(request):
    username = request.user.username
    
    user_info = get_object_or_404(scholarship_info, uid=username)
    temp_dict = user_info.__dict__
    school_name = temp_dict["school"]
    grade_value = temp_dict["grade"]
    year_value = temp_dict["year"]
    credit_value = temp_dict["credit"]
    income_value = temp_dict["income"]
    impaired_value = temp_dict["impaired"]
    merit_value = temp_dict["merit"]
    major_value = temp_dict["major"]
    regular_decision_value = temp_dict["regular_decision"]

    result_table = Scholarship.objects.filter(school=school_name).filter(Q(grade__lte=grade_value)|Q(grade__isnull=True)).filter(Q(year=year_value)|Q(year__isnull=True)).filter(Q(credit__lte=credit_value)|Q(credit__isnull=True)).filter(Q(income__gte=income_value)|Q(income__isnull=True)).filter(Q(impaired=impaired_value)|Q(impaired__isnull=True)).filter(Q(merit=merit_value)|Q(merit__isnull=True)).filter(Q(major=major_value)|Q(major__isnull=True)).filter(Q(regular_decision=regular_decision_value)|Q(regular_decision__isnull=True)).filter(stype='복지')

    context = {
        'result_table': result_table,
    }
    return render(request, 'service2.html', context)

def service3(request):
    username = request.user.username
    
    user_info = get_object_or_404(scholarship_info, uid=username)
    temp_dict = user_info.__dict__
    school_name = temp_dict["school"]
    grade_value = temp_dict["grade"]
    year_value = temp_dict["year"]
    credit_value = temp_dict["credit"]
    income_value = temp_dict["income"]
    impaired_value = temp_dict["impaired"]
    merit_value = temp_dict["merit"]
    major_value = temp_dict["major"]
    regular_decision_value = temp_dict["regular_decision"]

    result_table = Scholarship.objects.filter(school=school_name).filter(Q(grade__lte=grade_value)|Q(grade__isnull=True)).filter(Q(year=year_value)|Q(year__isnull=True)).filter(Q(credit__lte=credit_value)|Q(credit__isnull=True)).filter(Q(income__gte=income_value)|Q(income__isnull=True)).filter(Q(impaired=impaired_value)|Q(impaired__isnull=True)).filter(Q(merit=merit_value)|Q(merit__isnull=True)).filter(Q(major=major_value)|Q(major__isnull=True)).filter(Q(regular_decision=regular_decision_value)|Q(regular_decision__isnull=True)).filter(stype='개인활동')

    context = {
        'result_table': result_table,
    }
    return render(request, 'service3.html', context)

def service4(request):
    username = request.user.username
    
    user_info = get_object_or_404(scholarship_info, uid=username)
    temp_dict = user_info.__dict__
    school_name = temp_dict["school"]
    grade_value = temp_dict["grade"]
    year_value = temp_dict["year"]
    credit_value = temp_dict["credit"]
    income_value = temp_dict["income"]
    impaired_value = temp_dict["impaired"]
    merit_value = temp_dict["merit"]
    major_value = temp_dict["major"]
    regular_decision_value = temp_dict["regular_decision"]

    result_table = Scholarship.objects.filter(school=school_name).filter(Q(grade__lte=grade_value)|Q(grade__isnull=True)).filter(Q(year=year_value)|Q(year__isnull=True)).filter(Q(credit__lte=credit_value)|Q(credit__isnull=True)).filter(Q(income__gte=income_value)|Q(income__isnull=True)).filter(Q(impaired=impaired_value)|Q(impaired__isnull=True)).filter(Q(merit=merit_value)|Q(merit__isnull=True)).filter(Q(major=major_value)|Q(major__isnull=True)).filter(Q(regular_decision=regular_decision_value)|Q(regular_decision__isnull=True)).filter(stype='특수')

    context = {
        'result_table': result_table,
    }
    return render(request, 'service4.html', context)

def is_admin(request):
    return render(request, 'is_admin.html')