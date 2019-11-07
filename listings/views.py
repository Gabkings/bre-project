from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, Paginator,PageNotAnInteger


# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)


    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html',context)


def listing(request,listing):
    listing_details = Listing.objects.filter(id=listing)

    context={
        'listing_details':listing_details
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    query_set = Listing.objects.order_by('-list_date').filter(is_published=True)

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        query_set = Listing.objects.filter(description__icontains=keywords, is_published=True)

    if 'city' in request.GET:
        city = request.GET['city']
        query_set = Listing.objects.filter(city__iexact=city, is_published=True)
    if 'state' in request.GET:
        state = request.GET['state']
        query_set = Listing.objects.filter(state__iexact=state,is_published=True)
    if 'price' in request.GET:
        price = request.GET['price']
        query_set = Listing.objects.filter(price__lte=price, is_published=True)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        query_set = Listing.objects.filter(bedrooms__lte=bedrooms, is_published=True)
    context = {
        'listings': query_set
    }
    return render(request, 'listings/search.html',context)
