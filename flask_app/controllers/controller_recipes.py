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
    for recipe in recipes:
        a_recipe = {
            'recipe_id': recipe.id,
            'name': recipe.name,
            'posted_by': recipe.first_name
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
    result = Recipe.add_recipe(request.form)
    return redirect("/recipes")


