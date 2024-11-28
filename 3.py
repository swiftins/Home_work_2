def bank(a,years):
  for _ in range(years):
    a += a * 0.1
  return round(a)
result = bank(100,10)
print(f"final amnt:{result}")