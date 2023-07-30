from flask import Flask,request,render_template
from profile_  import Profile
from firebase import FirebaseAdmin

app = Flask(__name__)

fb = FirebaseAdmin()


@app.route('/')
def index():
    perfil = Profile()
    context ={
        'nombre':perfil.name,
        'imagen':perfil.image,
        'rol':perfil.role,
        'ubicacion':perfil.location,
        'url_github':perfil.url_github
    }
    return render_template('index.html',**context)

@app.route('/resume')
def resume():
    perfil_fb = fb.get_collection('perfil')
    perfil_det = perfil_fb[0]
    context = {
        'resumen':perfil_det['resumen'],
        'experiencia':perfil_det['experiencia'],
        'cv':perfil_det['cv']
    }
    return render_template('resume.html',**context)

@app.route('/projects')
def projects():
    lista_proyectos = fb.get_collection('proyectos')
    context = {
        'proyectos':lista_proyectos
    }
    return render_template('projects.html',**context)

@app.route('/contact')
def contact():
    return render_template('contact.html')


app.run(debug=True)