#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/uart/uart.h"

#include <esp_timer.h>

namespace esphome {
namespace htzsafe_owl_alarm {

class HtzsafeOwlAlarm : public Component, public uart::UARTDevice {
 public:
  void setup() override;
  void loop() override;
  void dump_config() override;

  void set_last_id_sensor(sensor::Sensor *sensor) { this->LastSensorId = sensor; }

 protected:
  sensor::Sensor *LastSensorId{nullptr};
};

}  // namespace htzsafe_owl_alarm
}  // namespace esphome
