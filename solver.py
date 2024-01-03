main_dict = {
   1 : "one",
   2 : "Two",
   3   : "Three"      ,
   4  :  "four"     ,
   5  :  "five"     ,
   6  :  "six"     ,
   7  :  "seven"     ,
   8  :  "eight"     ,
   9  :  "nine"     ,
   10  : "ten"      ,
   11  : "eleven"      ,
   12  : "twelve"      ,
   13  : "thirteen"      ,
   14  : "fourteen"      ,
   15  : "fifteen"      ,
   16  : "sixteen"      ,
   17  : "seventeen"      ,
   18  : "eighteen"      ,
   19  : "ninteen"      ,
   20  : "twenty"   ,
   30  : "thirty",
   40  : "fourty",
   50  : "fivety",
   60  : "sixty",
   70  : "sevety",
   80  : "eigthy",
   90  : "ninety",
   100  : "hundred",
   1000 : "thousand",
   100000  : "lakh",
   1000000  : "million",
   10000000 : "crore",
   1000000000 : "billion",

 }

def cal_words(num) :
    total = ""
    li = [ i for i in main_dict if i <= num]
    print(li)
    print(li[-2])
    
    i = 1
    divider = li[-i]
    while divider >=100 :
        
        start = num//divider
        end =  num%divider
        
        print("divider",divider ,"start = " , start , "end = " ,end)
        if start in main_dict :
                total += main_dict[start]+main_dict[divider]
        else :      
                val_n = start-(start%10)
                word = main_dict[val_n]+main_dict[start%10]

                total += word+ main_dict[divider]
        
        
        if len(str(end))== 2 :
            if end in main_dict :
                total += "and"+main_dict[end]
            else :      
                val = end-(end%10)
                total += "and"+main_dict[val]+ main_dict[end%10]            

        
        i+= 1
        divider = li[-i]
        num = end

    # print("start" ,start ,"end" ,end)
    print("total" ,total)
    print(divider)


def less_than_100(num) :
    if num in main_dict:
        return main_dict[num]
    else :    
        start = num - num%10 
        return main_dict[start] + main_dict[num%10]
    
# def solver():

         

 

if __name__ == "__main__" : 
#    print(solver())
  print(cal_words(3452266698))
  print(less_than_100(99))

#   345226668
