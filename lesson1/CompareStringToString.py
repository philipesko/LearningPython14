def compareStr (a, b):
        if type(a) is str and type(b) is str:
            print(0)
            if a == b:
                print(1)
            elif len(a) > len(b) and not a == b:
                print(2)
            elif b == 'learn' and not a == b:
                print(3)
        else: print("This is not string!")

        print('------')



compareStr('test', 'learn')
compareStr(int(12), int(123))
compareStr('test', 'test')
compareStr('kokoko', '12б')
compareStr(13, 14)




