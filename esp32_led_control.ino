#include <WiFi.h>

const char* ssid = "YOUR_WIFI_NAME";
const char* password = "YOUR_WIFI_PASSWORD";

WiFiServer server(80);

#define LED1 23
#define LED2 22
#define LED3 21
#define LED4 19

void setup() {

  Serial.begin(115200);

  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);

  digitalWrite(LED1, LOW);
  digitalWrite(LED2, LOW);
  digitalWrite(LED3, LOW);
  digitalWrite(LED4, LOW);

  WiFi.begin(ssid, password);

  Serial.print("Connecting");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi Connected");
  Serial.print("ESP32 IP: ");
  Serial.println(WiFi.localIP());

  server.begin();
}

void loop() {

  WiFiClient client = server.available();

  if (!client) {
    return;
  }

  String request = client.readStringUntil('\r');

  Serial.println(request);

  if (request.indexOf("/1") != -1) {
    digitalWrite(LED1, HIGH);
  }

  if (request.indexOf("/2") != -1) {
    digitalWrite(LED2, HIGH);
  }

  if (request.indexOf("/3") != -1) {
    digitalWrite(LED3, HIGH);
  }

  if (request.indexOf("/4") != -1) {
    digitalWrite(LED4, HIGH);
  }

  if (request.indexOf("/off") != -1) {
    digitalWrite(LED1, LOW);
    digitalWrite(LED2, LOW);
    digitalWrite(LED3, LOW);
    digitalWrite(LED4, LOW);
  }

  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type:text/html");
  client.println("Connection: close");
  client.println();

  client.stop();
}