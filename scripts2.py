import sys
import re
# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
    numero_tabelas =len(sys.argv)

    name = sys.argv[1]
    todas_tabelas = sys.argv
    #tabelas = sys.argv

    print('create table ' + name +'(')
    for numero_tabelas in range(2, numero_tabelas):
        tabelas_list = todas_tabelas[numero_tabelas]

        # Tipo de dados
        tipo = re.search('(?<=:)\w+', tabelas_list)

        tipo_de_dados_contruindo = tipo.group(0)

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
        tabelas = tabelas_dados.group()


        # saida de dados
        #print(tabelas[numero_tabelas] + tipo_de_dados + " not null,")
        print(tabelas + tipo_de_dados + " not null,")

        numero_tabelas -= numero_tabelas

    print("created_at date not null")
    print(')')

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
