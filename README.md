# MBPython

Miniblink is a lighter browser widget base on chromium,
just one file, faster browser kernel of blink to integrate HTML UI in your app.

MBPython is an open source project founded by lochen to provide python bindings for the Miniblink. Examples of embedding Miniblink browser are available for many popular GUI toolkits including: wxPython, PyQt, PySide, Kivy, Panda3D, PyGTK, PyGObject, PyGame/PyOpenGL and PyWin32.

By using C interface, you can create a browser just some line code.
There are many use cases for MBPython. You can embed a web browser control based on MBPython with great HTML 5 support. You can use it to create a HTML 5 based GUI in an application, this can act as a replacement for standard GUI toolkits like wxWidgets, Qt or GTK. You can render web content off-screen in application that use custom drawing frameworks. You can use it for automated testing of existing applications. You can use it for web scraping or as a web crawler, or other kind of internet bots.

### Latest release

OS | Py3 | 32bit | 64bit | Requirements
--- | --- | --- | --- | ---
Windows | 3.6+ | Yes | Yes | Windows 7+

### Installation

```bash
pip install --user MBPython
```

### How to use
Must create a new file named config.py like this demo → https://github.com/lochen88/MBPython/blob/master/tests/config.py
and download the node.dll add to your project.

<p style="color: red">
    The free version can only be called on the UI thread.
</p>

Create a simple Window
```bash
from MBPython import miniblink
wke=miniblink.MiniBlink
mb=wke.init()
window=wke.window
webview=window.wkeCreateWebWindow(0,0,0,860,760)
window.wkeShowWindow(webview)
window.wkeRunMessageLoop()
```

### PyInstaller

```bash
pyinstall xxx.py --noconsole
```

### Examples

See the [tests](https://github.com/lochen88/MBPython/tree/master/tests) folder

### Tutorial

See the [documents](https://github.com/lochen88/MBPython/tree/master/documents) folder

### What about CEF?

In short: I do not like CEF, it is too big, comes with too many dependency resolution library, and I think we can make a better and more intuitive one. Here are a few things that I don't like.

### Resources

<table border="0">
    <tr>
        <td width="50%" valign="top">
            <p align="center">
                <img src="https://raw.githubusercontent.com/lochen88/MBPython/master/tests/testjs/images/qq.jpg">
            </p>
            if you have any questions,you can contact me,and i will try my best to help you
        </td>
        <td width="50%" valign="top">
            <p align="center">
                <img src="https://raw.githubusercontent.com/lochen88/MBPython/master/tests/testjs/images/alipay.jpg">
            </p>
            If you would like to support general MBPython development efforts by making a donation then please scan to pay by the alipay
        </td>
    </tr>
</table>

* [Project Website](https://github.com/lochen88/MBPython)
* [Issue Tracker](https://github.com/lochen88/MBPython/issues)
* [Official Website](https://weolar.github.io/miniblink/)
* [QQ Group-198671899](https://qm.qq.com/cgi-bin/qm/qr?k=JipVq9gRdpPf4dqjPK9bkL99u-_BLwZz&jump_from=webapi)


