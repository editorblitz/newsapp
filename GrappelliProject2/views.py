from django.shortcuts import render
from posts.models import HomepageSection
def home(request):
    # Query the ordered posts for each section
    sections = HomepageSection.objects.prefetch_related('homepagesectionorder_set__post').all()

    # Create a dictionary to store the ordered posts for each section
    ordered_posts = {}
    for section in sections:
        ordered_posts[section.name] = [order.post for order in section.homepagesectionorder_set.order_by('order')]

    # Include the ordered posts in the context
    context = {
        'ordered_posts': ordered_posts
    }

    return render(request, 'home.html', context)
