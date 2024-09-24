print("="*40)
print("Tabung")
print("="*40)

R = float(input("Masukan jarijari"))
T = float(input("Masukan Tinggi"))

PHI = 3.14
V = PHI * R * R * R * T
LP = (2 * PHI * R * T) + (2 * (2 * PHI * R))

print("Volume:",V," cm2")
print("Luas Permukaan:",LP," cm")