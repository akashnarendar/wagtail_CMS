from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class ProjectsIndexPage(Page):
    intro = RichTextField(blank=True)

    parent_page_types = ['home.HomePage']
    subpage_types = ['projects.ProjectPage']

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]


class ProjectPage(Page):
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    description = RichTextField()
    github_url = RichTextField(blank=True)
    demo_url = RichTextField(blank=True)

    parent_page_types = ['projects.ProjectsIndexPage']
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel('banner_image'),
        FieldPanel('description'),
        FieldPanel('github_url'),
        FieldPanel('demo_url'),
    ]
