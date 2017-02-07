<h2>Compra#Index</h2>
    <table>
    <tr>
      <th>nome</th>
<th>price</th>
<th>Editar/Deletar<th></tr><?php foreach ($Compra as $lista_Compra): ?><tr><td><?php echo $lista_Compra['Compra']['nome']; ?></td><td><?php echo $lista_Compra['Compra']['price']; ?></td><td><?php echo $this->Form->postLink('Delete', array('action' => 'delete', $lista_Compra['Compra']['id']))?><?php echo $this->Html->link('Edit', array('action' => 'edit', $lista_Compra['Compra']['id']));?></td><?php endforeach ?>
    </tr>
    </table>
    <?php echo $this->Html->link('Add', array('action' => 'add'));?>