from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "5b5b9d003d57f85af37e472b5b1ab24d"
IDIOMA = "es"

def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang={IDIOMA}&appid={API_KEY}"
    response = requests.get(url).json()
    return response


@app.route('/', methods=['GET', 'POST'])
def index():
    ciudad = ""
    temp = ""
    humedad = ""
    presion = ""
    descripcion = ""
    icon = ""
    error = None

    if request.method == 'POST':
        ciudad = request.form.get('txtCiudad')
        if ciudad:
            data = get_weather_data(ciudad)
            if data.get("cod") == 200:  
                temp = data["main"]["temp"]
                humedad = data["main"]["humidity"]
                presion = data["main"]["pressure"]
                descripcion = data["weather"][0]["description"]
                icon = data["weather"][0]["icon"]
            else:
                error = "No se encontró la ciudad. Por favor, inténtalo de nuevo."

    return render_template(
        'index.html',  
        ciudad=ciudad,
        temp=temp,
        humedad=humedad,
        presion=presion,
        descripcion=descripcion,
        icon=icon,
        error=error
    )

@app.route("/cv.html")
def cv():
    return render_template("cv.html")

if __name__ == '__main__':
    app.run(debug=True)
