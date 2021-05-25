def print_welcome():
    return """
Hello world!

This API is intended for TheFoodExplorer application.

"""


def print_man():
    return """
    api/search/image
      POST method
      form data berisi image

    api/search/<name>
      GET method
      search food using text
      nyari pake query

    api/food
      GET method
      get all food data
      query semua (SELECT *)

    api/food/<int:id>
      GET method
      get food details based on id
      pake path berupa id-nya food

    api/food/store/<int:id>
      GET method
      get food stores based on id
      pake path berupa id-nya food
    """
