
import matplotlib.pyplot as plt
import numpy as np
iterations = []
for i in range(20):
    iterations.append(i)

plt.title('Loss')

plt.plot(iterations, iterations, color='cyan',label='loss_train50w_0.01_v2')

plt.legend()  #显示上面的label
plt.xlabel('Iteration')
plt.ylabel('Loss')
from datetime import datetime
dt01 = datetime.today()

plt.savefig('imgs/'+str(dt01.day)+str(dt01.hour)+str(dt01.minute))

plt.show()
