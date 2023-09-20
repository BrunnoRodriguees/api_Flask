import mysql.connector
from flask import Flask, make_response, jsonify, request


#CONEXÃO COM BANCOS DE DADOS
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '2407',
    database = 'Pycodebr'
)

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False



@app.route('/carros', methods=['GET']) # PESQUISA LISTA.
def get_carros():

    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM carros')
    meus_carros = my_cursor.fetchall()

    carros = list()
    for carro in meus_carros:
        carros.append(
            {
                'id': carro[0],
                'marca': carro[1],
                'modelo': carro[2],
                'ano': carro[3]
            }
        )

    return make_response(
        jsonify(
            mensagem= 'LISTA DE CARROS.',
            carros= meus_carros
        )
    ) 



@app.route('/carros', methods=['POST']) #INCLUIR DADOS.
def create_carro():
    carro = request.json
    my_cursor = mydb.cursor()

    sql = f"INSERT INTO carros (marca, modelo, ano) VALUES ('{carro['marca']}','{carro['modelo']}',{carro['ano']})"

    my_cursor.execute(sql)
    mydb.commit()



    return make_response(
        jsonify(
            mensagem = 'CARRO ADICIONADO COM SUCESSO !',
            carro = carro
        )
    ) 


app.run()


