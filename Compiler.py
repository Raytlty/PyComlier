__author__ = 'Benco'
from Token import *
import re

if __name__ == '__main__':
    #all=re.compile('(\d+\.\d+[eE][-+]?\d+|\d+\.\d+|[1-9]\d*|0[0-7]+|0x[0-9a-fA-F]+|[a-zA-Z_]\w*|>>|<<|::|->|\.|\+=|\-=|\*=|/=|%=|>=|<=|==|!=|&&|\|\||\+|\-|\*|/|=|>|<|!|^|%|~|\?|:|,|;|\(|\)|\[|\]|\{|\}|\'|\")')
    #mth=all.findall('ROT IS 18')
    '''try:
        f=open('a.txt','r')
    except Exception:
        print("ERROR")
    finally:
        a=f.readlines()
        lens=0
        for i in a:
            lens+=len(i)
        #print(lens)
        while True:
            tokens=Token()
            tokens.CheckToken(f)
            #print(Token().pos)
            if tokens.key == None:
                continue
            print('< '+tokens.key,end=' ')
            for item in tokens.value:
                if item == sin:
                    print('sin',end=' ')
                    continue
                elif item == cos:
                    print('cos',end=' ')
                    continue
                elif item == log:
                    print('log',end=' ')
                    continue
                elif item == exp:
                    print('exp',end=' ')
                    continue
                elif item == sqrt:
                    print('sqrt',end=' ')
                    continue
                if isinstance(item,float):
                    print("%.6f"%item,end=' ')
                else:
                    print(item,end=' ')
            print('>')
            if Token().pos>lens:
                break
        f.close()'''