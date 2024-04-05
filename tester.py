import requests

if __name__ == "__main__":
    requests.post('http://localhost:5000/set_config', files={'file': open('configs/test_config_1.json', 'rb')})
    requests.post('http://localhost:5000/set_config', files={'file': open('configs/test_config_2.json', 'rb')})

    requests.post('http://localhost:5000/set_device', files={'file': open('devices/test_device_1.json', 'rb')})
    requests.post('http://localhost:5000/set_device', files={'file': open('devices/test_device_2.json', 'rb')})
    requests.post('http://localhost:5000/set_device', files={'file': open('devices/test_device_3.json', 'rb')})

    r = requests.get('http://localhost:5000/get_table/devices')
    print(r.content)
