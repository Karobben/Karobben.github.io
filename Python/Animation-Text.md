---
url: animation-text
---

# Animation-Text


<br />![deepin-screen-recorder_Select area_20200122145317.gif](https://cdn.nlark.com/yuque/0/2020/gif/691897/1579676009809-e8b52670-cc62-4097-899d-33c7c7cf34a4.gif#align=left&display=inline&height=200&name=deepin-screen-recorder_Select%20area_20200122145317.gif&originHeight=200&originWidth=200&size=24690&status=done&style=none&width=200)<br />

```python

class Signal: # <1>
    go = True

def spin(msg, signal):  # <2>
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):  # <3>
        status = char + ' ' + msg
        write(status)
        flush()
        time.sleep(.1)
        write('\x08' * len(status))  # <4>
        if not signal.go:
              break
    write(' ' * len(status) + '\x08' * len(status))  # <6>


def slow_function():  # <7>
    # pretend waiting a long time for I/O
    time.sleep(3)  # <8>
    return 42


def supervisor():  # <9>
    signal = Signal()
    spinner = threading.Thread(target=spin,
                               args=('thinking!', signal))
    print('spinner object:', spinner)  # <10>
    spinner.start()  # <11>
    result = slow_function()  # <12>
    signal.go = False  # <13>
    spinner.join()  # <14>
    return result


def main():
    result = supervisor()  # <15>
    print('Answer:', result)


if __name__ == '__main__':
    main()
```

