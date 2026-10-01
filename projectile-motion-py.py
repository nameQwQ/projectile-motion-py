import math
g=9.8
v0=float(input("输入初速度m/s:"))
angle=float(input("输入抛射角度(角度):"))
#角度转弧度，math三角函数用弧度
theta=math.radians(angle)
vx=v0*math.cos(theta)
vy0=v0*math.cos(theta)
#飞行总时间(落回原高度)
t_total=2*vy0/g
max_height=vy0**2/(2*g)
range_x=vx*t_total
print(f"总飞行时间:{t_total:.2f}s")
print(f"最大高度:{max_height:.2f}m")
print(f"水平射程:{range_x:.2f}m")
         
