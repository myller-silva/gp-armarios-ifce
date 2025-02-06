"""
app.py
Este arquivo é o ponto de entrada da aplicação.
"""


from services.facade.app_facade import AppFacade
from flask import redirect, session

# Criando a instância do Facade
app_facade = AppFacade()

# Criando o aplicativo Flask usando o Facade
app = app_facade.create_app()


@app.route("/")
def index():
    """
    Rota inicial da aplicação. 
    Aqui é feito um redirecionamento para a rota de dashboard do usuário, caso ele esteja logado.
    """
    return redirect("/user/dashboard") if "google_id" in session else redirect("/login")


@app.route("/home")
def home():
    """
    Rota inicial da aplicação. 
    Aqui é feito um redirecionamento para a rota de dashboard do usuário, caso ele esteja logado.
    """
    return redirect("/user/dashboard") if "google_id" in session else redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
