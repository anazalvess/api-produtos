#importação de frameworks
from flask import Flask, jsonify, request
from flask_cors import CORS 

#criar o nosso app
app = Flask(__name__)
#habilitar o CORS
CORS(app)

#criando nosso banco de dados local 
produtos = [
    {"id":1,
     "nome":"Notebook Gamer",
     "preco": 4000
     },
    {"id":2,
     "nome":"Cadeira Gamer",
     "preco": 300
     },  
    {"id":3,
     "nome":"monitor",
     "preco": 800
     }
]

#criar uma rota e o método GET (visualizar os dados)
@app.route("/listar", methods=['GET'])
def exibirProdutos():
    return jsonify(produtos)

#Criar uma rota e o método POST
@app.route("/criar",methods=['POST'])
def criarProdutos():
    produtonovo = request.get_json()
    produtos.append(produtonovo)
    return jsonify(produtonovo),201

#Criar rota e o método PUT (atualizar)
@app.route("/atualizar/<int:id>", methods=['PUT'])
def atualizarProdutos(id):
    dados = request.get_json()
    for produto in produtos:
        if produto ['id'] == id:
            produto['preco'] = dados['preco']
            return jsonify(dados)
    return jsonify({"mensagem":"ID NÃO ENCONTRADO"})

#criar uma tota e o método DELETE (apagar)
@app.route("/apagar/<int:id>", methods=['DELETE'])
def apagarProduto(id):
    for produto in produtos:
        if produto['id'] == id:
            produtos.remove(produto)
            return jsonify({"mensagem":"produto removido!"})
    return jsonify({"mansagem":"ID não encontrado"}),404

#Rodar o programa 
if __name__ == '__main__':
    app.run(port=8000,host="0.0.0.0")