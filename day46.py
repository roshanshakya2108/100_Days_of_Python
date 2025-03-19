import os

if(not os.path.exists("Data")):
    os.mkdir("Data")

for i in range(1,10):
    os.rename(f"Data/Tutoril {i}",f"Data/Tutorial {i}",)