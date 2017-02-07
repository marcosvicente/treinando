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
    if os.path.exists('cake/app/View/' + nome):
        print("Ja exites")
    else:
        os.mkdir('cake/app/View/' + nome )


def criarViewIndex():
    f = open('cake/app/View/' +nome +'/index.ctp', "w+")
    f.write("<h2>"+ nome + "#Index</h2>")
    f.write("""
    <table>
    <tr>
      """)
    numero_tabelas = len(sys.argv)
    for numero_tabelas in range(2, numero_tabelas):
        tabelas_list = todas_tabelas[numero_tabelas]
        tabelas_dados = re.search('(?<!:)\w+', tabelas_list)
        tabelas = tabelas_dados.group()
        f.write("<th>"+ tabelas + "</th>\n")

    f.write("</tr>")
    f.write("<?php foreach ($"+nome+" as $lista_"+nome+"): ?>")
    f.write("<tr>")
    numero_tabelas = len(sys.argv)
    for numero_tabelas in range(2, numero_tabelas):
        tabelas_list = todas_tabelas[numero_tabelas]
        tabelas_dados = re.search('(?<!:)\w+', tabelas_list)
        tabelas = tabelas_dados.group()
        f.write("<td><?php echo $lista_"+nome+"["+nome+"]["+tabelas+"]; ?></td>")
    f.write("""
    </tr>
    </table>
    """)

    f.close()


def criarViewAdd():
    f = open('cake/app/View/' +nome +'/add.ctp', "w+")
    f.write("<h2>"+ nome + "#Add</h2>")
    f.write("""\n<?php \n""" )
    f.write("echo $this->Form->create('"+nome+"');")
    numero_tabelas = len(sys.argv)
    for numero_tabelas in range(2, numero_tabelas):
        tabelas_list = todas_tabelas[numero_tabelas]
        tabelas_dados = re.search('(?<!:)\w+', tabelas_list)
        tabelas = tabelas_dados.group()
        f.write("echo $this->Form->create('"+tabelas+"');")
    f.write("echo $this->Form->end('Salvar');")
    f.write("""\n ?> \n""" )

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

    print('create table ' + nome +'(')
    #id
    print('id int primary key not null')
    for numero_tabelas in range(2, numero_tabelas):
        tabelas_list = todas_tabelas[numero_tabelas]

        # Tipo de dados
        tipo = re.search('(?<=:)\w+', tabelas_list)

        tipo_de_dados_contruindo = tipo.group(0)

        global tipo_de_dados

        if tipo_de_dados_contruindo == 'string':
            tipo_de_dados = ' varchar '
        elif tipo_de_dados_contruindo == 'integer':
            tipo_de_dados = ' int '
        elif tipo_de_dados_contruindo == 'data':
            tipo_de_dados = ' data '
        else:
            print('deu ruim')
        #Nome tabela

        tabelas_dados = re.search('(?<!:)\w+', tabelas_list)
        global tabelas

        tabelas = tabelas_dados.group()


        # saida de dados
        print(tabelas + tipo_de_dados + " not null,")

        numero_tabelas -= numero_tabelas

    print("created_at date not null")
    print(')')

def main():
    comandos()
    criarView()
    criarViewIndex()
    criarViewAdd()
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
