#散列表用于防止重复
voted = {}  #创建一个散列表记录已经投票的人

def check_voted(name):
    if voted.get(name):  #名字已经在列表中
        print("kick them out")
    else:
        voted[name] = True  #将投票的人记录在表中
        print("let them vote")


check_voted("tom")
check_voted("lily")
check_voted("tom")