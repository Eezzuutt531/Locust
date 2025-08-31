import os 

url = input("Masukan Url :")
uA = input("Total User :")
rA = input("User Per Detik :")
commads = f"python -m locust -f locusmain.py --host {url} -u {uA} -r {rA}"
os.system(f"{commads}")