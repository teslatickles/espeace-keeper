#include <Wifi.h>
#include <HTTPClient.h>

const char* ssid = "";
const char* pwd = "";

void setup() {
    Serial.begin(115200);

    WiFi.begin(ssid, pwd)

    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WaifuFaifu...");
    }

    Serial.println("Connected to WiFi network");
}

void loop() {
    if ((WiFi.status() == WL_CONNECTED)) {
        HTTPClient http;

        http.begin("http://192.xxx.x.xx:8090/button");
        int httpCode = http.GET();

        if (httpCode > 0) {
            String payload = http.getString();
            Serial.println(httpCode);
            Serial.println(payload);
        } else {
            Serial.println("Error during HTTP request!");
        }
        http.end();
    }
    delay(20000);
}
