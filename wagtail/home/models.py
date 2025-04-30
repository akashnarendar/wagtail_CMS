from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

# class HomePage(Page):
    
#     # TEMPORARY
#     intro_text = RichTextField(blank=True)
#     content_panels = Page.content_panels + [
#     FieldPanel('intro_text'),
#     ]


class HomePage(Page):
    pass  # no fields now

    
