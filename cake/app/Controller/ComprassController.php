<?php 
class ComprassController extends AppController{ 
public $helpers = array('Html', 'Form', 'Flash');
public $components = array('Flash');
public function index() { 
$this->set('Compras', $this->Compras->find('all'));}
public function add() { 
if ($this->request->is('post')) { 
$this->Compras->create();
if ($this->Compras->save($this->request->data)) { 
$this->Flash->success(__('Seu Compras foi salvo'));
return $this->redirect(array('action' => 'index'));
}
$this->Flash->error(__('Unable to add your post.'));}
}
public function edit($id = null) { 
if (!$id) {
throw new NotFoundException(__('Invalid post'));
}
$Compras= $this->Compras->findById($id);
if (!$Compras) {
throw new NotFoundException(__('Invalid post'));
}
if ($this->request->is(array('post', 'put'))) {
$this->Compras->id = $id;
if ($this->Compras->save($this->request->data)) {
$this->Flash->success(__('Seu Compras foi atualizado.'));
return $this->redirect(array('action' => 'index')); 
}
$this->Flash->error(__('Unable to update your Compras.'));
}
if (!$this->request->data) {
$this->request->data = $Compras;
}
}
public function delete($id=null) { 
if ($this->request->is('get')) {
throw new MethodNotAllowedException();
}
if ($this->Compras->delete($id)) {
$this->Flash->success('Foi Salvo');
}
else {$this->Flash->error('Não foi salvo');}
return $this->redirect(array('action' => 'index'));
}
}?>