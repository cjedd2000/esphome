#include "esphome/core/log.h"
#include "htzsafe_owl_alarm.h"

#include <esp_timer.h>


namespace esphome {
namespace htzsafe_owl_alarm {

static const char *TAG = "htzsafe_owl_alarm.component";

/*******************************************************************
* Private Function Prototypes
*******************************************************************/
uint32_t millis();

uint32_t millis() {
  return esp_timer_get_time() / 1000;
}

void HtzsafeOwlAlarm::setup() {
  ESP_LOGI(TAG, "Setup Complete");
}

void HtzsafeOwlAlarm::dump_config() {
    ESP_LOGCONFIG(TAG, "HTZSAFE Owl Sensor");
}

void HtzsafeOwlAlarm::loop() {
  if(millis() - StartTime > 5000) {
    StartTime = millis();
    ESP_LOGI(TAG, "Test Log");
  }
}

void HtzsafeOwlAlarm::parse_data() {
  // Example parsing method
  // Translates data received into buffer_data_ and stores it in parsed_value_ for publishing
}

}  // namespace htzsafe_owl_alarm
}  // namespace esphome
