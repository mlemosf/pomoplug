from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Post
import markdown

# Create your views here.
class PostView(TemplateView):
    template_name = "post.html"

    def get_context_data(self, **kwargs):
        md = markdown.Markdown(extensions=["fenced_code"])
        context = super(PostView, self).get_context_data(**kwargs)
        post_slug = kwargs.get("slug")
        post = Post.objects.get(slug=post_slug)
        context["title"] = post.title
        context["content"] = post.content
        return context
