from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Marlene Mood Picker</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f8f8f8;
                text-align: center;
                padding: 40px;
            }

            h1 {
                color: #333;
            }

            p {
                color: #666;
                margin-bottom: 35px;
            }

            a {
                text-decoration: none;
            }

            button {
                width: 100%;
                max-width: 350px;
                padding: 18px;
                margin: 12px;
                font-size: 20px;
                border: none;
                border-radius: 20px;
                background-color: white;
                box-shadow: 0px 3px 12px rgba(0,0,0,0.15);
                cursor: pointer;
            }
        </style>

    </head>

    <body>

        <h1>✨ Bienvenida ✨</h1>

        <p>
            Tengo una pequeña misión para ti... para el viernes 😉
        </p>

        <a href="/comida?vestimenta=Sport">
            <button>😎 Sport</button>
        </a>

        <a href="/comida?vestimenta=Semi-Casual">
            <button>✨ Semi-Casual</button>
        </a>

        <a href="/comida?vestimenta=Casual">
            <button>👔 Casual</button>
        </a>

        <a href="/comida?vestimenta=Whatever">
            <button>😜 Whatever</button>
        </a>

    </body>
    </html>
    """


@app.route("/comida")
def comida():

    vestimenta = request.args.get("vestimenta")

    return f"""
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>¿Qué se te antoja?</title>

        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f8f8f8;
                text-align: center;
                padding: 40px;
            }}

            h1 {{
                color: #333;
            }}

            p {{
                color: #666;
                margin-bottom: 35px;
            }}

            a {{
                text-decoration: none;
            }}

            button {{
                width: 100%;
                max-width: 350px;
                padding: 18px;
                margin: 12px;
                font-size: 20px;
                border: none;
                border-radius: 20px;
                background-color: white;
                box-shadow: 0px 3px 12px rgba(0,0,0,0.15);
                cursor: pointer;
            }}
        </style>

    </head>

    <body>

        <h1>🍽️ ¿Qué se te antoja hoy?</h1>

        <p>
            👗 {vestimenta}
        </p>

        <a href="/resultado?vestimenta={vestimenta}&comida=Puertorriqueña">
            <button>🇵🇷 Puertorriqueña 🍛</button>
        </a>

        <a href="/resultado?vestimenta={vestimenta}&comida=Mofongo">
            <button>🍤 Mofongo 🇵🇷</button>
        </a>

        <a href="/resultado?vestimenta={vestimenta}&comida=Italiana">
            <button>🇮🇹 Italiana 🍝</button>
        </a>

        <a href="/resultado?vestimenta={vestimenta}&comida=Japonesa">
            <button>🇯🇵 Japonesa 🍣</button>
        </a>

        <a href="/resultado?vestimenta={vestimenta}&comida=Coreana">
            <button>🇰🇷 Coreana 🍜</button>
        </a>

        <a href="/resultado?vestimenta={vestimenta}&comida=Mexicana">
            <button>🇲🇽 Mexicana 🌮</button>
        </a>

        <a href="/resultado?vestimenta={vestimenta}&comida=Peruana">
            <button>🇵🇪 Peruana 🐟</button>
        </a>

        <a href="/resultado?vestimenta={vestimenta}&comida=Cubana">
            <button>🇨🇺 Cubana 🥪</button>
        </a>

        <a href="/resultado?vestimenta={vestimenta}&comida=Burgers">
            <button>🍔 Burgers 🍟</button>
        </a>

        <a href="/resultado?vestimenta={vestimenta}&comida=Steakhouse">
            <button>🥩 Steakhouse 🥩</button>
        </a>

        <a href="/resultado?vestimenta={vestimenta}&comida=Pizza">
            <button>🍕 Pizza 🍕</button>
        </a>

        <a href="/resultado?vestimenta={vestimenta}&comida=Mariscos">
            <button>🐟 Mariscos 🦞</button>
        </a>

        <a href="/resultado?vestimenta={vestimenta}&comida=Cervecitas y Picadera">
            <button>🍺 Cervecitas & Picadera 🍻</button>
        </a>

    </body>
    </html>
    """


@app.route("/resultado")
def resultado():

    vestimenta = request.args.get("vestimenta")
    comida = request.args.get("comida")

    return f"""
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tu Selección</title>

        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f8f8f8;
                text-align: center;
                padding: 50px;
            }}

            .card {{
                background-color: white;
                max-width: 350px;
                margin: auto;
                padding: 35px;
                border-radius: 25px;
                box-shadow: 0px 3px 12px rgba(0,0,0,0.15);
            }}

            h1 {{
                color: #333;
                margin-bottom: 30px;
            }}

            p {{
                font-size: 24px;
                color: #555;
                margin: 25px 0;
            }}

            .mensaje {{
                font-size: 18px;
                color: #777;
                margin-top: 35px;
                margin-bottom: 30px;
            }}

            .whatsapp-btn {{
                width: 100%;
                max-width: 300px;
                background-color: #25D366;
                color: white;
                border: none;
                border-radius: 25px;
                padding: 16px;
                font-size: 18px;
                font-weight: bold;
                cursor: pointer;
                box-shadow: 0px 4px 12px rgba(0,0,0,0.20);
            }}

            a {{
                text-decoration: none;
            }}
        </style>

    </head>

    <body>

        <div class="card">

            <h1>✨ Misión Completada ✨</h1>

            <p>👗 {vestimenta}</p>

            <p>🍽️ {comida}</p>

            <div class="mensaje">
                Interesante... la misión continúa 🕵️‍♂️
            </div>

            <a href="https://wa.me/17876497309?text=Hola%20😊%0A%0ATe%20envío%20mis%20selecciones:%0A%0A👗%20Vestimenta:%20{vestimenta}%0A🍽️%20Comida:%20{comida}%0A%0AQuedo%20pendiente%20al%20plan%20😉"
               target="_blank">

                <button class="whatsapp-btn">
                    💬 Enviar mi selección
                </button>

            </a>

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)