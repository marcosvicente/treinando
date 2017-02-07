<?php 
class VendasController extends AppController{ 
public $helpers = array('Html', 'Form', 'Flash');
public $components = array('Flash');
public function index() { 
$this->set('Venda', $this->Venda->find('all'));}
public function add() { 
if ($this->request->is('post')) { 
$this->Venda->create();
if ($this->Venda->save($this->request->data)) { 
$this->Flash->success(__('Seu Venda foi salvo'));
return $this->redirect(array('action' => 'index'));
}
$this->Flash->error(__('Unable to add your post.'));}
}
public function edit($id = null) { 
if (!$id) {
throw new NotFoundException(__('Invalid post'));
}
$Venda= $this->Venda->findById($id);
if (!$Venda) {
throw new NotFoundException(__('Invalid post'));
}
if ($this->request->is(array('post', 'put'))) {
$this->Venda->id = $id;
if ($this->Venda->save($this->request->data)) {
$this->Flash->success(__('Seu Venda foi atualizado.'));
return $this->redirect(array('action' => 'index')); 
}
$this->Flash->error(__('Unable to update your Venda.'));
}
if (!$this->request->data) {
$this->request->data = $Venda;
}
}
public function delete($id=null) { 
if ($this->request->is('get')) {
throw new MethodNotAllowedException();
}
if ($this->Venda->delete($id)) {
$this->Flash->success('Foi Salvo');
}
else {$this->Flash->error('Não foi salvo');}
return $this->redirect(array('action' => 'index'));
}
}?>