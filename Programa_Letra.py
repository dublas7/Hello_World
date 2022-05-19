
print ("¡Bienvenido! Hoy te diré cuántas veces está una letra en tu frase")
frase=(input("Ingresa una frase= "))
letra=(input("Dime una letra que esté en tu frase "))

for x in frase:
    if(x == letra):
        counter +=1

print ("la letra {} se menciona {} veces" .format(letra,counter))