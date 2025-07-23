import esphome.codegen as cg
from esphome.components import sensor, uart
import esphome.config_validation as cv
from esphome.const import CONF_ID, ICON_EMPTY

DEPENDENCIES = ["uart"]
AUTO_LOAD = ["sensor"]

LAST_ID = "last_id"

htzsafe_owl_alarm_ns = cg.esphome_ns.namespace("htzsafe_owl_alarm")
HtzsafeOwlAlarm = htzsafe_owl_alarm_ns.class_(
    "HtzsafeOwlAlarm", cg.Component, uart.UARTDevice
)

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(HtzsafeOwlAlarm),
            cv.Optional(LAST_ID): sensor.sensor_schema(
                icon=ICON_EMPTY, accuracy_decimals=0
            ),
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
    .extend(uart.UART_DEVICE_SCHEMA)
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)
    if LAST_ID in config:
        sens = await sensor.new_sensor(config[LAST_ID])
        cg.add(var.set_last_id_sensor(sens))
