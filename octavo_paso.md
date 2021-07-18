## Octavo paso

### Reemplazar el condicinal con polimorfismo

La primera parte de este problema son los ifs anidados. Es una mala idea hacer
estas preguntas basadaas en atributos de otro objeto. Debería trabajarse en 
sus propios datos. Esto implica que `get_charge` debería moverse a la clase
`Movie`. Porque se prefiere hacer esto? porque los nuevos cambios que se
proponen son acerca de añadir nuevos tipos. Si cambio un tipo de pelicula tengo
menos efecto cadena, entonces, es preferible hacer los calculos en la clase
`Movie`.
Algo similar pasa con el calculo de alquilador frecuente.
