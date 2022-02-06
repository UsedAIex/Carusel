from flask import Flask
from flask import url_for, request

app = Flask(__name__)


@app.route("/")
def name_of_operation():
    return "/carousel_2"


@app.route('/carousel_2')
def carousel_2():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                         <link rel="stylesheet"
                         href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                         integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                         crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/main2.css')}" />
                        <title>Каракули</title>
                        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
                      </head>
                      <body>
                        <h1>Виды Марса</h1>
                        <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
                          <div class="carousel-inner">
                            <div class="carousel-item active">
                              <img src="{url_for('static', filename='image/vid_mars_1.png')}" class="d-block w-80" alt="...">
                            </div>
                            <div class="carousel-item">
                              <img src="{url_for('static', filename='image/vid_mars_2.jpg')}" class="d-block w-80" alt="...">
                            </div>
                            <div class="carousel-item">
                              <img src="{url_for('static', filename='image/vid_mars_3.png')}" class="d-block w-80" alt="...">
                            </div>
                          </div>
                          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Previous</span>
                          </button>
                          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Next</span>
                          </button>
                        </div>
                      </body>
                    </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
