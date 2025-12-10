import threading
import time

def download_file(file):
  print(f"Downloading{file}...")
  time.sleep(2)
  print(f"{file}downloaded.")


files=["file1.txt","file2.txt","file3.txt"]
threads=[threading.Thread(target=download_file,args=(f,))for f in files]

for t in threads:
  t.start()

for t in threads:
  t.join()