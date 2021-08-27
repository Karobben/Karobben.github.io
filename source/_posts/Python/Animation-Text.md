---
title: "Text Animation in Python"
ytitle: "Python: terminal 內的文字動畫"
description: "Text Animation in Python for scripts updating"
url: animation-text2
date: 2020/06/22
toc: true
excerpt: "Text Animation for Python scripts"
tags: [Python, Script]
category: [Python, Scripting, Module]
cover: 'https://th.bing.com/th/id/R3d9a78ed6fe62aa5ee6e9fd61c092cca?rik=I7LX8qXniM2YLQ&riu=http%3a%2f%2fgetcodify.com%2fwp-content%2fuploads%2f2016%2f10%2fPython_logo.jpg&w=680'
covercopy: '© getcodify.com'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---

## Animation-Text

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
