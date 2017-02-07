<?php 
class BrasilsController extends AppController{ 
public $helpers = array('Html', 'Form', 'Flash');
public $components = array('Flash');
public function index() { 
$this->set('Brasil', $this->Brasil->find('all'));}
public function add() { 
if ($this->request->is('post')) { 
$this->Brasil->create();
if ($this->Brasil->save($this->request->data)) { 
$this->Flash->success(__('Seu Brasil foi salvo'));
return $this->redirect(array('action' => 'index'));
}
$this->Flash->error(__('Unable to add your post.'));}
}
public function edit($id = null) { 
if (!$id) {
throw new NotFoundException(__('Invalid post'));
}
$Brasil= $this->Brasil->findById($id);
if (!$Brasil) {
throw new NotFoundException(__('Invalid post'));
}
if ($this->request->is(array('post', 'put'))) {
$this->Brasil->id = $id;
if ($this->Brasil->save($this->request->data)) {
$this->Flash->success(__('Seu Brasil foi atualizado.'));
return $this->redirect(array('action' => 'index')); 
}
$this->Flash->error(__('Unable to update your Brasil.'));
}
if (!$this->request->data) {
$this->request->data = $Brasil;
}
}
public function delete($id=null) { 
if ($this->request->is('get')) {
throw new MethodNotAllowedException();
}
if ($this->Brasil->delete($id)) {
$this->Flash->success('Foi Salvo');
}
else {$this->Flash->error('Não foi salvo');}
return $this->redirect(array('action' => 'index'));
}
}?>