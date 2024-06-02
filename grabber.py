from flask import Flask, request
from pyngrok import ngrok

app = Flask(__name__)

@app.route('/')
def home():
    user_ip = request.remote_addr
    with open("ips.txt", "a") as log:
        log.write(f"{user_ip}\n")
    return f"Votre adresse IP ({user_ip}) a été enregistrée."

if __name__ == '__main__':
    # Ouvrir un tunnel avec ngrok
    public_url = ngrok.connect(5000)
    print("ngrok tunnel ouvert à l'URL:", public_url)

    # Démarrer le serveur Flask
    app.run(debug=True)
