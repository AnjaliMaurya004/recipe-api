from app import oauth2, schemas, models, database
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
import os
import shutil

router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
)

# Recipes endpoints

UPLOAD_DIR = "app/static/images"

# Create folder if not exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload-image/")
def upload_image(file: UploadFile = File(...), current_user: models.User = Depends(oauth2.get_current_user)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "path": file_path}

# Get all recipes with pagination
@router.get("/", response_model=list[schemas.RecipeResponse])
def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db), search: str | None = None):
    query = db.query(models.Recipe)
    if search:
        query = query.filter(models.Recipe.name.ilike(f"%{search}%"))
    recipes = query.offset(skip).limit(limit).all()
    if search and not recipes:
        raise HTTPException(status_code=404, detail="No recipes found matching your search")
    return recipes

# Get a single recipe by ID
@router.get("/{recipe_id}", response_model=schemas.RecipeResponse)
def read_recipe(recipe_id: int, db: Session = Depends(database.get_db)):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if recipe is None:
        return {"error": "Recipe not found"}
    return recipe

# Create a new recipe
@router.post("/")
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    db_recipe = models.Recipe(name=recipe.name, instructions=recipe.instructions)
    for ingredient in recipe.ingredients:
        db_recipe.ingredients.append(
            models.Ingredient(name=ingredient.name))
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

# Delete a recipe by ID
@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db.delete(recipe)
    db.commit()
    return {"message": "Recipe deleted successfully"}

# Update a recipe by ID
@router.put("/{recipe_id}")
def update_recipe(recipe_id: int, recipe: schemas.RecipeCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db_recipe.name = recipe.name
    db_recipe.instructions = recipe.instructions
    db_recipe.ingredients = [models.Ingredient(name=ingredient.name)for ingredient in recipe.ingredients]
    db.commit()
    db.refresh(db_recipe)
    return db_recipe