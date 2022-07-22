#outer design
c1=circle(r=150,fill="black",stroke_width="5")

e1 = ellipse(w=300,h=60,fill="purple",stroke_width="none",stroke="none")|repeat(30,rotate(10))

r1=rectangle(h=205,w=205,stroke="none",fill="#800000")|rotate(5)|repeat(18,rotate(10))
r2=rectangle(h=189.5,w=189.5,fill="#b30000",stroke="none")|rotate(0)|repeat(18,rotate(10))
r3=rectangle(h=175,w=175,stroke="none",fill="#cc3300")|rotate(5)|repeat(18,rotate(10))
r4=rectangle(h=161.5,w=161.5,stroke="none",fill="#ff471a")|rotate(0)|repeat(18,rotate(10))
r5=rectangle(h=155,w=155,stroke="none",fill="#ffa500")|rotate(5)|repeat(18,rotate(10))
r6=rectangle(h=150,w=150,stroke="none",fill="#ffbb33")|rotate(0)|repeat(18,rotate(10))
r7=rectangle(h=140,w=140,stroke="none",fill="#ffcc66")|rotate(5)|repeat(18,rotate(10))
r8=rectangle(h=130,w=130,stroke="none",fill="#ffb888",stroke_width=5)|rotate(5)|repeat(18,rotate(10))

show(c1,e1,r1,r2,r3,r4,r5,r6,r7,r8)

#inner design

#1 sun
r9=rectangle(h=115,w=110,stroke="none",fill="#ffb380")|rotate(0) | repeat(9,rotate(30))
r10=rectangle(h=105,w=105,stroke="none",fill="#ffae78")|rotate(15) | repeat(9,rotate(30))
r11=rectangle(h=95,w=95,stroke="none",fill="#ffa970")|rotate(0) | repeat(9,rotate(30))
r12=rectangle(h=85,w=85,stroke="none",fill="#ffa468")|rotate(15) | repeat(9,rotate(30))
r13=rectangle(h=75,w=75,stroke="none",fill="#ffa05f")|rotate(0) | repeat(9,rotate(30))
r14=rectangle(h=65,w=65,stroke="none",fill="#ff9b57")|rotate(15) | repeat(9,rotate(30))
r15=rectangle(h=55,w=55,stroke="none",fill="#ff964f")|rotate(0) | repeat(9,rotate(30))
r16=rectangle(h=45,w=45,stroke="none",fill="#ff9147")|rotate(15) | repeat(9,rotate(30))

sun=circle(r=20,fill="yellow",stroke="none")|scale(x=-1)
sun1= circle(r=10,fill="#ffff80",stroke="none")
sun2= circle(r=5,fill="#ffff99",stroke="none")

show(r9,r10,r11,r12,r13,r14,r15,r16,sun,sun1,sun2)

#2 water
p14=point(-83,-23)
p15=point(84,-23)
p16=point(60,-60)
p17=point(45,-70)
p18=point(12,-85)
p19=point(-35,-80)
p20=point(-57,-65)
watercolor=polygon([p14,p15,p16,p17,p18,p19,p20],fill="#66b3ff",stroke="#cce6ff")

water1=ellipse(w=25,h=10,fill="#66b3ff",stroke="#cce6ff")|translate(x=5,y=5)
water11=water1|repeat(12,rotate(30))
w1=water11|translate(x=-61,y=-32)|repeat(6,rotate(25)) 

water2=ellipse(w=25,h=10,fill="#66b3ff",stroke="#cce6ff")|translate(x=5,y=5)
water21=water2|repeat(12,rotate(30))
w2=water21|translate(x=-30,y=-35)|repeat(5,rotate(20))

water3=ellipse(w=25,h=10,fill="#66b3ff",stroke="#cce6ff")|translate(x=5,y=5)
water31=water3|repeat(12,rotate(30))
w3=water31|translate(y=-39)

show(watercolor,w3,w2,w1)

#3 inner outline
c2= circle(r=85,stroke="#ac00e6",stroke_width="5",fill="")
show(c2)

#4 boat body
p1=point(73,-40)
p2=point(10,-50)
p3=point(-25,-30)
p4=point(-25,-50)
boatbase=polygon([p1,p2,p4,p3],fill="black")

boatside=circle(x=-25,y=-40,r=10,fill="black")|repeat(250,rotate(-0.2))

p5=point(-45,3)
p6=point(-56,-10)
p7=point(-62.7,3)
boattop=polygon([p5,p6,p7],fill="black")

show(boatbase,boatside,boattop)

#5 persons

#person1
c3=circle(fill="black",r=5,x=-15,y=-12)
p8=point(-25,-30)
p9=point(-10,-45)
p10=point(-15,-12)
person1=polygon([p8,p9,p10],fill="black")
l1=line(x1=5,y1=10,x2=-30,y2=-75)

#person2
c4=circle(fill="black",r=4,x=10,y=-20)
p11=point(0,-40)
p12=point(15,-40)
p13=point(10,-20)
person2=polygon([p11,p12,p13],fill="black")
l2=line(x1=25,y1=0,x2=0,y2=-60)

#person3
c5=circle(fill="black",r=3,x=30,y=-27)
p14=point(26,-34)
p15=point(34,-40)
p16=point(30,-27)
person3=polygon([p14,p15,p16],fill="black")

#person4
person4=circle(fill="black",r=2.5,x=45,y=-33)

#person5
person5=circle(fill="black",r=2,x=55,y=-35)

#person6
person6=circle(fill="black",r=1,x=65,y=-37)

#person7
person7=circle(fill="black",r=0.5,x=71,y=-38)

show(c3,person1,l1,c4,person2,l2,c5,person3,person4,person5,person6,person7)