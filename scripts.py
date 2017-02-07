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

def criarViewIndex():
    f = open('cake/app/View/' +nome +'s/index.ctp', "w+")
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

    f.write("<th>Editar/Deletar<th>")
    f.write("</tr>")
    f.write("<?php foreach ($"+nome+" as $lista_"+nome+"): ?>")
    f.write("<tr>")
    numero_tabelas = len(sys.argv)
    for numero_tabelas in range(2, numero_tabelas):
        tabelas_list = todas_tabelas[numero_tabelas]
        tabelas_dados = re.search('(?<!:)\w+', tabelas_list)
        tabelas = tabelas_dados.group()
        f.write("<td><?php echo $lista_"+nome+"['"+nome+"']['"+tabelas+"']; ?></td>")
    f.write("<td>")
    f.write("<?php echo $this->Form->postLink('Delete', array('action' => 'delete', $lista_"+nome+"['"+nome+"']['id']))?>")
    f.write("<?php echo $this->Html->link('Edit', array('action' => 'edit', $lista_"+nome+"['"+nome+"']['id']));?>")

    f.write("</td>")



    f.write("<?php endforeach ?>")
    f.write("""
    </tr>
    </table>
    """)
    f.write("<?php echo $this->Html->link('Add', array('action' => 'add'));?>")

    f.close()

def criarViewAdd():
    f = open('cake/app/View/' +nome +'s/add.ctp', "w+")
    f.write("<h2>"+ nome + "#Add</h2>")
    f.write("""\n<?php \n""" )
    f.write("echo $this->Form->create('"+nome+"');")
    numero_tabelas = len(sys.argv)
    for numero_tabelas in range(2, numero_tabelas):
        tabelas_list = todas_tabelas[numero_tabelas]
        tabelas_dados = re.search('(?<!:)\w+', tabelas_list)
        tabelas = tabelas_dados.group()
        f.write("echo $this->Form->input('"+tabelas+"');")
    f.write("echo $this->Form->end('Salvar');")
    f.write("""\n ?> \n""" )

    f.close()

def criarViewEdit():
    f = open('cake/app/View/' +nome +'s/edit.ctp', "w+")
    f.write("<h2>"+ nome + "#Edit</h2>")
    f.write("""\n<?php \n""" )
    f.write("echo $this->Form->create('"+nome+"');")
    numero_tabelas = len(sys.argv)
    for numero_tabelas in range(2, numero_tabelas):
        tabelas_list = todas_tabelas[numero_tabelas]
        tabelas_dados = re.search('(?<!:)\w+', tabelas_list)
        tabelas = tabelas_dados.group()
        f.write("echo $this->Form->input('"+tabelas+"');")
    f.write("echo $this->Form->end('Salvar');")
    f.write("""\n ?> \n""" )

    f.close()

def criarController():
    f = open('cake/app/Controller/' +nome +'sController.php', "w+")
    f.write("<?php \n")
    f.write("class "+nome +"sController extends AppController{ \n")

    f.write("public $helpers = array('Html', 'Form', 'Flash');\n")
    f.write("public $components = array('Flash');\n")


    #função index
    f.write("public function index() { \n")
    f.write("$this->set('"+nome+"', $this->"+nome+"->find('all'));")
    f.write("}\n")

    #funcao add
    f.write("public function add() { \n")
    f.write("if ($this->request->is('post')) { \n")
    f.write("$this->"+nome+"->create();\n")
    f.write("if ($this->"+nome+"->save($this->request->data)) { \n")
    f.write("$this->Flash->success(__('Seu "+nome+" foi salvo'));\n")
    f.write("return $this->redirect(array('action' => 'index'));\n")
    f.write("}\n")
    f.write("$this->Flash->error(__('Unable to add your post.'));")
    f.write("}\n")
    f.write("}\n")

    #funcao edit
    f.write("public function edit($id = null) { \n")
    f.write("if (!$id) {\n")
    f.write("throw new NotFoundException(__('Invalid post'));\n")
    f.write("}\n")
    f.write("$"+nome+"= $this->"+nome+"->findById($id);\n")
    f.write("if (!$"+nome+") {\n")
    f.write("throw new NotFoundException(__('Invalid post'));\n")
    f.write("}\n")
    f.write("if ($this->request->is(array('post', 'put'))) {\n")
    f.write("$this->"+nome+"->id = $id;\n")
    f.write("if ($this->"+nome+"->save($this->request->data)) {\n")
    f.write("$this->Flash->success(__('Seu "+nome+" foi atualizado.'));\n")
    f.write("return $this->redirect(array('action' => 'index')); \n")
    f.write("}\n")
    f.write("$this->Flash->error(__('Unable to update your "+nome+".'));\n")
    f.write("}\n")

    f.write("if (!$this->request->data) {\n")
    f.write("$this->request->data = $"+nome+";\n")
    f.write("}\n")
    f.write("}\n")

    #funcao delete
    f.write("public function delete($id=null) { \n")

    f.write("if ($this->request->is('get')) {\n")
    f.write("throw new MethodNotAllowedException();\n")
    f.write("}\n")
    f.write("if ($this->"+nome+"->delete($id)) {\n")
    f.write("$this->Flash->success('Foi Salvo');\n")
    f.write("}\n")
    f.write("else {")
    f.write("$this->Flash->error('Não foi salvo');")
    f.write("}\n")

    f.write("return $this->redirect(array('action' => 'index'));\n")
    f.write("}\n")

    f.write("}")
    f.write("?>")
    f.close()

def criarModel():
    f = open('cake/app/Model/' +nome +'.php', "w+")
    f.write("<?php \n")
    f.write("class "+nome+" extends AppModel { \n")
    f.write("var $useTable = '"+nome+"';\n")
    f.write("}\n")
    f.write("?>\n")

    f.close()

def salvarDados():
    f = open('cake/app/Config/database.php')
    base = f.read()

    regex = re.compile('login')
    login = regex.search(base)
    print(login.group)

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
    criarViewIndex()
    criarViewAdd()
    criarViewEdit()
    criarController()
    criarModel()
    salvarDados()
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
