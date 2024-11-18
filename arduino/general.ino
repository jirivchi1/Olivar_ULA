#include "RTClib.h"
#include "LowPower.h"
#include <SoftwareSerial.h>

RTC_DS3231 rtc;
const int wakeUpPin = 2;
const int relayPin = 7;
unsigned long lastDebounceTime = 0;
const unsigned long debounceDelay = 200;

// Definición de pines y constantes
const int ldrA0 = A0;
const int ldrA1 = A1;

const float maxVoltage = 5.0;
const int maxADC = 1023;

// Define activation times
const byte NUM_ALARMAS = 4;
byte horasActivacion[NUM_ALARMAS] = {9, 12, 15, 18};
byte minutosActivacion[NUM_ALARMAS] = {00,00,00, 00};

// Pines de SoftwareSerial
const int rxPin = 1; // RX de SoftwareSerial (Recibe de Pi)
const int txPin = 0; // TX de SoftwareSerial (Envía a Pi)
SoftwareSerial mySerial(rxPin, txPin); // RX, TX

void setup() {

  pinMode(ldrA0, INPUT);
  pinMode(ldrA1, INPUT);

  Serial.begin(9600);
  mySerial.begin(9600);

  if (!rtc.begin()) {
    Serial.println("No se pudo encontrar el RTC");
    delay(5000);
    asm volatile ("jmp 0");
  }

  if (rtc.lostPower()) {
    rtc.adjust(DateTime(__DATE__, __TIME__));
  }

  rtc.disableAlarm(1);
  rtc.disableAlarm(2);
  rtc.clearAlarm(1);
  rtc.clearAlarm(2);
  rtc.writeSqwPinMode(DS3231_OFF);

  pinMode(wakeUpPin, INPUT_PULLUP);
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, LOW);

  configurarSiguienteAlarma();
}

void loop() {

  delay(500);
  attachInterrupt(digitalPinToInterrupt(wakeUpPin), wakeUp, LOW);
  LowPower.powerDown(SLEEP_FOREVER, ADC_OFF, BOD_OFF);
  detachInterrupt(digitalPinToInterrupt(wakeUpPin));

  activarRele();

  rtc.clearAlarm(1);
  configurarSiguienteAlarma();
}

void activarRele() {
    const unsigned long tiempoTotalReleEncendido = 240000;  // 4 minutos en milisegundos
    unsigned long inicioReleEncendido = millis();

    digitalWrite(relayPin, HIGH);  // Encender el relé (enciende la Raspberry Pi)

    while (millis() - inicioReleEncendido < tiempoTotalReleEncendido) {
        // Leer y calcular los voltajes de las baterías
        int sensorValueA1 = analogRead(ldrA1);
        float voltageA1 = ((sensorValueA1 * maxVoltage) / maxADC) * 2;
        int sensorValueA0 = analogRead(ldrA0);
        float voltageA0 = (((sensorValueA0 * maxVoltage) / maxADC) / 10) * 25;

        // Enviar los valores de voltaje a través de SoftwareSerial
        mySerial.print(voltageA0, 2);
        mySerial.print(",");
        mySerial.println(voltageA1, 2);

        Serial.print(voltageA0, 2);   // Enviar voltageA0 con 2 decimales

        Serial.print(",");            // Separador de valores
        Serial.println(voltageA1, 2); // Enviar voltageA1 con 2 decimales

        delay(1000);  // Esperar 500 ms entre cada envío de datos para evitar sobrecarga
    }

    digitalWrite(relayPin, LOW);  // Apagar el relé al finalizar los 3 minutos
}



void configurarSiguienteAlarma() {
  DateTime now = rtc.now();
  Serial.print(now.hour());
  Serial.print(":");
  Serial.println(now.minute());
  delay(500);

  for (int i = 0; i < NUM_ALARMAS; i++) {
    if (now.hour() < horasActivacion[i] || (now.hour() == horasActivacion[i] && now.minute() < minutosActivacion[i])) {
      rtc.setAlarm1(DateTime(0, 0, 0, horasActivacion[i], minutosActivacion[i], 0), DS3231_A1_Hour);
      Serial.print("Alarma establecida para: ");
      Serial.print(horasActivacion[i]);
      Serial.print(":");
      Serial.println(minutosActivacion[i]);
      return;
    }
  }
  rtc.setAlarm1(DateTime(0, 0, 0, horasActivacion[0], minutosActivacion[0], 0), DS3231_A1_Hour);
  Serial.print("Alarma establecida para mañana a las: ");
  Serial.print(horasActivacion[0]);
  Serial.print(":");
  Serial.println(minutosActivacion[0]);
}

void wakeUp() {
  unsigned long currentTime = millis();
  if ((currentTime - lastDebounceTime) > debounceDelay) {
    lastDebounceTime = currentTime;
  }
}