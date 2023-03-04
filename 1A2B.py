import itertools as it
import random
from fun1A2B import listMatch, randomQuestion, possibleLst

level = int(input('請輸入遊戲數字長度１～９－－＞'))
question = randomQuestion(level)
lst = [i for i in range(10)]
possible = list(it.permutations(lst,level))

guess = []
count=0
while  guess!=question:
    guess = input('請輸入'+str(level) +'位數字－－＞')
    count+=1
    guess = [int(x) for x in guess] 
    if  guess ==question:       
        z = [str(o) for o in question] 
        ans = int("".join(z)) 
        print('恭喜!!!',level ,'A全對，你猜了',count,'次答案為：',ans)
    else:   
        result = listMatch(question,guess)
        a_count =result[0]
        b_count =result[1]
        print(a_count,'A',b_count,'B，加油！繼續努力。')
        possible = possibleLst(a_count,b_count,possible,guess)    
        print ("還剩下",len(possible),"種可能")
        print ("下次猜中機率為",round(100/len(possible),2),"%")


input("Press enter to exit ;)")
