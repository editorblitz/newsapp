from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from posts.models import Post, HomepageSection, HomepageSectionOrder
import json




def dashboard(request):
    # Query the ordered posts for each section
    sections = HomepageSection.objects.prefetch_related('homepagesectionorder_set__post').all()

    # Create a dictionary to store the ordered posts for each section
    ordered_posts = {}
    for section in sections:
        ordered_posts[section.name] = [order.post for order in section.homepagesectionorder_set.order_by('order')]

    # Include the ordered posts in the context
    context = {
        'published_posts': Post.objects.filter(status='published'),
        'ordered_posts': ordered_posts
    }

    return render(request, 'dashboard/dashboard.html', context)


def save_order(request):
    # Logic for saving the new order of posts in the homepage sections
    pass

@method_decorator(csrf_exempt, name='dispatch')
class SaveOrderView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            hero_order = data.get("hero", [])
            top_news_order = data.get("top_news", [])
            latest_order = data.get("latest", [])

            self.update_order("Hero", hero_order)
            self.update_order("Top News", top_news_order)
            self.update_order("Latest", latest_order)

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    def update_order(self, section_name, post_ids):
        section = HomepageSection.objects.get(name=section_name)
        HomepageSectionOrder.objects.filter(section=section).delete()

        for index, post_id in enumerate(post_ids):
            post = Post.objects.get(id=post_id)
            order = HomepageSectionOrder(section=section, post=post, order=index)
            order.save()
