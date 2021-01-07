from django.shortcuts import render,redirect,HttpResponse
from .models import Articles
from blog_categorys.models import Categorys,Categorys_Article
from django.core.paginator import Paginator
from PIL import Image
import os



def add_article(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            categorys_all = Categorys.objects.filter(ReleaseStatus=True).all()
            context = {
                'title': 'Admin Panel  | Add Article',
                'error_title': None,
                'error_slug': None,
                'error_description': None,
                'error_categorys': None,
                'error_image': None,
                'done_successfully': None,
                'categorys_all': categorys_all,
            }
            if request.method == 'POST':
                # request post
                title = request.POST['title']
                slug = request.POST['slug']
                description = request.POST['description']
                categorys = request.POST.getlist('categorys')


                # end request post


                # ReleaseStatus
                try:
                    ReleaseStatus = request.POST['ReleaseStatus']

                except:
                    ReleaseStatus = False

                if ReleaseStatus == 'on':
                    ReleaseStatus = True
                else:
                    ReleaseStatus = False

                # end ReleaseStatus


                # image
                try:
                    image = request.FILES['image']
                except:
                    context['error_image'] = 'The photo should not be blank'
                    return render(request, 'AddArticle_Template/AddArticle.html', context)
                 # end image



                # slug

                slug = str(slug).replace(' ', '-')


                Article_filter_slug: Articles = Articles.objects.filter(slug__iexact=slug).first()
                if Article_filter_slug is not None:
                    context['error_slug'] = 'This slug has already been registered'
                    return render(request, 'AddArticle_Template/AddArticle.html', context)

                # end slug


                # Examines category security issues

                for Categorys_security in categorys:
                    categorys_check = Categorys.objects.filter(id=Categorys_security,ReleaseStatus=True).first()
                    if categorys_check is None:
                        context['error_categorys'] = 'There is a security problem in the categories section'
                        return render(request, 'AddArticle_Template/AddArticle.html', context)


                # end Examines category security issues




                # Check that the received content is not empty
                if title == '':
                    context['error_title'] = 'The title should not be empty'
                    return render(request, 'AddArticle_Template/AddArticle.html', context)

                elif slug == '':
                    context['error_slug'] = 'The slug should not be blank'
                    return render(request, 'AddArticle_Template/AddArticle.html', context)


                elif description == '':
                    context['error_description'] = 'The description should not be blank'
                    return render(request, 'AddArticle_Template/AddArticle.html', context)

                elif categorys == []:
                    context['error_categorys'] = 'The category should not be blank'
                    return render(request, 'AddArticle_Template/AddArticle.html', context)


                # end   Check that the received content is not empty ^


                # Persian letters are not allowed inside the snail

                Persian_letters = ['ظ', 'ط', 'ز', 'ر', 'ذ', 'د', 'ئ', 'ش', 'س', 'ی', 'ب', 'ل', 'ا', 'ت', 'ن', 'م', 'ض',
                                   'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'چ', 'پ', 'ژ']
                error_slug = 0
                for i in range(len(Persian_letters)):
                    if Persian_letters[i] in slug:
                        error_slug += int(1)

                if error_slug > 0:
                    context['error_slug'] = 'Persian letters should not be used inside the snail'
                    return render(request, 'AddArticle_Template/AddArticle.html', context)

                # end Persian letters are not allowed inside the snail

                # Check the file format
                image_name = str(image)
                UnauthorizedFormats = ['.mp3', '.mp4', '.html', '.css', '.db', '.php', '.js', '.ttf', '.py', '.zip', '.rar',
                                       '.bat', '.xs', '.txt', '.pdf', '.xss','.ico','.gif',]
                error_format = 0
                for i in range(len(UnauthorizedFormats)):
                    if UnauthorizedFormats[i] in image_name:
                        error_format += int(1)

                if error_format > 0:
                    context['error_image'] = 'This file format is not allowed'
                    return render(request, 'AddArticle_Template/AddArticle.html', context)
                # end Check the file format






                try:
                    # Create an article

                    Article = Articles.objects.create(title=title,slug=slug,description=description,image=image,ReleaseStatus=ReleaseStatus)
                    # end


                    # Related to the image

                    Article_filter: Articles = Articles.objects.filter(title__iexact=title).first()

                    Article_filter2 : Articles = Articles.objects.filter(title__iexact='b').first()

                    image_edit = Image.open(r'{}'.format(Article_filter.image.path))

                    logo = Image.open(r'{}'.format(Article_filter2.image.path))

                    image_copy = image_edit.copy()

                    position = ((image_copy.width - logo.width), (image_copy.height - logo.height))

                    image_copy.paste(logo, position)

                    os.remove(Article_filter.image.path)

                    image_copy.save('{}'.format(Article_filter.image.path))

                    Article_filter.image = Article_filter.image.name
                    Article_filter.save()

                    # end Related to the image


                    # Add category
                    for categorys_id in categorys:
                        categorys_check: Categorys = Categorys.objects.filter(id=categorys_id,ReleaseStatus=True).first()
                        if categorys_check is not None:
                            Categorys_Article_check: Categorys_Article = Categorys_Article.objects.filter(Article_id=Article_filter.id,Category_id=categorys_id).first()
                            if Categorys_Article_check is None:
                                Categorys_Article_create: Categorys_Article = Categorys_Article.objects.create(Article_id=Article_filter.id, Category_id=categorys_id)
                            else:
                                pass

                        else:
                            pass

                    # end Add category


                    context['done_successfully'] = 'done successfully'
                    return render(request, 'AddArticle_Template/AddArticle.html', context)

                except:
                    context['error_image'] = 'There is a Problem'
                    return render(request, 'AddArticle_Template/AddArticle.html', context)




            else:
                return render(request,'AddArticle_Template/AddArticle.html',context)
        else:
            return redirect('/')
    else:
        return redirect('/')




def articles(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            articles_all = Articles.objects.all()
            pr = Paginator(articles_all,20)
            page = request.GET.get('page')
            pg = pr.get_page(page)
            Approved_articles = Articles.objects.filter(ReleaseStatus=True).count()
            Articles_awaiting_approval = Articles.objects.filter(ReleaseStatus=False).count()
            context = {
                'title': 'Admin Panel  | Articles',
                'articles': articles_all,
                'Approved_articles': Approved_articles,
                'Articles_awaiting_approval': Articles_awaiting_approval,
                'pr': pr,
                'pg': pg,
            }



            return render(request,'Articles_Template/Articles.html',context)
        else:
            return redirect('/')
    else:
        return redirect('/')



def edit_article(request):
    pass


def articles_search(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
                    try:
                        articles_all = Articles.objects.all()
                        search = request.GET.get('search')
                        articles_filter = Articles.objects.filter(title__icontains=search).all()
                        pr = Paginator(articles_filter, 2)
                        page = request.GET.get('page')
                        pg = pr.get_page(page)
                        Approved_articles = Articles.objects.filter(ReleaseStatus=True).count()
                        Articles_awaiting_approval = Articles.objects.filter(ReleaseStatus=False).count()
                        context = {
                            'title': 'Admin Panel  | Articles',
                            'articles': articles_all,
                            'Approved_articles': Approved_articles,
                            'Articles_awaiting_approval': Articles_awaiting_approval,
                            'search': search,
                            'pr': pr,
                            'pg': pg,
                        }


                        return render(request,'Article_Search_Template/Articles_search.html',context)
                    except:
                        return redirect('AdminPanel:articles')
        else:
            return redirect('/')
    else:
        return redirect('/')






