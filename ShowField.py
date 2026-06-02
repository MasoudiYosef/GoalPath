import matplotlib.pyplot as plt
import matplotlib.patches as patches
w=80
h=50
r=7.13
fig, ax = plt.subplots(figsize=(w/10,h/10))
rect=patches.Rectangle((0, 0), w, h, linewidth=4, edgecolor='black', facecolor="#e9ecde")
ax.add_patch(rect)
circ=patches.Circle((w/2, h/2), r, linewidth=2, edgecolor='black', facecolor='none')
ax.add_patch(circ)
circ=patches.Circle((9.14, h/2), r, linewidth=2, edgecolor='black', facecolor='none')
ax.add_patch(circ)
rect=patches.Rectangle((0, 14.1), 10.9, 21.8, linewidth=2, edgecolor='black', facecolor='#e9ecde')
ax.add_patch(rect)
circ=patches.Circle((w-9.14, h/2), r, linewidth=2, edgecolor='black', facecolor='none')
ax.add_patch(circ)
rect=patches.Rectangle((w-10.9, 14.1), 10.9, 21.8, linewidth=2, edgecolor='black', facecolor='#e9ecde')
ax.add_patch(rect)
plt.xlim([0,w])
plt.ylim([0,h])
plt.axis('off')
plt.arrow(w/2,0,0,h)
plt.savefig('Field.jpg',dpi=800)
for i in range(round(w/10),90,round(w/10)):
   plt.arrow(i,0,0,h,linewidth=0.3,color='r') 
for i in range(round(h/5),50,round(h/5)):
   plt.arrow(0,i,w,0,linewidth=0.3,color='r') 
C=1
for i in range(0,90-round(w/5),round(w/10)):
   for j in range(0,51-round(h/5),round(h/5)):
      plt.text(i+round(w/20)-1,j+2,str(C),color='blue')
      C=C+1
plt.savefig('DividedField.jpg',dpi=800)
plt.show()