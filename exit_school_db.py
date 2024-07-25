import time
import pymssql # type: ignore
from azure.iot.device import IoTHubDeviceClient, Message # type: ignore

# SQL Server connection details
server = 'your_sql_server.database.windows.net'
database = 'your_database'
username = 'your_username'
password = 'your_password'

# IoT Hub connection string
iot_hub_connection_string = "HostName=your-iothub.azure-devices.net;DeviceId=your_device_id;SharedAccessKey=your_device_key"

# Connect to the IoT Hub
client = IoTHubDeviceClient.create_from_connection_string(iot_hub_connection_string)

def get_student_tags():
    # Connect to the SQL Server
    conn = pymssql.connect(server, username, password, database)
    cursor = conn.cursor()
    cursor.execute("SELECT StudentID, TagID FROM StudentTags")
    rows = cursor.fetchall()
    conn.close()
    return rows

def simulate_car_passing(student_id, tag_id):
    message = Message(f"Car with StudentID: {student_id} and TagID: {tag_id} is passing.")
    client.send_message(message)
    print(f"Sent message: {message}")

def main():
    while True:
        student_tags = get_student_tags()
        for student_id, tag_id in student_tags:
            simulate_car_passing(student_id, tag_id)
            time.sleep(30)

if __name__ == "__main__":
    main()
