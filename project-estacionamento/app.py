from flask import Flask,render_template,request,redirect
from models import db,Carro
from config import Config

app  = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/add', methods=['GET','POST'])
def add_carro():
    if request.method == 'POST':
        placa = request.form.get('placa')
        modelo = request.form.get('modelo')
        vaga = request.form.get('vaga')

        if not placa or not modelo or not vaga: #Verificar se os campos estão todos preenchidos
            return "Todos os campos são obrigatórios!",400
        
        if Carro.query.filter_by(vaga=vaga).first(): #Verifica se a vaga esta ocupada
            return "Erro: Essa vaga já está ocupada!",400
        
        carro = Carro(placa=placa,modelo=modelo,vaga=vaga) #Cria novo carro e salva no DB
        db.session.add(carro)
        db.session.commit()
        return redirect('/')
    
    return render_template('add.html') #Renderizar formulario para o carro

@app.route('/edit/<int:id>',methods = ['GET','POST'])
def edit_carro(id):
    carro = Carro.query.get_or_404(id)
    if request.method == 'POST': #Atualiza dados do carro
        nova_vaga = request.form['vaga']
    
        if nova_vaga != str(carro.vaga) and Carro.query.filter_by(vaga=nova_vaga).first():
            return "Erro: A nova vaga está ocupada!",400
        
        carro.placa = request.form['placa']
        carro.modelo = request.form['modelo']
        carro.vaga = nova_vaga
        db.session.commit()
        return redirect('/')

    return render_template('edit.html',carro=carro) #Renderizar o formulário para editar