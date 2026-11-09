#include <Servo.h>

Servo myservo; // crea el objeto servo para controlarlo
// se pueden definir hasta 8 servos

int pos = 0; // crea la variable de posición del servo

void setup()
{
myservo.attach(9); // define el pin de trabajo del servo
}


void loop()
{
for(pos = 0;pos < 180; pos += 1) // hace un barrido desde 0 a 180
// grados con incrementos de 1
{
myservo.write(pos); // ordena al servo que se mueva
delay(20); // espera 20 ms
}

for(pos = 180; pos>=1; pos-=1) // cuando llega a 180, hace un
// barrido hasta 0
{
myservo.write(pos); // ordena al servo que se mueva
delay(20); // espera 20 ms para cambiar de posición
}
}
