from flask import Flask, render_template, request, flash, redirect, url_for, jsonify

app = Flask(__name__)
app.secret_key = "405448cc1d453a4759fe37219d639e83"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

mensajes_contacto = []

@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        email = request.form.get("email", "").strip()
        mensaje = request.form.get("mensaje", "").strip()

        errores = []

        if errores:
            for error in errores:
                flash(error, "error")
            return render_template(
                "contacto.html",
            )

        # Guardar el mensaje
        nuevo_mensaje = {
            "id": len(mensajes_contacto) + 1,
            "nombre": nombre,
            "email": email,
            "mensaje": mensaje,
        }
        mensajes_contacto.append(nuevo_mensaje)

        flash(
            f"¡Gracias {nombre}! Hemos recibido tu mensaje y te contactaremos pronto.",
            "success",
        )
        return redirect(url_for("contacto"))

    return render_template("contacto.html")


@app.route("/api/mensajes")
def api_mensajes():
    """Mensajes de contacto en formato JSON"""
    return jsonify({"total": len(mensajes_contacto), "mensajes": mensajes_contacto})

if __name__ == '__main__':
    app.run(debug=True)