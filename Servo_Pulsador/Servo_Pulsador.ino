#include <Servo.h>

// Practica 3: un paso de 5 grados por cada pulsacion.
// Pulsador entre D4 y GND; senal del servo en D9.
// INPUT_PULLUP: pulsado = LOW; suelto = HIGH.

const byte PIN_PULSADOR = 4;
const byte PIN_SERVO = 9;
const unsigned long ANTIRREBOTE_MS = 30;

Servo servo;
int posicion = 0;
int paso = 5;
int ultimaLectura = HIGH;
int estadoEstable = HIGH;
unsigned long ultimoCambio = 0;

void setup() {
  pinMode(PIN_PULSADOR, INPUT_PULLUP);

  // Fija el objetivo inicial antes de activar la senal del servo.
  servo.write(posicion);
  servo.attach(PIN_SERVO);

  // Si arranca con el boton pulsado, espera a soltarlo y pulsar de nuevo.
  ultimaLectura = digitalRead(PIN_PULSADOR);
  estadoEstable = ultimaLectura;
  ultimoCambio = millis();
}

void loop() {
  const int lectura = digitalRead(PIN_PULSADOR);
  const unsigned long ahora = millis();

  if (lectura != ultimaLectura) {
    ultimoCambio = ahora;
    ultimaLectura = lectura;
  }

  // Acepta un cambio solo si permanece estable durante 30 ms.
  if (ahora - ultimoCambio >= ANTIRREBOTE_MS && lectura != estadoEstable) {
    estadoEstable = lectura;

    // Solo actua al pulsar, no al soltar ni al mantener pulsado.
    if (estadoEstable == LOW) {
      posicion += paso;
      servo.write(posicion);

      if (posicion == 180) {
        paso = -5;
      } else if (posicion == 0) {
        paso = 5;
      }
    }
  }
}
