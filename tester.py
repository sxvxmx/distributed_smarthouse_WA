import requests
import yaml

if __name__ == "__main__":
    requests.post('http://localhost:5000/set_device', files={'file': open('test_files/test_device_1.json', 'rb')})
    requests.post('http://localhost:5000/set_device', files={'file': open('test_files/test_device_2.json', 'rb')})
    r = requests.get("http://localhost:5000/get_var")
    print(r.content)