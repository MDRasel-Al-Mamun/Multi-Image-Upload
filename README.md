# Multi Image Upload - Django

###  Upload File Setup

1. Create a home app `python manage.py startapp home`

2. Define install app - ecommerce > settings > base.py - `INSTALLED_APPS = ['home.apps.HomeConfig']`

3. Create url - ecommerce > urls.py - `path('', include('home.urls'))`

4. Create url file - `home > urls.py`

5. Add CSS & JS file - static > css/js - `dropzone.min.css & dropzone.min.js`

6. Link to HTML file - templates > base > css.html/scripts.html -

   `<link rel="stylesheet" href="{% static 'css/dropzone.min.css' %}">`

   `<script type="text/javascript" src="{% static 'js/dropzone.min.js' %}"></script>`


* home > models.py

```py
from django.db import models


class Doc(models.Model):
    upload = models.FileField(upload_to='images/')

    def __str__(self):
        return str(self.pk)

```

* home > admin.py

```py
from django.contrib import admin
from .models import Doc


admin.site.register(Doc)
```

1. Run Command - `python manage.py makemigrations` & `python manage.py migrate`


* home > views.py

```py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from .models import Doc


class HomeView(TemplateView):
    template_name = 'home/index.html'


def uploadView(request):
    if request.method == 'POST':
        files = request.FILES.get('file')
        Doc.objects.create(upload=files)
        return HttpResponse('')
    return JsonResponse({'post': 'false'})

```

* home > urls.py

```py
from django.urls import path
from .views import HomeView, uploadView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload/', uploadView, name='upload')
]

```

* templates > home > index.html

```html
<div class="container mt-5">
 <form action="{% url 'upload' %}" method="POST" class="dropzone dz" id="my-dropzone">
  {% csrf_token %}
  <div class="fallback">
   <input name="file" type="file" multiple />
  </div>
 </form>
</div>
```

* static > css > style.css (If You Need)

```css
body {
  background-color: #f8f8f8;
}
.dz {
  border: dashed !important;
  border-color: #ccc  !important;
  border-radius: 10px !important;
}

.dz:hover {
  background-color: aliceblue !important;
}

```
* static > js > main.js

```js
Dropzone.autoDiscover = false;

const myDropzone = new Dropzone('#my-dropzone', {
  url: 'upload/',
  maxFiles: 20,
  maxFilesize: 2,
  acceptedFiles: '.png, .jpg',
});

```

## Getting started

Steps:

1. Clone/pull/download this repository
2. Create a virtualenv with `virtualenv venv` and install dependencies with `pip install -r requirements.txt`
3. Configure your .env variables
4. Rename your project with `python manage.py rename <yourprojectname> <newprojectname>`
5. Collect all static files `python manage.py collectstatic`

This project includes:

1. Multiple Image Upload
2. Upload Specific Files
3. Upload File & Size Fixed