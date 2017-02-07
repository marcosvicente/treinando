<h2>Compras#Index</h2>
    <table>
    <tr>
      <th>nome</th>
<th>test</th>
<th>a</th>
<th>Editar/Deletar<th></tr><?php foreach ($Compras as $lista_Compras): ?><tr><td><?php echo $lista_Compras['Compras']['nome']; ?></td><td><?php echo $lista_Compras['Compras']['test']; ?></td><td><?php echo $lista_Compras['Compras']['a']; ?></td><td><?php echo $this->Form->postLink('Delete', array('action' => 'delete', $lista_Compras['Compras']['id']))?><?php      echo $this->Html->link('Edit', array('action' => $lista_Compras['Compras']['id']));?></td><?php endforeach ?>
    </tr>
    </table>
    