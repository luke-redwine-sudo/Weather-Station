/* Example sketch to control a stepper motor with TB6600 stepper motor driver and Arduino without a library: number of revolutions, speed and direction. More info: https://www.makerguides.com */

// Define stepper motor connections and steps per revolution:
#define dirPin 5
#define stepPin 8
#define stepsPerRevolution 1600

int UVin = A0;

int data = 0;

uint8_t stepPinOut = HIGH;

unsigned long delayInterval = 0;

String request = "";

uint8_t response;

void setup() {

  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);

  // Declare pins as output:
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(UVin, INPUT);

  // Set the spinning direction counterclockwise:
  digitalWrite(dirPin, LOW);

  delayInterval = millis();
}

void loop() {

  if ((millis() - delayInterval) >= 300)
  {
    if (stepPinOut == HIGH)
    {
      stepPinOut = LOW;
    }
    else
    {
      stepPinOut = HIGH;
    }

    delayInterval = millis();

    digitalWrite(stepPin, stepPinOut);
  }

  if (Serial.available() > 0)
  {
    request = (Serial.read());

    if (request == "85")
    {
      Serial.write(analogRead(UVin)&0xFF);
    }
    else if (request == "84")
    {
      Serial.write("L");
    }
    else
    {
      Serial.write("N");
    }
    
  }
}
