def main():  #字符串操作
    str1 = 'hello , world!'
    #通过len函数计算字符串的长度
    print(len(str1))
    #获得字符串首字母大写的拷贝
    print(str1.capitalize())
    #获得字符串变大写后的拷贝
    print(str1.upper())
    #从字符串中差查找子串所在的位置
    print(str1.find('or'))
    print(str1.find('shit'))
    str2 = 'abc123456'
    #从字符串中取出指定位置的字符（下标运算）
    print(str2[2])
    #字符串切片（从指定的开始索引到指定的结束索引）
    print(str2[2:5])  # c12
    print(str2[2:])  # c123456
    print(str2[2::2])  #c246
    print(str2[::2])   #ac246
    print(str2[::-1])   #654321cba
    print(str2[-3:-1])  # 45
    str3 = '    jackfred@123.com'
    print(str3)
    #获得字符串修剪左右两侧空格的拷贝
    print(str3.strip())

if __name__=='__main__':
      main()