n = []
q = []

for i in range (0,10):
    n.append(float(input(f"Digite o {i+1}º número: ")))
    q.append(n[i]*n[i])

print("Números: ", n)
print("Quadrados: ", q)