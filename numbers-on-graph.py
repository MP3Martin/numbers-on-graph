# By MP3Martin @ https://github.com/MP3Martin/numbers-on-graph
# MIT licensed
# Too lazy to rewrite this code

import matplotlib.pyplot as plt
import input_num
# input_num.allow_update()
import math
import mplcursors
import sys
from platform import system

args_list = list(sys.argv)[1:]
args = {"mode" : "", "ncount" : "", "data": ""}

def getData(text, data_type = str):
  if not args["data"]:
    if data_type == int:
      data_input = int(input_num(text, True, False))
    else:
      data_input = input(text)
    print("")
  else:
    data_input = args["data"]
  try:
    return data_type(data_input)
  except Exception:
    print(f"Error: Invalid type for the \"data\" arg (got {type(data_input).__name__}, expected {data_type.__name__})!")
    exit()
  
def setPltTitle(text):
  plt.title(text, fontsize=18)

for key in args:
  i = list(args.keys()).index(key)
  try:
    args_list[i]
  except Exception:
    pass
  else:
    args[key] = args_list[i]

MODES = ["Fibonacci", "Pi", "Recamán's Sequence", "Collatz conjecture"]

plot_y = []
plot_x = []

if not args["mode"]:
  print("- Select graph mode: -")
  for mode in list(MODES):
    print("[" + str(MODES.index(mode)) + "]" + " " + mode)
  print("")

mode = -1
def getMode():
  global mode
  if not args["mode"]:
    mode_input = int(input_num("Mode: ", True, False))
  else:
    try:
      mode_input = int(args["mode"])
    except Exception:
      if not args["mode"]:
        print("")
      print("Error: Mode must be integer!")
      exit()
  if mode_input > len(MODES) - 1 or mode_input < 0:
    if not args["mode"]:
        print("")
    print("Error: Invalid mode!")
    if args["mode"]:
      exit()
    getMode()
  else:
    mode = mode_input
    if not args["mode"]:
      print("")

getMode()

if not args["ncount"]:
  COUNT = int(input_num("Number count: ", True, False))
  print("")
else:
  try:
    COUNT = int(args["ncount"])
  except Exception:
    print("\nError: Number count must be integer!")
    exit()

if COUNT < 2:
  print("Error: Minimally 2 numbers are required!")
  exit()
count = int(COUNT)
if mode == 3:
  start = getData("Start from: ", int)
  
print("Loading...\n")

if mode == 0:
  i = 2
  global fib
  fib = [0, 1] # init array
  count = count + i
  setPltTitle('Fibonacci numbers on graph')
  for i in range(i, count):
    # print(fib[i - 2])

    fib.insert(i, fib[i - 2] + fib[i - 1])
    plot_y.append(fib[i])
elif mode == 1:
  setPltTitle('Pi numbers on graph')

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

elif mode == 2:
  setPltTitle('Recamán\'s sequence on graph')
  R = [0]; [(R:= R + [R[-1]+x]) if R[-1]-x in R or R[-1] < x else (R := R + [R[-1]-x]) for x in range(1,count)]
  plot_y = list(R)
  
elif mode == 3:
  setPltTitle('Collatz conjecture on graph')
  digits = [start]
  for i in range(count):
    if digits[-1] % 2 == 0:
      digits.append(digits[-1] / 2)
    else:
      digits.append((digits[-1] * 3) + 1)
  plot_y = digits


 
plot_x = list(range(len(plot_y)))

plt.plot(plot_x, plot_y)
  
plt.xlabel('x', fontsize=18)
plt.ylabel('y', fontsize=18)

# function to show the plot
mng = plt.get_current_fig_manager()
plt.get_current_fig_manager().set_window_title('Matplotlib - Python')

print("Loaded!")

def show_datapoints(sel):
  xi, yi = sel[0], sel[0]
  xi, yi = xi._xorig.tolist(), yi._yorig.tolist()
  sel.annotation.set_text('y: '+ str(yi[int(round(sel.index))])) # +'\n'+ 'y: '+ str(yi[int(round(sel.target.index))])

mplcursors.cursor(hover=True).connect('add',show_datapoints)

plt.show()
