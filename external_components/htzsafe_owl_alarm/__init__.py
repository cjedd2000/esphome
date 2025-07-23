import esphome.codegen as cg
from esphome.components import binary_sensor, sensor, uart
import esphome.config_validation as cv
from esphome.const import CONF_ID, ICON_EMPTY, ICON_MOTION_SENSOR

DEPENDENCIES = ["uart"]
AUTO_LOAD = ["sensor", "binary_sensor"]

LAST_ID = "last_id"

# Temporary sensors for testing adding binary sensors
SEN1 = "sensor1"
SEN2 = "sensor2"

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
            cv.Optional(SEN1): binary_sensor.binary_sensor_schema(
                icon=ICON_MOTION_SENSOR
            ),
            cv.Optional(SEN2): binary_sensor.binary_sensor_schema(
                icon=ICON_MOTION_SENSOR
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

    if SEN1 in config:
        sens = await binary_sensor.new_binary_sensor(config[SEN1])
        cg.add(var.add_motion_sensor(sens, 64776))

    if SEN2 in config:
        sens = await binary_sensor.new_binary_sensor(config[SEN2])
        cg.add(var.add_motion_sensor(sens, 20236))
