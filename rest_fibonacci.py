from flask import Flask
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Fibonacci plain vs with memoization!'

@app.route('/fibonacci/<int:nth>/<string:mode>')
def fibonacci_endpoint(nth, mode):
    start = time.time()
    print str(start)
    fib = 0
    if mode == "plain":
        fib = fibonacci_plain(nth,{})
    elif mode == "memoization":
        fib = fibonacci_memoization(nth,{})
    else:
        return 404
    execution_time = time.time() - start
    print "end time: '" + str(execution_time) + "'"
    return "fibonacci " + str(nth) + "th: '" + str(fib) + "' computation time: '" + str(execution_time) + "' seconds"

def fibonacci_memoization(nth, mem):
    if nth == 1 or nth == 2:
        return 1
    mem[nth-1] = fibonacci_memoization(nth-1, mem) if not nth-1 in mem else mem[nth-1]
    mem[nth-2] = fibonacci_memoization(nth-2, mem) if not nth-2 in mem else mem[nth-2]
    return mem[nth-1] + mem[nth-2]

def fibonacci_plain(nth, mem):
    if nth == 1 or nth == 2:
        return 1
    mem[nth-1] = fibonacci_plain(nth-1, mem)
    mem[nth-2] = fibonacci_plain(nth-2, mem)
    return mem[nth-1] + mem[nth-2]
