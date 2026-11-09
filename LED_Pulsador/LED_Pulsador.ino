// Practica 2.1: encender el LED mientras se mantiene pulsado el boton.
// Pulsador entre D4 y GND. LED integrado de un Arduino Uno en D13.
// INPUT_PULLUP: pulsado = LOW; suelto = HIGH.

const byte PIN_PULSADOR = 4;
const byte PIN_LED = 13;

void setup() {
  pinMode(PIN_LED, OUTPUT);
  digitalWrite(PIN_LED, LOW);
  pinMode(PIN_PULSADOR, INPUT_PULLUP);
}

void loop() {
  const bool pulsado = (digitalRead(PIN_PULSADOR) == LOW);
  digitalWrite(PIN_LED, pulsado ? HIGH : LOW);
}
