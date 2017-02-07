<?php 
class NomesController extends AppController{ 
public $helpers = array('Html', 'Form', 'Flash');
public $components = array('Flash');
public function index() { 
$this->set('Nome', $this->Nome->find('all'));}
public function add() { 
if ($this->request->is('post')) { 
$this->Nome->create();
if ($this->Nome->save($this->request->data)) { 
$this->Flash->success(__('Seu Nome foi salvo'));
return $this->redirect(array('action' => 'index'));
}
$this->Flash->error(__('Unable to add your post.'));}
}
public function edit($id = null) { 
if (!$id) {
throw new NotFoundException(__('Invalid post'));
}
$Nome= $this->Nome->findById($id);
if (!$Nome) {
throw new NotFoundException(__('Invalid post'));
}
if ($this->request->is(array('post', 'put'))) {
$this->Nome->id = $id;
if ($this->Nome->save($this->request->data)) {
$this->Flash->success(__('Seu Nome foi atualizado.'));
return $this->redirect(array('action' => 'index')); 
}
$this->Flash->error(__('Unable to update your Nome.'));
}
if (!$this->request->data) {
$this->request->data = $Nome;
}
}
public function delete($id=null) { 
if ($this->request->is('get')) {
throw new MethodNotAllowedException();
}
if ($this->Nome->delete($id)) {
$this->Flash->success('Foi Salvo');
}
else {$this->Flash->error('Não foi salvo');}
return $this->redirect(array('action' => 'index'));
}
}?>