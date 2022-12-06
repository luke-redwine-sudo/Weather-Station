/* Example sketch to control a stepper motor with TB6600 stepper motor driver and Arduino without a library: number of revolutions, speed and direction. More info: https://www.makerguides.com */

// Define stepper motor connections and steps per revolution:
#define dirPin 5
#define stepPin 8
#define stepsPerRevolution 1600

void setup() {
  // Declare pins as output:
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
}

void loop() {
  // Set the spinning direction clockwise:
  digitalWrite(dirPin, HIGH);

  // Set the spinning direction counterclockwise:
  digitalWrite(dirPin, LOW);

  digitalWrite(stepPin, HIGH);
  delayMicroseconds(300);
  digitalWrite(stepPin, LOW);
  delayMicroseconds(300);

}