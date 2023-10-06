import requests
import yaml

if __name__ == "__main__":
    requests.post('http://localhost:5000/set_base_item/attributes', files={'file': open('test_files/data2.yaml', 'rb')})
    r = requests.get("http://localhost:5000/get_base/attributes")
    print(r.content)