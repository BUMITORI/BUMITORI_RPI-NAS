import serial

UART_PORT = "/dev/ttyACM0"
BAUD_RATE = 9600

try:
    ser = serial.Serial(UART_PORT, BAUD_RATE, timeout=1)
    print(f"UART 연결됨: {UART_PORT} (Baud: {BAUD_RATE})")

    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            print(f"STM32 → Raspberry Pi: {data}")

        user_input = input("Raspberry Pi → STM32: ")
        if user_input.lower() == "q":
            break

        ser.write((user_input).encode('utf-8'))

except serial.SerialException as e:
    print(f"시리얼 오류: {e}")

finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("UART 연결 종료됨")