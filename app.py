from flask import Flask, jsonify, request
import json
app = Flask(__name__)

desenvolvedores= [
    {'id':0,
     'nome':'Rafael',
     'habilidades':['Python','Flask']
     },
    {'id':1,
     'nome:':'Adioaldo',
     'habilidades':['Python', 'Django']
     }
]
#Pesquisa, Altera e Exclui um desenvolvedor pelo Id
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor do Id {} não existe'.format(id)
            response = {'staus': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da Api'
            response = {'staus': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id]= dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return  jsonify({'status':'Sucesso', 'mensagem':'Registro Excluido'})

#lista todos os desenvolvedores e inclui um novo registro do desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)
    
if __name__ == '__main__':
    app.run(debug=True)
