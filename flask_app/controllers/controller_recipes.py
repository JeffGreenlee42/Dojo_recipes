from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash
from flask_app.models.model_recipe import Recipe

@app.route("/recipes")
def recipes():
    if 'user_id' not in session:
        session.clear()
        return render_template("/")
    all_recipes = []
    recipes = Recipe.get_all()
    print(f"in route /recipes: recipes is {recipes}")
    for recipe in recipes:
        under30 = "No"
        if recipe['under30'] > 0:
            under30 = "Yes"
        a_recipe = {
            'recipe_id': recipe['recipe_id'],
            'name': recipe['name'],
            'under30': under30,
            'posted_by': recipe['first_name']
        }
        all_recipes.append(a_recipe)
    return render_template('recipes.html', all_recipes = all_recipes)

@app.route("/recipes/create_recipe")
def create_recipe():
    return render_template("new_recipe.html")

@app.route("/recipes/add_recipe", methods=["POST"])
def add_recipe():
    if 'user_id' not in session:
        return redirect("/logout")
    print("in controller add_recipe - About to call model add_recipe()")
    result = Recipe.add_recipe(request.form)
    return redirect("/recipes")

@app.route("/recipes/get_one/<int:recipe_id>")
def get_one(recipe_id):
    recipe = Recipe.get_one(recipe_id)
    print(f"recipe is {recipe}")
    if not recipe:
        return redirect("/recipes")
    return render_template("display_recipe.html", recipe = recipe)

@app.route("/recipes/edit_recipe/<int:recipe_id>")
def edit_recipe(recipe_id):
    if 'user_id' not in session:
        redirect("/")
    recipe = Recipe.get_one(recipe_id)
    if not recipe:
        return redirect("/recipes")
    return render_template("edit_recipe.html", recipe = recipe)