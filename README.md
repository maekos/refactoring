# refactoring
# Primera etapa

## Comentarios

* No está bien diseñado
* No es orientado a objetos.
* No hay nada malo si un programa simple. Si es un problema si es parte
  de un sistema mas complejo.
* El método `statements` en la clase `Customer` dice mucho.

Sin embargo el programa funciona.

Es hasta que queremos cambiar el sistema que empiezan los problemas. Un diseño 
pobre es dificil de cambiar. Si es dificil de darse cuenta donde se tienen que 
hacer los cambios hay una alta probabilidad que el programador cometa errores.

ie. Queremos hacer un cambio, queremos hacer que la salida del método 
statements sea en HTML. 

Considerando el impacto que este cambio tiene, en este codigo es imposible 
reusar algun comportamiento del método `statements`. El unico recurso es 
escribir un método nuevo que duplicará mucho de los comportamientos que ya 
existen. Obvio que esto no es muy costoso, ya que se copia y pega el método 
`statements` y se hacen los cambios que se deseen.

Y ahora que pasa si los precios cambian? se tiene que arreglar el código en 
ambos métodos y asegurarse que los cambios son consistentes.

El problema de copiar y pegar código es cuando se quiere hacer un cambio en el 
futuro.

Otro ejemplo

El usuario quiere hacer cambios de como se clasifican las peliculas pero
todavia no se decide que cambios va a hacer. Este cambio afecta la forma en 
que los rentals se cargan para las peliculas y la forma en que los puntos de 
alquilador frecuente son calculados.
