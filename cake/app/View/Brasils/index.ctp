<h2>Brasil#Index</h2>
    <table>
    <tr>
      <th>nome</th>
<th>data</th>
<th>Editar/Deletar<th></tr><?php foreach ($Brasil as $lista_Brasil): ?><tr><td><?php echo $lista_Brasil['Brasil']['nome']; ?></td><td><?php echo $lista_Brasil['Brasil']['data']; ?></td><td><?php echo $this->Form->postLink('Delete', array('action' => 'delete', $lista_Brasil['Brasil']['id']))?><?php      echo $this->Html->link('Edit', array('action' => $lista_Brasil['Brasil']['id']));?></td><?php endforeach ?>
    </tr>
    </table>
    