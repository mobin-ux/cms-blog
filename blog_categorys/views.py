from django.shortcuts import render
from .models import Categorys



def add_categorys(request):
    context = {
        'error_title': None,
        'error_slug': None,
        'Created_Successfully': None,

    }

    if request.method == 'POST':

        # request post
        title = request.POST['title']
        slug = request.POST['slug']
        # end request post


        # Check that the received content is not empty
        if title == '':
            context['error_title'] = 'The title should not be empty'
            return render(request, 'AddCategorys_Template/Add_Categorys.html', context)

        elif slug == '':
            context['error_slug'] = 'The slug should not be empty'
            return render(request, 'AddCategorys_Template/Add_Categorys.html', context)

        # end Check that the received content is not empty


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




        # Persian letters are not allowed inside the snail

        Persian_letters = ['ظ', 'ط', 'ز', 'ر', 'ذ', 'د', 'ئ', 'ش', 'س', 'ی', 'ب', 'ل', 'ا', 'ت', 'ن', 'م', 'ض',
                           'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'چ', 'پ', 'ژ']
        error_slug = 0
        for i in range(len(Persian_letters)):
            if Persian_letters[i] in slug:
                error_slug += int(1)

        if error_slug > 0:
            context['error_slug'] = 'The inside of the slug should not be Persian letters'
            return render(request, 'AddCategorys_Template/Add_Categorys.html', context)

        # end Persian letters are not allowed inside the snail





        category_filter = Categorys.objects.filter(slug__iexact=slug).first()

        if category_filter is not None:
            context['error_slug'] = 'This category has already been added'
            return render(request, 'AddCategorys_Template/Add_Categorys.html',context)


        #  Build categories
        elif category_filter is None:
            slug = str(slug).replace(' ', '-')
            category = Categorys.objects.create(title=title,slug=slug,ReleaseStatus=ReleaseStatus)
            context['Created_Successfully'] = 'Created successfully'
            return render(request, 'AddCategorys_Template/Add_Categorys.html',context)
        # end Build categories

    return render(request,'AddCategorys_Template/Add_Categorys.html',context)
