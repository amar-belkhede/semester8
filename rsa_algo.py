from decimal import Decimal


def gcb(a, b):
    if b == 0:
        return a
    else:
        return gcb(b, a % b)


p = int(input('enter the value for p: '))
q = int(input('enter the value for q: '))
no = int(input('enter the value for string: '))
n = p*q
t = (p-1)*(q-1)

for e in range(2, t):
    if gcb(e, t) == 1:
        break

for i in range(1, 10):
    x = 1+i*t
    if x % e == 0:
        d = int(x/e)
        break

ctt = Decimal(0)
ctt = pow(no, e)
ct = ctt % n

dtt = Decimal(0)
dtt = pow(ct, d)
dt = dtt % n

print('n = '+str(n)+' \ne = '+str(e)+' \nt = '+str(t)+' \nd = '+str(d) +
      ' \ncipher text = '+str(ct)+' \ndecrypted text = '+str(dt)+' \npubilc key: ('+str(e)+','+str(n)+') \nprivate key: ('+str(d)+','+str(n)+')')
