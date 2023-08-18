from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/formulario', methods=['GET', 'POST'])

def index():
    if request.method == 'POST': 
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        return f"nome:{nome} <br> email {email} <br> telefone {telefone}"   
    return render_template('formulario.html')
   
if __name__ == "__main__":
    app.run(debug=True)

