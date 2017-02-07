<?php 
class ComprasController extends AppController{ 
public $helpers = array('Html', 'Form', 'Flash');
public $components = array('Flash');
public function index() { 
$this->set('Compra', $this->Compra->find('all'));}
public function add() { 
if ($this->request->is('post')) { 
$this->Compra->create();
if ($this->Compra->save($this->request->data)) { 
$this->Flash->success(__('Seu Compra foi salvo'));
return $this->redirect(array('action' => 'index'));
}
$this->Flash->error(__('Unable to add your post.'));}
}
public function edit($id = null) { 
if (!$id) {
throw new NotFoundException(__('Invalid post'));
}
$Compra= $this->Compra->findById($id);
if (!$Compra) {
throw new NotFoundException(__('Invalid post'));
}
if ($this->request->is(array('post', 'put'))) {
$this->Compra->id = $id;
if ($this->Compra->save($this->request->data)) {
$this->Flash->success(__('Seu Compra foi atualizado.'));
return $this->redirect(array('action' => 'index')); 
}
$this->Flash->error(__('Unable to update your Compra.'));
}
if (!$this->request->data) {
$this->request->data = $Compra;
}
}
public function delete($id=null) { 
if ($this->request->is('get')) {
throw new MethodNotAllowedException();
}
if ($this->Compra->delete($id)) {
$this->Flash->success('Foi Salvo');
}
else {$this->Flash->error('Não foi salvo');}
return $this->redirect(array('action' => 'index'));
}
}?>