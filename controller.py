import sys
import re
import os
def __init__():
    self.nome = nome
    self.tipo_de_dados = tipo_de_dados
    self.tabelas = tabelas
# Define a main() function that prints a little greeting.


def criarView():
    # criar Pasta
    if os.path.exists('cake/app/View/' + nome + 's'):
        print("Atualizada!")
    else:
        os.mkdir('cake/app/View/' + nome + 's')
        print("Criado!")



def criarController():
    f = open('cake/app/Controller/' +nome +'sController.php', "w+")
    f.write("<?php \n")
    f.write("class "+nome +"sController extends AppController{ \n")

    f.write("public $helpers = array('Html', 'Form', 'Flash');\n")
    f.write("public $components = array('Flash');\n")
    for numero_tabelas in range(2, numero_tabelas):
        f.write("public function "+todas_tabelas[numero_tabelas]+" (){} ;\n")

    f.close()


def comandos():
  # Get the name from the command line, using 'World' as a fallback.
    global numero_tabelas
    numero_tabelas = len(sys.argv)

    global nome
    nome = sys.argv[1]

    global todas_tabelas
    todas_tabelas = sys.argv
    #tabelas = sys.argv

    print("Criar table:\n")

    print('create table ' + nome +'(')
    for numero_tabelas in range(2, numero_tabelas):
        tabelas_list = todas_tabelas[numero_tabelas]

        # Tipo de dados
        tipo = re.search('(?<=:)\w+', tabelas_list)

        tipo_de_dados_contruindo = tipo.group(0)

        global tipo_de_dados

        if tipo_de_dados_contruindo == 'string':
            tipo_de_dados = ' varchar(255) '
        elif tipo_de_dados_contruindo == 'integer':
            tipo_de_dados = ' int '
        elif tipo_de_dados_contruindo == 'data':
            tipo_de_dados = ' data '
        elif tipo_de_dados_contruindo == 'float':
            tipo_de_dados = ' float '
        elif tipo_de_dados_contruindo == 'text':
            tipo_de_dados = ' text '
        else:
            print('deu ruim')
        #Nome tabela

        tabelas_dados = re.search('(?<!:)\w+', tabelas_list)
        global tabelas

        tabelas = tabelas_dados.group()


        # saida de dados
        print(tabelas + tipo_de_dados + " not null,")

        numero_tabelas -= numero_tabelas
    print('id int primary key not null auto_increment')

    print(')')
    print("\n")



def main():
    comandos()
    criarView()

    criarController()
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
