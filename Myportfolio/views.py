from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Myportfolio/index.html ')

def about(request):
    return render(request, 'Myportfolio/about-me.html ')

def projects(request):
    return render(request, 'Myportfolio/my-projects.html ')

def edu_Exp(request):
    return render(request, 'Myportfolio/education-experience-1.html ')

def contact(request):
    return render(request, 'Myportfolio/contact-me.html ')

def MyProjects(request):
    return render(request, 'Myportfolio/my-projects/todo.html ')

# def MyProjects(request):
#     return render(request, 'Myportfolio/my-projects/web-design.html ')

def bscCS(request):
    return render(request, 'Myportfolio/education-experience-1/BscCS.html ')

def dataDev(request):
    return render(request, 'Myportfolio/education-experience-1/data-developer.html ')

def diploma(request):
    return render(request, 'Myportfolio/education-experience-1/IT-Diploma.html ')

def intern(request):
    return render(request, 'Myportfolio/education-experience-1/it-intern.html ')

def sysDev(request):
    return render(request, 'Myportfolio/education-experience-1/System Developer.html ')

