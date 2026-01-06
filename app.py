# Nama : Muhammad Abdurrahman Ar-Rafif
# NPM : 24670042
# Kelas : Teknik Informatika - 3B

def minimum_change(amount, denominations):
  """
  Menghitung kembalian minimum menggunakan algoritma greedy.
  
  Args:
  - amount (int): Jumlah kembalian yang harus diberikan.
  - denominations (list): Daftar denominasi koin/uang (diurutkan otomatis).
  
  Returns:
  - dict: Breakdown koin dan total jumlah koin.
  """
  if amount <= 0:
    return {"total_coins": 0, "breakdown": {}}
  
  denominations = sorted(set(denominations), reverse=True)  # hapus duplicates & sort
  breakdown = {}
  total_coins = 0
  
  for denom in denominations:
    if amount >= denom:
      count = amount // denom
      breakdown[denom] = count
      total_coins += count
      amount -= count * denom
  
  return {"total_coins": total_coins, "breakdown": breakdown}


def display_result(result, currency="rupiah"):
  """Display the result in a formatted way."""
  print(f"\nJumlah koin minimum: {result['total_coins']}")
  print("Breakdown:")
  if result['breakdown']:
    for denom, count in result['breakdown'].items():
      print(f"  {denom} {currency}: {count} koin")
  else:
    print("  Tidak ada koin yang dibutuhkan")


def main():
  """Main function for user interaction."""
  denominations = [1000, 500, 100, 50, 25, 10, 5, 1]
  
  while True:
    try:
      amount = int(input("\nMasukkan jumlah kembalian (0 untuk keluar): "))
      if amount == 0:
        print("Terima kasih!")
        break
      
      result = minimum_change(amount, denominations)
      display_result(result)
    except ValueError:
      print("Input tidak valid. Masukkan angka bulat.")


if __name__ == "__main__":
  main()
