def main():
    scores = {'lily' : 18 , 'lucy' : 20, 'cindy' : 33}
    #通过键可以获取字典中对应的值
    print(scores['lily'])
    print(scores['lucy'])
    #对字典进行遍历（便利的其实是键再通过键取对应的值）
    for elem in scores:
        print('%s\t---t\t%d' % (elem, scores[elem]))
        #更新字典中的元素
    scores['lucy'] = 25
    scores['cindy'] = 90
    scores.update(luna = 22 , kitty = 30 )
    print(scores)
    if 'lea' in scores:
        print(scores['lea'])
    print(scores.get('lea'))
    #get方法也是通过键获取对应的值但是可以设置默认值
    print(scores.get('lea' , 60))
    #删除字典中的元素
    print(scores.pop('lea',60))
    print(scores.popitem())
    print(scores.pop('lily' , 18 ))
    #清空字典
    scores.clear()
    print(scores)

if __name__ == '__main__':
    main()