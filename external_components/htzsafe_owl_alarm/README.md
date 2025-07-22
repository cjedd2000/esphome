```yaml
# example configuration:

esphome:
  name: htzsafe-owl-alarm-dev
  build_path: build/htzsafe_owl_alarm_dev

htzsafe_owl_alarm:
  id: OwlAlarm
  uart_id: OwlUart

uart:
  id: OwlUart
  tx_pin: 17
  rx_pin: 16
  baud_rate: 9600

```
