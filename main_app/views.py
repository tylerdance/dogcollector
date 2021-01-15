from django.shortcuts import render

# main_app/views.py
...
class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
dogs = [
    Dog('Chonners', 'tabby', 'foul little demon', 3),
    Dog('Talo', 'tortoise shell', 'diluted tortoise shell', 2),
    Dog('Humphrey', 'black tripod', '3 legged dog', 4)
]

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    # grab list from line 11
    return render(request, 'dogs/index.html', {'dogs': dogs})