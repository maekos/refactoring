
## Quinto paso

Usar la tecnica de extraer método para la variable frequent_renter_points pero
con una ligera variacion. Parece rezanable poner la responsabilidad en la
clase Rental. Nuevamente tenemos que buscar variables locales y rental es
usada y puede pasarse como parametro. Una variable temporal usada es 
frequent_renter_points pero en este caso tiene un valor de antemano. El cuerpo 
del metodo extraido no lee el valor sin embargo no se necesita pasar como
parametro, solamente asignarla.
