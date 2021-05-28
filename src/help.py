def print_welcome():
    return """
<h1>Hello world!</h1>

<h2>This API is intended for TheFoodExplorer application.</h2>

"""


def print_man():
    return """
    <h3>api/search/image</h3>
      <p>POST method</p>
      <p>form data berisi image</p>

    <h3>api/search/<name></h3>
      <p>GET method</p>
      <p>search food using text</p>
      <p>nyari pake query</p>

    <h3>api/food</h3>
      <p>GET method</p>
      <p>get all food data</p>
      <p>query semua (SELECT *)</p>

    <h3>api/food/<int:id></h3>
      <p>GET method</p>
      <p>get food details based on id</p>
      <p>pake path berupa id-nya food</p>

    <h3>api/food/store/<int:id></h3>
      <p>GET method</p>
      <p>get food stores based on id</p>
      <p>pake path berupa id-nya food</p>
    """
