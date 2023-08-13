from django.shortcuts import render

# Create your views here.


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def get_recipe_name(requestPath: str) -> str:
    pathEndPos = requestPath[:-1].rfind('/')
    return requestPath[pathEndPos+1:-1]

def get_recipe(request):
    recipeQuery = get_recipe_name(request.path)
    servingsCount = int(request.GET.get('servings', 1))

    recipe = DATA[recipeQuery]
    context = {'recipe': recipe, 'servingsCount': servingsCount}
    return render(request, 'recipe.html', context)