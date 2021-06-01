def print_welcome():
    return """
<h1>Hello world!</h1>
<p>
<h3>This API is intended for FoodExplorer application.</h2>

"""


def print_man():
    return """
    <h3>api/v1/food</h3>
      <p>POST method</p>
      <p>form data berisi image</p>

    <h3>api/v1/food?q={query}</h3>
      <p>GET method</p>
      <p>search food using text</p>
      <p>nyari pake query</p>

    <h3>api/v1/food/all</h3>
      <p>GET method</p>
      <p>get all food in the database</p>
      <p>ambil semua data</p>

    <h3>api/v1/food/<int:food_id>/detail</h3>
      <p>GET method</p>
      <p>get food details based on id</p>
      <p>pake path berupa id-nya food</p>

    <h3>api/v1/food/<int:food_id>/location?latitude={latitude}&longitude={longitude}</h3>
      <p>GET method</p>
      <p>get food stores based on id</p>
      <p>pake path berupa id-nya food</p>
    """
