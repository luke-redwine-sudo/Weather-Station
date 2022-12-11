/* Example sketch to control a stepper motor with TB6600 stepper motor driver and Arduino without a library: number of revolutions, speed and direction. More info: https://www.makerguides.com */

// Define stepper motor connections and steps per revolution:
#define dirPin 5
#define stepPin 8
#define stepsPerRevolution 1600
#define windVaneIn A1
#define UVin A0

#define Offset 0;

int data = 0;
int VaneValue;
int Direction;
int LastValue;

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

  VaneValue = analogRead(windVaneIn);

   // Only update the display if change greater than 2 degrees.
  if(abs(VaneValue - LastValue) > 8)
  {
    Direction = getHeading(VaneValue);
    LastValue = VaneValue;
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
    else if ((request) == "68")
    {
      Serial.write(Direction&0xFF);
    }
    
  }
}

// Converts compass direction to heading
int getHeading(int direction) {
  if(direction > 460 and direction < 470)
    return 0;
  else if (direction > 400 and direction < 415)
    return 22.5;
  else if (direction > 785 and direction < 795)
    return 45;
  else if (direction > 765 and direction < 775)
    return 67.5;
  else if (direction > 980 and direction < 990)
    return 90;
  else if (direction > 915 and direction < 925)
    return 112.5;
  else if (direction > 955 and direction < 970)
    return 135;
  else if (direction > 835 and direction < 845)
    return 157.5;
  else if (direction > 890 and direction < 905)
    return 180;
  else if (direction > 590 and direction < 605)
    return 202.5;
  else if (direction > 645 and direction < 660)
    return 225;
  else if (direction > 155 and direction < 165)
    return 247.5;
  else if (direction > 170 and direction < 185)
    return 290;
  else if (direction > 120 and direction < 135)
    return 312.5;
  else if (direction > 320 and direction < 335)
    return 325;
  else if (direction > 230 and direction < 240)
    return 347.5;
}
