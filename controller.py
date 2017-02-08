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
    print("Controller "+nome+" --------- Criado")
    numero_tabelas = len(sys.argv)
    for numero_tabelas in range(2, numero_tabelas):
        f.write("public function "+todas_tabelas[numero_tabelas]+"(){} ;\n")
        print(todas_tabelas[numero_tabelas] + " --------------------- Ok")

    f.write("} \n")
    f.write("?> \n")

    f.close()

def criarTodasView():
    numero_tabelas = len(sys.argv)
    for numero_tabelas in range(2, numero_tabelas):
        f = open('cake/app/View/'+ nome +'s/'+todas_tabelas[numero_tabelas] +'.ctp', "w+")
        f.write(todas_tabelas[numero_tabelas]+" View")
        f.write("\n")
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


    for numero_tabelas in range(2, numero_tabelas):
        tabelas_list = todas_tabelas[numero_tabelas]

        #Nome tabela

        tabelas_dados = re.search('(?<!:)\w+', tabelas_list)
        global tabelas

        tabelas = tabelas_dados.group()


        numero_tabelas -= numero_tabelas





def main():
    comandos()
    criarView()
    criarTodasView()
    criarController()
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
