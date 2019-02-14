class Img:
    def __init__(self,r,c):
        self.c=c
        self.r=r
        self.img=[0 for i in range(r*c)]
    def s(self,r,c,v):
        self.img[c+r*self.c]=v
    def ln(self,rs,cs,rf,cf,v):
        dr=abs(rf-rs)
        dc=abs(cf-cs)
        if rs==rf and cs==cf:
            self.s(rs,cs,v)
        elif rs>rf if dr<dc else cs>cf:
            self.ln(rf,cf,rs,cs,v)
        elif dr<dc:
            rr=2*dr-dc
            for c in range(cs,cf-1 if cs>cf else cf+1,-1 if cs>cf else 1):
                self.s(rs,c,v)
                rs+=1 if rr>0 else 0
                rr+=2*dr-2*dc if rr>0 else 2*dr
        else:
            rr=2*dc-dr
            for r in range(rs,rf-1 if rs>rf else rf+1,-1 if rs>rf else 1):
                self.s(r,cs,v)
                cs+=1 if rr>0 else 0
                rr+=2*dc-2*dr if rr>0 else 2*dc
    def __str__(self):
        txt = "P3 "+str(self.c)+" "+str(self.r)+" 255\n"
        for i in self.img:
            txt+=str(i/65536)+" "+str(i/256%256)+" "+str(i/256)+" "
        return txt

class Etrx:
    def __init__(self):
        self.m=[]
    def e(self,s):
        for i in (*s,1):
            self.m.append(i)
    def __str__(self):
        txt=""
        for i in range(4):
            for j in range(0,len(self.m),4):
                txt+=("  " if self.m[i+j]<10 else " " if self.m[i+j]<100 else "") + str(self.m[i+j])+" "
            txt+="\n"
        return txt
    def x(self,m):
        tmp=self.m[:]
        for i in range(len(self.m)):
            tmp[i]=sum(self.m[i-i%4+k]*m[4*i%4+k] for k in range(4))
        self.m=tmp
if __name__ == "__main__":
    a = Etrx()
    a.e((30,20,0))
    a.e((40,50,0))
    a.e((60,10,0))
    print(a)
    a.x((1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1))
    print(a)
