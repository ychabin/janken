import random

print("ジャンケン開始")

print("グー：０、チョキ：１、パー：２")

your_hand = int(input("手を決めて下さい　：　"))

cpu = random.randint(0,2)

print("あなたの手は" + str(your_hand))

print("相手の手は" + str(cpu))

if your_hand == 0 and cpu == 0 or your_hand == 1 and cpu == 1 or your_hand == 2 and cpu == 2:
  print("引き分け")

elif your_hand == 0 and cpu == 2 or your_hand == 1 and cpu == 0 or your_hand == 2 or cpu == 1:
  print("負け")

else:
  print("勝ち")

