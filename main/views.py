from django.shortcuts import render, redirect

from django.views.generic import CreateView

from .forms import RegistrationForm

from django.urls import reverse_lazy

from .models import Statement
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


class RegistrationViews(CreateView):
    template_name = 'registration/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')


@login_required
def AllStatements(request):
    statements = Statement.objects.filter(user=request.user)
    return render(request, 'main/allStatements.html', {'statements': statements})


@login_required
def CreateStatement(request):
    if request.method == 'POST':
        statement = Statement()
        statement.user = request.user
        statement.title = request.POST.get('title')
        statement.body = request.POST.get('body')
        statement.date_time = request.POST.get('date_time') 
        statement.save()
        return redirect('profile')
    return render(request, 'main/createStatement.html')

@staff_member_required
def statement_list(request):
    statements = Statement.objects.all()
    return render(request, 'admin_panel/statement_list.html', {'statements': statements})

@staff_member_required
def accept_statement(request, statement_id):
    statement = Statement.objects.get(id=statement_id)
    statement.status = 'Принято'
    statement.save()
    return redirect('statement_list')

@staff_member_required
def reject_statement(request, statement_id):
    statement = Statement.objects.get(id=statement_id)
    statement.status = 'Отклонено'
    statement.save()
    return redirect('statement_list')




