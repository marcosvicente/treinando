<h2>Venda#Index</h2>
    <table>
    <tr>
      <th>nome</th>
<th>price</th>
<th>Editar/Deletar<th></tr><?php foreach ($Venda as $lista_Venda): ?><tr><td><?php echo $lista_Venda['Venda']['nome']; ?></td><td><?php echo $lista_Venda['Venda']['price']; ?></td><td><?php echo $this->Form->postLink('Delete', array('action' => 'delete', $lista_Venda['Venda']['id']))?><?php      echo $this->Html->link('Edit', array('action' => $lista_Venda['Venda']['id']));?></td><?php endforeach ?>
    </tr>
    </table>
    