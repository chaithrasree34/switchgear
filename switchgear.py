# switchgear
# Simple Switchgear Protection Program

VOLTAGE_MIN = 200
VOLTAGE_MAX = 250
CURRENT_MAX = 100

breaker_status = "OFF"


def check_protection(voltage, current):
    global breaker_status

    print(f"\nVoltage : {voltage} V")
    print(f"Current : {current} A")

    if voltage < VOLTAGE_MIN:
        print("FAULT: Under-voltage detected")
        breaker_status = "TRIPPED"

    elif voltage > VOLTAGE_MAX:
        print("FAULT: Over-voltage detected")
        breaker_status = "TRIPPED"

    elif current > CURRENT_MAX:
        print("FAULT: Over-current detected")
        breaker_status = "TRIPPED"

    else:
        breaker_status = "ON"
        print("System healthy")


def main():
    print("=== SWITCHGEAR PROTECTION SYSTEM ===")

    voltage = float(input("Enter voltage (V): "))
    current = float(input("Enter current (A): "))

    check_protection(voltage, current)

    print(f"Breaker Status: {breaker_status}")


if __name__ == "__main__":
    main()
