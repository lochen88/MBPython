# Tutorial
With MBPython you can embed a web browser control based
on Chromium in a Python application. You can also use it to
create a HTML 5 based GUI in an application that can act as
a replacement for standard GUI toolkits such as wxWidgets,
Qt or GTK. With this tutorial you will learn MBPython
basics. This tutorial will discuss the three featured examples:

[test_mbpython.py](../tests/test_mbpython.py),
[test_bindwindow.py](../tests/test_bindwindow.py)
and [test_bindwebview.py](../tests/test_bindwebview.py).

## Install and run example

You can install with pip. Alternatively you can download packages for offline installation from QQ-Group.

Run the commands below to install the MBPython package, clone
the repository and run the test_mbpython example:

```bash
pip install --user MBPython
git clone https://github.com/lochen88/MBPython.git
cd MBPython/tests/
python test_mbpython.py
```

The [test_mbpython.py](../tests/test_mbpython.py) example is the
most basic example. It doesn't depend on any third party GUI framework.
It creates a browser widget without providing any window information
(parent window is not specified), thus Miniblink automatically takes care of
creating a top-level window, and in that window a Chromium widget
is being embedded. When creating the browser, the "url" parameter is
specified, which causes the browser to initially navigate to Baidu website. Let's analyze the code from that example:

1. `from MBPython import miniblink` - Import the miniblink module
2. `wke.init()` - Initialize Miniblink. This function must be called
   somewhere in the beginning of your code. It must be called before
   any application window is created. It must be called only once
   during app's lifetime.
3. `window.wkeCreateWebWindow(0,0,0,860,760)` - Create
   a browser, this function returns a Browser object.
4. `window.wkeRunMessageLoop()` - Run Miniblink message loop. Message loop is a programming construct that waits for and
dispatches events or messages in a program. All desktop GUI
programs must run some kind of message loop. The test_mbpython.py
example doesn't depend on any third party GUI framework and thus
can run Miniblink message loop directly by calling window.wkeRunMessageLoop().
However in other examples that embed Miniblink browser with GUI frameworks
such as Qt/wxPython/Tkinter you can't call window.wkeRunMessageLoop(), because
these frameworks run a message loop of its own.

## Javascript integration
In the free version of Miniblink, Python and Javascript just can communicate sync.

In [test_bindwindow.py](../tests/test_bindwindow.py) and  [test_bindwebview.py](../tests/test_bindwindow.py) example you will find

example usage of javascript bindings, javascript callbacks
and python callbacks. Here is part of its source code:

```python
def test_js_run_py(**kwargs):
    es=kwargs['es']
    param=kwargs['param']
    arg_count=jsrunpy.mb.jsArgCount(es)
    val_ls=jsrunpy.get_js_args_val(es,arg_count)
    print(val_ls,'test_js_run_py')

    hwnd=param
    if val_ls[0]=='move':
        user32.ReleaseCapture()
        user32.SendMessageW(hwnd,161, 2, 0)
    elif val_ls[0]=='close':
        win32gui.PostQuitMessage(0)
    elif val_ls[0]=='max':
        ismax=user32.IsZoomed(hwnd)
        if ismax==0:
            user32.ShowWindow(hwnd,3)
        elif ismax==1:
            user32.ShowWindow(hwnd,1)
    elif val_ls[0]=='min':
        user32.ShowWindow(hwnd,2)
    elif val_ls[0]=='menu':
        return jsrunpy.to_js_args_val(es,'点击菜单')
    elif val_ls[0]=='loadurl':
        pyrunjs.run_js(webview,'alert("create new window")')
        j_webview=window.wkeCreateWebWindow(0,0,0,360,480)
        network.wkeLoadURLW(j_webview,'https://www.baidu.com/')
        window.wkeShowWindow(j_webview)
    return 0
```

## Plugins and Flash support

Miniblink supports NPAPI plugins.

## Off-screen rendering

Off-screen rendering, in short OSR, also known as windowless
rendering, is a method of rendering pages into a memory buffer
without creating an actual visible window. This method of
rendering has its uses, some pluses and some minuses. Its main
use is so that web page rendering can be integrated into apps
that have its own rendering systems and they can draw web browser
contents only if they are provided a pixel buffer to draw. MBPython
provides [test_bindwebview.py](../tests/test_bindwindow.py) example of integrating Miniblink off-screen rendering
with frameworks.

* [Api-index](https://github.com/lochen88/MBPython/blob/master/documents/api.md#methods)