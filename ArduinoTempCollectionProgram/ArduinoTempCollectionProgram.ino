
const int temperaturePin = 0;  //Set to 0


void setup()
{
  
  Serial.begin(9600);    // Initiate Serial to record Data
}


void loop()
{

  float voltage, degreesC;

  voltage = getVoltage(temperaturePin); //Using Volt Potential to find temp

  degreesC = (voltage - 0.5) * 100.0;  //Convert Volts to celsius
  
  Serial.print(voltage);                      //Print Values
  Serial.print('\t');Serial.print(millis());
  Serial.print('\t'); Serial.println(degreesC);
  //Serial.print("  deg F: ");
  //Serial.println(degreesF);

   
  delay(50); // repeat once 50 milliseconds
}


float getVoltage(int pin)       //Getting Voltage Values and Converting
{

  
  return (analogRead(pin) * 0.004882814);

}
