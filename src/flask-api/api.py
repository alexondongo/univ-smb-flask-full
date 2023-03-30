# save this  as API.py 

from flask import Flask, jsonify
import mysql.connector
import json

app = Flask(__name__)

@app.route('/')
def get_data():
    try:
        conn = mysql.connector.connect(
            user="root",
            password="ondongoa",
            host="localhost",
            port=3306,
            database="identity"
        )
        conn2 = mysql.connector.connect(
            user="root",
            password="ondongoa",
            host="localhost",
            port=3306,
            database="config_generator"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        cursor1 = conn2.cursor()
        cursor1.execute("SELECT * FROM load_balancer")
        rows1 = cursor1.fetchall()

        cursor2 = conn2.cursor()
        cursor2.execute("SELECT * FROM reverse_proxy")
        rows2 = cursor2.fetchall()

        cursor3 = conn2.cursor()
        cursor3.execute("SELECT * FROM webserver")
        rows3 = cursor3.fetchall()

        cursor5 = conn.cursor()
        cursor5.execute("SELECT * FROM usernames")
        rows5 = cursor5.fetchall()

        # Convertir les données en JSON
        data = []
        mes_users = []
        for row in rows5:
            user = {
                "id": row[0],
                "nom": row[1],
                "password": row[2],
            }
            auth = f"{user['nom']}{user['password']}"
            mes_users.append(auth)
        data.append(mes_users)
        mes_user=[]
        for row in rows:
            d = {
                "id": row[0],
                "nom": row[1],
                "prenom": row[2],
                "date de naissance": row[3],
            }
            
            
            data.append(d)

        for row in rows1:
            d1 = {
                "id": row[0],
                "strategy_method": row[1],
                "server1_domain": row[2],
                "server2_domain": row[3],
            }
            data.append(d1)

        for row in rows2:
            d2 = {
                "id": row[0],
                "app_location": row[1],
                "proxy_bind": row[2],
                "proxy_pass": row[3],
            }
            data.append(d2)
        
        for row in rows3:
            d3 = {
                "id": row[0],
                "root": row[1],
                "index": row[2],
                "erreur": row[3],
                "erreur_location": row[4]
            }
            data.append(d3)

        # Fermer la connexion à la base de données
        cursor.close()
        conn.close()

        cursor1.close()
        conn2.close()

        cursor2.close()
        conn2.close()

        cursor3.close()
        conn2.close()

        cursor5.close()
        conn.close()
        # Renvoyer les données sous forme de JSON
        return jsonify(data)

    except mysql.connector.Error as error:
        print(error)
        return "Error connecting to database"

if __name__ == '__main__':
    app.run(debug=True)