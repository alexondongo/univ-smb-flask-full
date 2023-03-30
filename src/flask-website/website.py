from flask import Flask, render_template,request,redirect,url_for,session
import requests
app = Flask(__name__)
app.secret_key = 'secret_key'

# URL de l'API Flask
url = "http://localhost:5000"

# Faire une requête GET à l'API
response = requests.get(url)

# Récupérer les données JSON de la réponse
data = response.json()

# Afficher les données
print(data)

@app.route("/")
def start(): 
    return render_template('login.html')

@app.route("/index")
def index(): 
    return render_template('index.html')   

authtable =[]
for auth in data[0]:
	authtable.append(auth)
print(authtable)


@app.route('/login', methods=['POST'])
def login():
	username = "mon_nom_utilisateur"
	password = "mon_mot_de_passe"


	if request.form['username'] + request.form['password'] in authtable:
		print()
		session['connect'] = True
		session['username'] = request.form['username']
		return redirect(url_for('page_protégée'))
	else:
		r = request.form['username'] +":"+request.form['password']
		print(auth)
		print(r)
		return redirect(url_for("start"))
    
@app.route('/index')
def page_protégée():
	if 'connect' in session:
		return render_template('index')
	else:
		return redirect(url_for("start"))

if __name__ == '__main__':
	app.run(debug=True)

@app.route("/logout", methods=["POST"])
def logout():
	session.pop("username", None)
	return redirect(url_for("start"))

mes_user = data
print(mes_user)
@app.route('/user')
def user():
    return render_template('user.html', mes_user=mes_user)

@app.route('/proxy')
def proxy():
    return render_template('proxy.html', mes_user=mes_user)

@app.route('/web')
def web():
    return render_template('web.html', mes_user=mes_user)

@app.route('/Load')
def load():
    return render_template('Load.html', mes_user=mes_user)