from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


# ///get...
@login_required(login_url='/login/')
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
        )
        return redirect("/recipes/")

    queryset = Recipe.objects.all()

    search = request.GET.get("search")
    if search:
        print("searching {{search}}")
        queryset = queryset.filter(recipe_name__icontains=search)

    context = {"recipes": queryset}
    return render(request, "recipe.html", context=context)


# .......update......
def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")
        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect("/recipes/")

    context = {"recipe": queryset}
    return render(request, "recipes_update.html", context=context)


# ......delete........
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect("/recipes/")


def register(request):
    if request.method == "POST":
        data = request.POST
        user_name = data.get("user_name")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        password = data.get("password")

        if User.objects.filter(username=user_name).exists():
            messages.info(request, "User name already taken")
            return redirect("/register")
        else:
            user = User(username=user_name, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            messages.info(request, "Account created successfully.")
            return redirect("/register")

    return render(request, "register.html")


def login_user(request):
    if request.method == "POST":
        data = request.POST
        user_name = data.get("user_name")
        password = data.get("password")

        if not (User.objects.filter(username=user_name).exists()):
            messages.info(request, "User name already taken")
            return redirect("/login/")
        else:
            user = authenticate(username=user_name, password=password)
            if user is None:
                messages.error(request, "invalid credentials")
                return redirect("/login/")
            else:
                login(request, user)
                return redirect("/recipes/")

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("/login/")
