import requests
from time import perf_counter

url = "https://httpbin.org/status/200"  


try:
    expected_status_code = (input("Enter the expected status code: ")) 
    if not expected_status_code.isdigit():
        raise ValueError("The expected status code must be a number in the range 100-599.")
    expected_status_code = int(expected_status_code)
    if not 100 <= expected_status_code <= 599:
        raise ValueError("The expected status code must be a number in the range 100-599.")
    start_time = perf_counter()
    response = requests.get(url, timeout=3)
    end_time = perf_counter()
    if response.status_code == expected_status_code:
        print("PASS: The status code matches the expected value.")
    else:
        print(f"FAIL: Expected {expected_status_code}, but got {response.status_code}")
    print(f"Execution time: {(end_time - start_time)*1000:.2f} ms")
except requests.exceptions.Timeout:
    print("The request timed out.")