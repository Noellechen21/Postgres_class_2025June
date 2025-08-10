import argparse
import random
## 以下是結構化後的程式，未結構化的請見lesson9_2修改為結構化程式.py

def get_user_name()->str:
    parser = argparse.ArgumentParser(description="猜數字遊戲")
    parser.add_argument("-n","--name",type=str,help="姓名")
    parser.add_argument("-f","--frequency",type=int,help="玩的次數",default=1)
    args = parser.parse_args()

    if not args.name:
        name = input("請輸入您的姓名:")
    else:
        name = args.name

    return name
# ->None 是型別提醒，可以不用寫
#(name : str) str是type hint可以不寫
#每一行可以用AI寫說明(這段AI寫不好，就沒放)
def play_game(name:str)->None:
    print(f"========猜數字遊戲第{i+1}次=========\n\n")
    min = 1
    max = 100
    count = 0
    target = random.randint(min,max)
    print(target)
    while(True):
        keyin = int(input(f"猜數字範圍{min}~{max}:"))
        count += 1
        if(keyin>=min and keyin<=max):
            if target == keyin:
                print(f"賓果!猜對了, 答案是:{target}")
                print(f"{name}共猜了{count}次\n")
                break
            elif(keyin > target):
                print(f"猜錯了!再小一點")
                max = keyin - 1
            else:
                print(f"猜錯了!再大一點")
                min = keyin + 1
            print(f"{name}已經猜{count}次\n")
        else:
            print("請輸入提示範圍內的數字\n")

def main():
    frequency = 1
    #呼叫get_user_name()
    name = get_user_name()
    for i in range(frequency):
        play_game(name)  #把def play_game的name這引數值帶入
    print(f"遊戲結束,{name}共玩了{frequency}次")

if __name__ == '__main__':
    main()