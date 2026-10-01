trans, acc = map(float, input().split())

if trans % 5 == 0 and acc >= (trans + 0.50):
    acc -= trans + 0.50

print(f"{acc:.2f}")
