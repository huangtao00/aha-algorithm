def myfun(a,**args):
    print (a)
    if "b" in args:
        print ("ok")
    print (args)


myfun(a=3,b=3,c=5)
