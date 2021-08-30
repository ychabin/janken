import random

print("ジャンケン開始")

hands = { 0: "グー", 1: "チョキ", 2: "パー"}

print("グー：0 チョキ：1 パー：2")

count = 0

while count < 3:

  your_hand = int(input())

  cpu_hand = random.randint(0,2)

  print("あなたは" + hands[your_hand] + "を出しました")

  print("相手は" + hands[cpu_hand] + "を出しました")

  def is_draw(your_hand: int, cpu_hand: int) -> bool:
    if your_hand == 0 and cpu_hand == 0 or your_hand == 1 and cpu_hand == 1 or your_hand == 2 and cpu_hand == 2:
      return True

  def is_lose(your_hand: int, cpu_hand: int) -> bool:
    if your_hand == 0 and cpu_hand == 2 or your_hand == 1 and cpu_hand == 0 or your_hand == 2 and cpu_hand == 1:
      return True

  if is_draw(your_hand, cpu_hand):
    print("引き分け")

  elif is_lose(your_hand, cpu_hand):
    print("負け")

  else:
    print("勝ち")
    count += 1
    print("現在の勝ち点" + str(count))

    if count == 3:
      print("3勝しました。終了です。")