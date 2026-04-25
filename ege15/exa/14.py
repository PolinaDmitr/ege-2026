# ¬(x ∈ A) → ((x ∈ T) ≡ (x ∈ S))

def f(x, a1, a2):
    return (not (a1 <= x <= a2)) <= ((223 <= x <= 260) == (280 <= x <= 514))


k = []
for a1 in range(200, 550):
    for a2 in range(a1 + 1, 551):
        if all(f(x / 2, a1, a2) for x in range(400, 1200)):
            print(a1, a2)
            k.append((a2 - a1, a1, a2))

print(min(k))