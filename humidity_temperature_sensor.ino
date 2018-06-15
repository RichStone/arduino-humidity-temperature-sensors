#include <dht.h>

dht DHT;

#define DHT11_PIN 7
IPAddress server(10,0,0,138);

void setup(){
  Serial.begin(9600);
    
  if (client.connect(server, 80)) {
    client.println("POST /Api/AddParking/3 HTTP/1.1");
    client.println("Host: 10.0.0.138");
    client.println("User-Agent: Arduino/1.0");
    client.println("Connection: close");
    client.print("Content-Length: ");
    client.println(PostData.length());
    client.println();
    client.println(PostData);
  }
}

void loop()
{
  int chk = DHT.read11(DHT11_PIN);
  Serial.print("Temperature = ");
  Serial.println(DHT.temperature);
  Serial.print("Humidity = ");
  Serial.println(DHT.humidity);
  delay(1000);
}
