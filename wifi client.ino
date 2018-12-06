#include <WiFi.h>
 
const char* ssid = "group2";
const char* password =  "9oW8524,";
 
const uint16_t port = 5005;
const char * host = "192.168.137.1";
 
void setup()
{
 
  Serial.begin(115200);
 
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("...");
  }
 
  Serial.print("WiFi connected with IP: ");
  Serial.println(WiFi.localIP());
 
}
 
void loop()
{
    WiFiClient client;
 
    if (!client.connect(host, port)) {
 
        Serial.println("Connection to host failed");
 
        delay(1000);
        return;
    }
 
    Serial.println("Connected to server successful!");
 
    client.print("MAC addresss");
 
    Serial.println("Disconnecting...");
    client.stop();
 
    delay(10000);
}
