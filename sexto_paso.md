## Sexto paso
como se vio antes, variables temporales pueden ser un problema. En este caso 
tenemos dos variables temporales, ambas usadas para para obtener las rentas 
totales del cliente. Tanto el formato ASCII como el HTML necesitan esos
totales. Se utiliza la tecnica `Replace temp with query`.

Se comienza reemplazando `total_amount` con otro metodo en la clase `Customer`.
Este no es un caso simple, `total_amount` esta asignada dentro del loop asi que
se debe copiar el loop dentro del metodo que hace la consulta. Despues se 
hace lo mismo para `frequent_renter_points`.

La mayoria de los refactors reducen la cantidad de codigo pero este lo 
incrementa y ademas afecta la performance. El viejo codigo ejecuta el while una
vez mientras que el nuevo lo ejecuta tres veces. Muchos programadores no harian
este refactor por esta razon cuando en realidad no deberiamos preocuparnos por
este problema, cuando se necesite optimizar si, pero en este punto estamos en 
una mejor posicion para hacer algo con esto y hay mas opciones para hacerlo 
de forma mas efectiva. Ahora puedo escribir el metodo `html_statement` y 
agregar los tests apropiados.
Extrayendo los métodos de calculos se pudo crear el método `html_statement` y
reutilizar el código que estaba en el método original. No se va a copiar y 
pegar si las reglas del precio cambian.
