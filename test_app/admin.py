from django.contrib import admin

# Register your models here.

from test_app.models import Article, Author

admin.site.register([Article, Author])