# By MP3Martin @ https://github.com/MP3Martin/numbers-on-graph
# MIT licensed

import matplotlib.pyplot as plt
import input_num
# input_num.allow_update()
import math
import mplcursors
MODES = ["Fibonacci", "Pi", "Recamán's Sequence"]

plot_y = []
plot_x = []


print("- Select graph mode: -")
for mode in list(MODES):
  print("[" + str(MODES.index(mode)) + "]" + " " + mode)
print("")

mode = -1
def getMode():
  global mode
  mm = int(input_num("Mode: ", True, False))
  if mm > len(MODES) - 1 or mm < 0:
    print("\nError: Invalid mode!")
    getMode()
  else:
    mode = mm

getMode()
# print(mode)

print("")
COUNT = int(input_num("Number count: ", True, False))
if COUNT < 2:
    print("\nError: Minimally 2 numbers are required!")
    exit()
else:
  pass
count = int(COUNT)
print("\nLoading...\n")

if mode == 0:
  i = 2
  global fib
  fib = [0, 1]; # init array
  count = count + i
  plt.title('Fibonacci numbers on graph', fontsize=18)
  for i in range(i, count):
    # print(fib[i - 2])

    fib.insert(i, fib[i - 2] + fib[i - 1])
    plot_y.append(fib[i])
elif mode == 1:
  plt.title('Pi numbers on graph', fontsize=18)

  DIGITS = count

  def pi_digits(x):
      k,a,b,a1,b1 = 2,4,1,12,4
      while x > 0:
          p,q,k = k * k, 2 * k + 1, k + 1
          a,b,a1,b1 = a1, b1, p*a + q*a1, p*b + q*b1
          d,d1 = a/b, a1/b1
          while d == d1 and x > 0:
              yield int(d)
              x -= 1
              a,a1 = 10*(a % b), 10*(a1 % b1)
              d,d1 = a/b, a1/b1

  digits = [int(n) for n in list(pi_digits(DIGITS))]

  plot_y = list(digits)

  # plot_y.append(99)

  # if len(plot_y) >= count:
  #   plot_y = plot_y[0:count]
  #   # print(plot_y)
  # else:
  #   print("Error: Not enough numbers to plot!")
  #   exit()
elif mode == 2:
  plt.title('Recamán\'s sequence on graph', fontsize=18)
  R = [0]; [(R:= R + [R[-1]+x]) if R[-1]-x in R or R[-1] < x else (R := R + [R[-1]-x]) for x in range(1,count)]
  plot_y = list(R)



plot_x = list(range(len(plot_y)))
# plot_x = list(range(10))

# print(plot_y)
# print(plot_x)
plt.plot(plot_x, plot_y)
  
plt.xlabel('x', fontsize=18)
plt.ylabel('y', fontsize=18)

# function to show the plot
mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())
plt.gcf().canvas.set_window_title('Matplotlib - Python')

print("Loaded!")

def show_datapoints(sel):
  xi, yi = sel[0], sel[0]
  xi, yi = xi._xorig.tolist(), yi._yorig.tolist()
  # print(xi[int(round(sel.target.index))])
  # exit()
  sel.annotation.set_text('y: '+ str(yi[int(round(sel.index))])) # +'\n'+ 'y: '+ str(yi[int(round(sel.target.index))])

  mplcursors.cursor(hover=True).connect('add',show_datapoints)

# print(plot_y)

plt.show()