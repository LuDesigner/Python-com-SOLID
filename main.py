from cliente import Cliente
from item import Item
import os

cliente = Cliente("Lais", "Alura")
item_um = Item("Pizza", 30.00)
item_dois = Item("Suco", 15.00)

print( f"\n Cliente: {cliente.nome}, \n Endereço: {cliente.endereco}.")
print(f"\n Item: {item_um.nome}, \n Preço: {item_um.preco}.")

