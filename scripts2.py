import sys

# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
    numero_tabelas =len(sys.argv)

    name = sys.argv[1]
    tabelas = sys.argv

    print('create table ' + name +'(')
    for numero_tabelas in range(2, numero_tabelas):
        print(tabelas[numero_tabelas] + " varchar(255) not null")
        numero_tabelas -= numero_tabelas

    print(')')

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
