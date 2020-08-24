from django.shortcuts import render, get_object_or_404

# Create your views here.
from sublets.models import SubletListing, Subtenant
from .filters import SubletFilter

from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from django.core.mail import EmailMessage
from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def index(request):
    listing = SubletListing.objects.all()

    my_filter = SubletFilter(request.GET, queryset=listing)
    listing = my_filter.qs
    context = {
        'sublet_listing': listing,
        'my_filter': my_filter
    }
    return render(request, 'sublets/index.html', context)


def details(request, listing_id):
    detail_sublet = get_object_or_404(
        SubletListing.objects.select_related('sublet_place', 'sublet_gender', 'sublet_legal_fee',
                                             'sublet_owner_info').all(), pk=listing_id)
    return render(request, 'sublets/details.html', {'detail_sublet': detail_sublet})


def subtenantInfo(request, listing_id):
    return render(request, 'sublets/subtenantInfo.html', {'sublet_id': listing_id})


def pdf_view(request, listing_id):
    with open('templates/Generic_Sublet_Agreement_11th.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed


def legalFee(request, listing_id):
    if request.method == 'POST':
        fullname = request.POST.get('fullname', False)
        phone = request.POST.get('phone', False)
        user_email = request.POST.get('email', False)
        photoId = request.POST.get('photoId', False)
        user_signature = request.POST.get('signature', False)
        subtenant = Subtenant(legal_name=fullname, phone_number=phone, email=user_email,
                              photo_id=photoId, signature=user_signature,
                              chosen_sub=get_object_or_404(SubletListing.objects.all(), pk=listing_id))
        subtenant.save()

        #PDF
        #change the HTML to contract later on
        pdf = render_to_pdf('sublets/subtenantInfo.html', {'sublet_id': listing_id})
        response = HttpResponse(pdf, content_type='application/pdf')
        # Download directly: response['Content-Disposition'] = 'attachment; filename="contract.pdf"'

        #Mail (Unable to send pdf yet)
        mail = EmailMessage('This is your Contract', 'Read the subject', 'unisublet@gmail.com'
                            , [user_email])
        mail.attach_file('img/Generic_Sublet_Agreement_11th.pdf')
        mail.send()
    return response
