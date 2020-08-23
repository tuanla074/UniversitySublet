from django.shortcuts import render, get_object_or_404

# Create your views here.
from sublets.models import SubletListing

from django.http import HttpResponse


def index(request):
    listing = SubletListing.objects.select_related('sublet_place', 'sublet_gender', 'sublet_legal_fee',
                                                   'sublet_owner_info').all()
    context = {
        'sublet_listing': listing
    }
    return render(request, 'sublets/index.html', context)


def details(request, listing_id):
    detail_sublet = get_object_or_404(
        SubletListing.objects.select_related('sublet_place', 'sublet_gender', 'sublet_legal_fee',
                                             'sublet_owner_info').all(), pk=listing_id)
    return render(request, 'sublets/details.html', {'detail_sublet': detail_sublet})


def subtenantInfo(request, listing_id):
    return render(request, 'sublets/subtenantInfo.html')


def pdf_view(request, listing_id):
    with open('templates/Generic_Sublet_Agreement_11th.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed
