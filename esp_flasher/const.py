import re

__version__ = "1.4.1"

ESP32_DEFAULT_OTA_DATA = "boot_app0.bin"
ESP32_DEFAULT_BOOTLOADER_FORMAT = "bootloader_$FLASH_MODE$_$FLASH_FREQ$.bin"
ESP32_DEFAULT_PARTITIONS = "partitions.$MODEL$.$FLASH$.bin"

# https://stackoverflow.com/a/3809435/8924614
HTTP_REGEX = re.compile(
    r"https?://(www\.)?[-a-zA-Z0-9@:%._+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_+.~#?&/=]*)"
)
