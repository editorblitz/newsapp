from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from posts.models import Post , HomepageSection , HomepageSectionOrder
import json


def dashboard(request):
    # Query the ordered posts for each section
    sections = HomepageSection.objects.prefetch_related('homepagesectionorder_set__post').all()

    # Create a dictionary to store the ordered posts for each section
    ordered_posts = {}
    ordered_post_ids = set()  # Create a set to store the IDs of the ordered posts
    for section in sections:
        ordered_section_posts = [order.post for order in section.homepagesectionorder_set.order_by('order')]
        ordered_posts[section.name] = ordered_section_posts
        for post in ordered_section_posts:
            ordered_post_ids.add(post.id)  # Add the ID of the ordered post to the set

    # Exclude the posts that are already ordered in a section from the published_posts queryset
    published_posts = Post.objects.filter(status='published').exclude(id__in=ordered_post_ids)

    # Include the ordered posts and published_posts in the context
    context = {
        'published_posts': published_posts,
        'ordered_posts': ordered_posts
    }

    return render(request , 'dashboard/dashboard.html' , context)


def save_order(request):
    # Logic for saving the new order of posts in the homepage sections
    pass


class SaveOrderView(View):
    def post(self , request , *args , **kwargs):
        try:
            data = json.loads(request.body)
            hero_order = data.get("hero" , [])
            top_news_order = data.get("top_news" , [])
            latest_order = data.get("latest" , [])

            self.update_order("hero" , hero_order)
            self.update_order("top_news" , top_news_order)
            self.update_order("latest" , latest_order)

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False , "error": str(e)})

    def update_order(self , section_name , post_ids):
        section = HomepageSection.objects.get(name=section_name)
        HomepageSectionOrder.objects.filter(section=section).delete()

        for index , post_id in enumerate(post_ids):
            post = Post.objects.get(id=post_id)
            order = HomepageSectionOrder(section=section , post=post , order=index)
            order.save()
