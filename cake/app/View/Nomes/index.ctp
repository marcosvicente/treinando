<h2>Nome#Index</h2>
    <table>
    <tr>
      <th>nome</th>
<th>price</th>
<th>Editar/Deletar<th></tr><?php foreach ($Nome as $lista_Nome): ?><tr><td><?php echo $lista_Nome['Nome']['nome']; ?></td><td><?php echo $lista_Nome['Nome']['price']; ?></td><td><?php echo $this->Form->postLink('Delete', array('action' => 'delete', $lista_Nome['Nome']['id']))?><?php      echo $this->Html->link('Edit', array('action' => $lista_Nome['Nome']['id']));?></td><?php endforeach ?>
    </tr>
    </table>
    