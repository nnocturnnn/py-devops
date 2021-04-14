
def search_cookbook(cookbook, recipe, section):
    if len(cookbook) == 0:
        return f'There is no "{recipe}" recipe in the cookbook.'
    for key in cookbook:
        if key == recipe:
            recipe_d = cookbook.get(recipe)
            for s_key in recipe_d:
                if s_key == section:
                    return recipe_d.get(section)
            return f'There is no section "{section}" in the "{recipe}" recipe.'
    return f'There is no "{recipe}" recipe in the cookbook.'