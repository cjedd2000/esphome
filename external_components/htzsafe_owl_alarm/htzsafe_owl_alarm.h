#pragma once

#include "esphome/core/component.h"
#include "esphome/components/uart/uart.h"

#include <esp_timer.h>

namespace esphome {
namespace htzsafe_owl_alarm {

static const uint8_t MAX_LINE_LENGTH = 8;  // Max characters for serial buffer

class HtzsafeOwlAlarm : public Component, public uart::UARTDevice {
 public:
  void setup() override;
  void loop() override;
  void dump_config() override;

 protected:
  void parse_data();  // A method to parse the data read from the sensor hardware

  uint8_t buffer_data_[MAX_LINE_LENGTH];
  float parsed_value_{0.0f};  // Parsed value to be published

 private:
  uint32_t StartTime { 0 };
};

}  // namespace htzsafe_owl_alarm
}  // namespace esphome
