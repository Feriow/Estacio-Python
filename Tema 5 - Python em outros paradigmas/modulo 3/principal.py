from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.debug = True

@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome=None):
   if nome:
      print(nome)
      return render_template('ola_usuario.html', usuario=nome)
   return render_template('ola_mundo.html')

@app.route('/login/', methods=['POST', 'GET'])
def login():
   if request.method == 'POST':
      nome = request.form.get('form_nome')
      return redirect(url_for("ola_mundo", nome=nome))
   return render_template('login.html')

if __name__ == '__main__':
   app.run()