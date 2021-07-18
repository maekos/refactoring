
## Tercer paso

Se puede ver que el metodo `amount_for` usa informacion de rental pero no usa
informacion desde el `customer`. Esto inmediatamente da la sensacion de que 
este metodo esta en el objeto equivocado. En la mayoria de los casos un metodo
debe estar en el objeto del cual usa los datos. Este metodo debe moverse a
la clase `Rental` usando la tecnica `Move method`.

### Move method
Primero se debe copiar el código en la clase `Rental` y ajustarla a su nuevo
hogar. Esto significa eliminar el parametro y renombrar el metodo cuando se
hace el movimiento y finalmente encontrar cada referencia al viejo método 
y ajustarlo para que use el nuevo método.
