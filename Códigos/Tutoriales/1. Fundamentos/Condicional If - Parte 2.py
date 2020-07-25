# Condificional If

"""
Para hacer que el código no se vea afectado por el tema de las tildes , podemos hacer que la condición sea un poco más detallada. por ejemplo,
Podemos hacer que si el usuario escriba "Sí" o "Si", ambas ejecuten las mismas instrucciones. Para ello se utiliza un concepto conocido como los 
operadores lógicos. Ellos no son más que palabras que usamos en nuestro día a día para conectar ideas y en la programación los podemos usar para
hacer condiciones más específicas. En este caso usaremos el operador OR (O en español). Revisemos el código del bot simple: 
"""


Nombre = input("¿Cuál es tu nombre? ") # Ingresando nombre 
print("Hola "+ Nombre + "." + " Bienvenido") # Bienvenida del usuario
Respuesta = input("¿Tienes experiencia programando? Sí/No: ")
if Respuesta == "Sí" or Respuesta == "Si": # Sí el usuario escribe Sí o Si, la condición será verdadera 
    print("Bueno, creo que Python no será desafío para tí") # Recuerda que primero debe colocarse los 4 espacios (la sangría)
    #  para especificar que estas intrucciones dependen de que la condición del if sea verdadera.
else: # Ahora el else se usa para definir lo que se va a ejecutar en caso de que el usuario no escriba ni "Sí" o "Si"
    print("No te preocupes. Python es un lenguaje excelente para empezar") # Lo que sigue debajo del else también necesita de 4 espacios, es 
    # decir una sangría, para indicar de que  éstas instrucciones dependen de que la condición del if sea falsa.

print("") # Espacio en blanco
print("Sigamos aprendiendo Python. Nos vemos pronto") # Como esta instrucción no tiene espacios al inicio, entonces se está dejando claro que
 # esta instrucción no depende de la condición if.


"""
Como verás, este código no es perfecto. Por ejemplo, que pasa si no escribes "Sí" con la mayúscula inicial? el código actualmente no podrá 
detectar eso como un Sí y de una aplicará las instrucciones del else, es decir que sólo si se escribe exactamente Sí es que se cumple la
condición. ¿Cómo se puede mejorar el código entonces? Puedes hacer tus propias propuestas, sin embargo la solución la explicaremos en los 
próximos códigos.
"""