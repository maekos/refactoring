
## Cuarto paso

En este paso se puede ver que la variable `this_amount` es redundante. Se le
asigna el resultado del método `rental.get_charge()` y luego no cambia. Esto
nos puede indicar que se puede eliminar usando la tecnica `Replace Temp with 
Query`
Las variables temporales son un problema usualmente, se puede perder facilmente
el trackeo de para que fue creada. Por supuesto hay un precio que pagar y es la
performance, aqui el `rental.get_charge()` es calculado dos veces, pero esto
es facil de optimizar en la clase `Rental` y se puede optimizar de forma mas
efectiva cuando el código sea refactoreado.
