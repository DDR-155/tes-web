import time

def timer(seconds):
    while seconds > 0:
        print(f"Time left: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# Masukkan jumlah detik untuk timer
seconds = int(input("Masukkan jumlah detik: "))
timer(seconds)
