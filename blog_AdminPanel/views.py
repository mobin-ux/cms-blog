from django.shortcuts import render,redirect
from blog_Articles.models import Articles
from blog_categorys.models import Categorys

def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            Article_ReleaseStatus_False = Articles.objects.filter(ReleaseStatus=False).count()
            Article_ReleaseStatus_True = Articles.objects.filter(ReleaseStatus=True).count()
            Latest_approved_articles = Articles.objects.filter(ReleaseStatus=True).order_by('-id')[:10]
            Latest_articles_awaiting_approval = Articles.objects.filter(ReleaseStatus=False).order_by('-id')[:10]
            Approved_categorys = Categorys.objects.filter(ReleaseStatus=True).count()
            Categorys_awaiting_approval = Categorys.objects.filter(ReleaseStatus=False).count()
            context = {
                'title': 'Admin Panel',
                'Article_ReleaseStatus_False': Article_ReleaseStatus_False,
                'Article_ReleaseStatus_True': Article_ReleaseStatus_True,
                'Latest_approved_articles': Latest_approved_articles,
                'Latest_articles_awaiting_approval': Latest_articles_awaiting_approval,
                'Approved_categorys': Approved_categorys,
                'Categorys_awaiting_approval': Categorys_awaiting_approval,
            }


            return render(request,'AdminPanel_Dashboard_Template/AdminPanel_Dashboard.html',context)
        else:
            return redirect('/')
    else:
        return redirect('/')

