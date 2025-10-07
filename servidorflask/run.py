from flask import Flask, render_template, redirect, url_for, session #precisei importar o session pra roda na rota do index
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.controllers.login_controller import LoginController
from app.forms.login_form import LoginForm


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

@app.route('/') #pra corrigir o erro que tava dando erro em 'usuario"
def index():
    usuario = session.get('usuario', {'identificacao': 'Visitante'})
    return render_template("index.html", usuario=usuario)
    
@app.route("/teste")
def teste():
    return render_template("teste.html")

@app.route("/withoumenu")
def wmenu():
    return render_template("layouts-without-menu.html")

@app.route("/withounavbar")
def wnavbar():
    return render_template("layouts-without-navbar.html")

@app.route("/conteinerlayout")
def contlayout():
    return render_template("layouts-container.html")

@app.route("/layoutsfluid")
def layoutsfluid():
    return render_template("layouts-fluid.html")
    
@app.route("/layoutblank")
def layoutblank():
    return render_template("layouts-blank.html")

@app.route("/pagecontaconfig")
def configconta():
    return render_template("pages-account-settings-account.html")


@app.route("/contanotificacoes")
def noticacaoes():
    return render_template("pages-account-settings-notifications.html")

@app.route("/connections")
def connections():
    return render_template("pages-account-settings-connections.html")

@app.route("/loginbasic")
def longinbasic():
    return render_template("auth-login-basic.html")

@app.route("/cadastro")
def resgistobasic():
    return render_template("auth-register-basic.html")

@app.route("/forgotpass")
def forgotpass():
    return render_template("auth-forgot-password-basic.html")

@app.route("/micerror")
def micerror():
    return render_template("pages-misc-error.html")

@app.route("/miscunder")
def miscunder():
    return render_template("pages-misc-under-maintenance.html")


@app.route("/leis")
def leis():
    return render_template("leis.html")

@app.route("/uiaccordion")
def uiaccordion():
    return render_template("ui-accordion.html")

@app.route("/uialerta")
def uialerta():
    return render_template("ui-alerts.html")

@app.route("/uibadges")
def uibadges():
    return render_template("ui-badges.html")

@app.route("/uibutoes")
def uibutoes():
    return render_template("ui-buttons.html")

@app.route("/uicarousel")
def uicarousel():
    return render_template("ui-carousel.html")

@app.route("/uicollapse")
def uicollapse():
    return render_template("ui-collapse.html")

@app.route("/uidropdowns")
def uidropdowns():
    return render_template("ui-dropdowns.html")

@app.route("/uifooter")
def uifooter():
    return render_template("ui-footer.html")


@app.route("/uilistgroups")
def uilistgroups():
    return render_template("ui-list-groups.html")


@app.route("/uimodesls")
def uimodesls():
    return render_template("ui-modals.html")

@app.route("/uinavbar")
def uinavbar():
    return render_template("ui-navbar.html")


@app.route("/uioffcanvas")
def uioffcanvas():
    return render_template("ui-offcanvas.html")

@app.route("/uipagibread")
def uipagibread():
    return render_template("ui-pagination-breadcrumbs.html")


@app.route("/uiprogress")
def uiprogress():
    return render_template("ui-progress.html")

@app.route("/uispinners")
def uispinners():
    return render_template("ui-spinners.html")

@app.route("/uitabspills")
def uitabspills():
    return render_template("ui-tabs-pills.html")

@app.route("/uitoasts")
def uitoasts():
    return render_template("ui-toasts.html")
 

@app.route("/uitoolspopovers")
def uitoolspopovers():
    return render_template("ui-tooltips-popovers.html")


@app.route("/uitypography")
def uitypography():
    return render_template("ui-typography.html")

@app.route("/exuiperfectscowbar")
def exuiperfectscowbar():
    return render_template("extended-ui-perfect-scrollbar.html")

@app.route("/iconsbox")
def iconsbox():
    return render_template("icons-boxicons.html")

@app.route("/formimputbasic")
def formimputbasic():
    return render_template("forms-basic-inputs.html")

@app.route("/uitextdivider")
def uitextdivider():
    return render_template("extended-ui-text-divider.html")

@app.route("/dicas")
def dicas():
    return render_template("dicas.html")

@app.route("/formvertical")
def formvertical():
    return render_template("form-layouts-vertical.html")

@app.route("/formhorizontal")
def formhorizontal():
    return render_template("form-layouts-horizontal.html")

@app.route("/tablesbasic")
def tablesbasic():
    return render_template("tables-basic.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        resposta = LoginController.login(formulario)
        if resposta['sexo'] == 'M':
            print('nao pode logar')
            print(resposta)

        else:
            print('pode logar')
            return render_template("index.html", usuario = resposta)
    return render_template('auth-login-basic.html', title='Login', form = formulario)


from app import models


#crie o banquinho no mysql
with app.app_context() as ctx:
    db.create_all()

#iniciar servidor quando rodar "python run.py"
if __name__ == "__main__":
    app.run(debug=True)


