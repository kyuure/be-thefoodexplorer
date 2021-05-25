def print_welcome():
    return """
Hello world!

This API is intended for TheFoodExplorer application.

"""


def print_man():
    return """
    api/searchFoodByImage
      POST method
      form data berisi image

    api/searchFoodByText
      GET method
      nyari pake query

    api/getAllFoods
      GET method
      query semua (SELECT *)

    api/getFoodDetail
      GET method
      pake path berupa id-nya food

    api/getFoodStores
      GET method
      pake path berupa id-nya food
    """
