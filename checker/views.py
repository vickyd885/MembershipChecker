from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from checker.models import Member
# Create your views here.

def index(request):
    print "getting home page"
    return render(request, 'checker/index.html')


def check_member_status(request):
    print "called checkin"
    if request.method == "POST":
        status = False
        print "heard a post request"
        print request.POST
        search_term = request.POST['input']
        print search_term
        member = Member.objects.filter(value=search_term)
        if len(member) == 0:
            return HttpResponse(False)
        return HttpResponse(True)

