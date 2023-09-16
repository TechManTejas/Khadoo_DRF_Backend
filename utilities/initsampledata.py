import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "khadoo_drf_backend.settings")

# Initialize Django
django.setup()

from tag.models import Tag
from currency.models import Currency

# Tag 
tags = [
    {
        "name": "beginner"
    },
    {
        "name": "intermediate"
    },
    {
        "name": "advanced"
    },
    {
        "name": "python"
    },
    {
        "name": "web development"
    }
]

currencies = [
    {
        "code": "INR",
        "symbol": "₹"
    },
    {
        "code": "USD",
        "symbol": "$"
    }
]


def initsampledata():
    for tag in tags:
        Tag.objects.get_or_create(
            name=tag.get("name")
        )

    for currency in currencies:
        Currency.objects.get_or_create(
            code=currency.get("code"),
            symbol=currency.get("symbol")
        )