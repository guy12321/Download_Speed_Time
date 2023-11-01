#Download time speed
import os

download_gb = float(input("Inserire dimensione (GB) del file da scaricare: "))
download_mb = download_gb*1024

actual_gb = float(input("Inserire dimensione (GB) già scaricati del file: "))
actual_mb = actual_gb*1024

speed = float(input("Inserire velocità di download (MB/s): "))

size = float(download_mb - actual_mb)

secondi = size / speed

ore = float(secondi / 3600)
minuti = float( (float(ore)-int(ore))*60 )
secondi = float( (float(minuti)-int(minuti))*60 )

print(f"\nIl download dovrebbe essere terminato in circa {int(ore)} ore, {int(minuti)} minuti, e {int(secondi)} secondi", end = '')
os.system("pause >nul")