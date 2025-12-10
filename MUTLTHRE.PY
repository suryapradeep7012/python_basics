def odd_number():
  for i in range(1,20,2):
    print("ODD :",i)
def even_number():
  for i in range(0,20,2):
    print("EVEN :",i)
import threading
tread_odd = threading.Thread(target=odd_number)
tread_even = threading.Thread(target=even_number)
tread_odd.start()
tread_even.start()
tread_odd.join()
tread_even.join()