import requests

if __name__ == "__main__":
    requests.post('http://localhost:5000/set_device', files={'file': open('test_files/test_device_1.json', 'rb')})
    requests.post('http://localhost:5000/set_device', files={'file': open('test_files/test_device_2.json', 'rb')})

    r = requests.get("http://localhost:5000/get_table")
    if r.content == b'[{"attributes":"[{\'is_input\': True, \'is_output\': True, \'lower_limit\': 10, \'name\': \'sometest1\', \'upper_limit\': 100, \'var_type\': \'float\', \'variable\': True}, {\'is_input\': False, \'is_output\': False, \'lower_limit\': 10, \'name\': \'sometest2\', \'upper_limit\': 15, \'var_type\': \'float\', \'variable\': True}]","id":1,"name":"someone"},{"attributes":"[{\'is_input\': True, \'is_output\': False, \'lower_limit\': 10, \'name\': \'newone\', \'upper_limit\': 1000, \'var_type\': \'int\', \'variable\': False}, {\'is_input\': False, \'is_output\': False, \'lower_limit\': 10, \'name\': \'sometest2\', \'upper_limit\': 15, \'var_type\': \'float\', \'variable\': True}]","id":2,"name":"better than someone"}]':
        print("test 1 passed")
    
    requests.post('http://localhost:5000/del_by_id/1')
    r = requests.get("http://localhost:5000/get_table")
    if r.content == b'[{"attributes":"[{\'is_input\': True, \'is_output\': False, \'lower_limit\': 10, \'name\': \'newone\', \'upper_limit\': 1000, \'var_type\': \'int\', \'variable\': False}, {\'is_input\': False, \'is_output\': False, \'lower_limit\': 10, \'name\': \'sometest2\', \'upper_limit\': 15, \'var_type\': \'float\', \'variable\': True}]","id":2,"name":"better than someone"}]':
        print("test 2 passed")
    
    requests.post('http://localhost:5000/del_by_id/2')
    r = requests.get("http://localhost:5000/get_table")
    print(r.content, "cleaned all data")
