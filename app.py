from flask import Flask, render_template, request, session
import math
import forms 
from flask_wtf.csrf import CSRFProtect

app= Flask(__name__)
app.secret_key='clave secreta'
csrf=CSRFProtect()

#decorador o ruta
@app.route('/')
def index():
    title= "IDGS804 - Intro Flask"
    listado=["Juan","Ana", "Pedro", "Luisa"]
    return render_template('index.html', title=title, listado=listado)

@app.route("/saludo1")
def saludo1():
    return render_template("saludo1.html")

@app.route("/hola")
def func():
    return "Hola mucho gusto, bienvenido a la casa de los sustos :D"

@app.route("/salu2")
def saludo2():
    return render_template("saludo2.html")

@app.route("/operasBas", methods=['GET','POST'])
def operasBas():
    res=None
    if request.method == 'POST':
        n1=request.form.get('num1')
        n2=request.form.get('num2')
        operacion=request.form.get('operacion')
        
        if operacion =='sumar':
            res=float(n1)+float(n2)
        elif operacion =='restar':
            res=float(n1)-float(n2)
        elif operacion =='multiplicar':
            res=float(n1)*float(n2)
        elif operacion=='dividir':
            res=float(n1)/float(n2)
    return render_template("operaBas.html", res=res)

@app.route("/distancia", methods=['GET','POST'])
def distancia():
    cuadradoy=None
    cuadradox=None
    distancia=None
    if request.method == 'POST':
        x1=request.form.get('x1')
        x2=request.form.get('x2')
        y1=request.form.get('y1')
        y2=request.form.get('y2')
        cuadradox= (float(x2)-float(x1)) ** 2
        cuadradoy= (float(y2)-float(y1)) ** 2
        distancia=math.sqrt(cuadradox+cuadradoy)
    return render_template("distancia.html", distancia=distancia)


@app.route("/resultado", methods=["GET","POST"])
def resul1():
    n1=request.form.get('num1')
    n2=request.form.get('num2')
    
    return f"<h1>La suma es: {float(n1)+float(n2)}</h1>"

# <parametro> si la ruta va a recibir un parametro
#RECOMENDACION DEL PROFE: DAR MISMO NOMBRE A LA FUNCION Y A LA RUA
@app.route("/user/<string:user>")
def user(user):
    return f'Hola, {user}'

@app.route("/numero/<int:n>")
def numero(n):
    return f'<h1>Numero: {n}</h1>'

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f'<h1>Hola, {username}<br>Tu ID es: {id}</h1>'

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f'<h1>La suma es: {n1+n2}</h1>'

@app.route("/default/")
@app.route("/default/<string:param>")
def func2(param='Juan'):
    return f'<h1>Hola {param}</h1>'

@app.route("/operas")
def operas():
    return '''
    <form>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    </br>
    <label for="name">apaterno:</label>
    <input type="text" id="name" name="name" required>
    </br>
    <input type="submit" value="Submit">
    </form>
    '''

@app.route("/alumnos", methods=['GET','POST'])
def alumnos():
    mat=0
    nom=''
    ape=''
    email=''
    alumno_clas=forms.userForm(request.form)
    if request.method=='POST' and alumno_clas.validate():
        mat=alumno_clas.matricula.data
        nom=alumno_clas.nombre.data
        ape=alumno_clas.apellido.data
        email=alumno_clas.correo.data
    return render_template("alumnos.html", form=alumno_clas, mat=mat, nom=nom,ape=ape, email=email)

if __name__=='__main__':
    #habilita la app solamente si se agrega la clave especificada (clave_secreta)
    #csrf.init_app(app)
    #con el debug se puede actualizar el servidor conforma se guardan los cambios, si no se coloca, se debe reiniciar
    #el servidor para que se apliquen los cambios
    app.run(debug=True)