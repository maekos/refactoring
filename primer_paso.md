## Primer paso

* Construir un set de tests robusto, esencial.

### Extract method

La fila de ifs es un buen punto de inicio. Para empezar se puede usar la
técnica `extract method`.

Primero hay que buscar en el código cualquier variable que sea local en ese
scope. Este pedazo de código usa dos: `this_amount` y `rental`. `rental` no
se modifica por ese pedazo de codigo pero `this_amount` se modifica. Cualquier
variable no modificada se puede pasar como parametro. Las que se modifican se
debe tener un poco mas de cuidado. En este caso `this_amount` es inicializada a 
cero en cada loop por lo que se puede asignar al resultado. 
