# Api index 

* [window(object)-Methods](#methods)
  * [wkeCreateWebWindow](#wkeCreateWebWindow)
  * [wkeShowWindow](#wkeShowWindow)
  * [wkeCreateWebView](#wkeCreateWebView)
  * [wkeDestroyWebView](#wkeDestroyWebView)
  * [wkeMoveToCenter](#wkeMoveToCenter)
  * [wkeRunMessageLoop](#wkeRunMessageLoop)
  * [wkeSetUserAgentW](#wkeSetUserAgentW)
  * [wkeSetDragEnable](#wkeSetDragEnable)
  * [wkeAddPluginDirectory](#wkeAddPluginDirectory)
  * [wkeSetNpapiPluginsEnabled](#wkeSetNpapiPluginsEnabled)
  * [wkeSetCspCheckEnable](#wkeSetCspCheckEnable)
  * [wkeSetDebugConfig](#wkeSetDebugConfig)
  * [wkeSetNavigationToNewWindowEnable](#wkeSetNavigationToNewWindowEnable)
  * [wkeSetWebViewName](#wkeSetWebViewName)
  * [wkeSetZoomFactor](#wkeSetZoomFactor)
  * [wkeSetContextMenuEnabled](#wkeSetContextMenuEnabled)
  * [wkeSetWindowTitleW](#wkeSetWindowTitleW)
  * [wkeSetTransparent](#wkeSetTransparent)
  * [wkeSetHandle](#wkeSetHandle)
  * [wkeResize](#wkeResize)
  * [wkeWidth](#wkeWidth)
  * [wkeHeight](#wkeHeight)
  * [wkeContentsWidth](#wkeContentsWidth)
  * [wkeContentsHeight](#wkeContentsHeight)
  * [wkeGoForward](#wkeGoForward)
  * [wkeGoBack](#wkeGoBack)
  * [wkeGetWindowHandle](#wkeGetWindowHandle)
  * [wkeGetViewDC](#wkeGetViewDC)
  * [wkeSetTouchEnabled](#wkeSetTouchEnabled)
  * [simulate_device](#simulate_device)
  * [bind_window](#bind_window)

* [network(object)-Methods](#methods)
  * [wkeLoadURLW](#wkeLoadURLW)
  * [wkeLoadHTMLW](#wkeLoadHTMLW)
  * [wkeLoadFile](#wkeLoadFile)
  * [wkePostURLW](#wkePostURLW)
  * [wkeReload](#wkeReload)
  * [wkeStopLoading](#wkeStopLoading)
  * [wkeGetURL](#wkeGetURL)
  * [wkeGetFrameUrl](#wkeGetFrameUrl)
  * [wkeGetSource](#wkeGetSource)
  * [wkeUtilSerializeToMHTML](#wkeUtilSerializeToMHTML)
  * [save_buf_data](#save_buf_data)
  * [cancel_request](#cancel_request)  

* [pyrunjs(object)-Methods](#methods)
  * [run_js](#run_js)
  * [run_js_file](#run_js_file)
  * [run_js_byframe](#run_js_byframe)
  * [run_js_global](#run_js_global)

* [jsrunpy(object)-Methods](#methods)
  * [get_js_args_val](#get_js_args_val)
  * [to_js_args_val](#to_js_args_val)
  * [bind_func](#bind_func)

* [proxy(object)-Methods](#methods)
  * [wkeSetProxy](#wkeSetProxy)
  * [wkeSetViewProxy](#wkeSetViewProxy)

* [cookie(object)-Methods](#methods)
  * [wkeGetCookieW](#wkeGetCookieW)
  * [wkeSetCookie](#wkeSetCookie)
  * [wkeSetCookieJarPath](#wkeSetCookieJarPath)
  * [wkeSetCookieJarFullPath](#wkeSetCookieJarFullPath)
  * [wkeClearCookie](#wkeClearCookie)

* [message(object)-Methods](#methods)
  * [wkeFireMouseEvent](#wkeFireMouseEvent)
  * [wkeFireKeyDownEvent](#wkeFireKeyDownEvent)
  * [wkeFireKeyUpEvent](#wkeFireKeyUpEvent)
  * [wkeFireKeyPressEvent](#wkeFireKeyPressEvent)
  * [wkeFireWindowsMessage](#wkeFireWindowsMessage)

* [bindwebview(object)-Methods](#methods)
  * [bind_webview](#bind_webview)

* [callback(object)-Methods](#methods)
  * [wkeOnCreateView](#wkeOnCreateView)
  * [wkeOnWindowClosing](#wkeOnWindowClosing)
  * [wkeOnWindowDestroy](#wkeOnWindowDestroy)
  * [wkeOnPaintUpdated](#wkeOnPaintUpdated)
  * [wkeOnPaintBitUpdated](#wkeOnPaintBitUpdated)
  * [wkeOnTitleChanged](#wkeOnTitleChanged)
  * [wkeOnURLChanged2](#wkeOnURLChanged2)
  * [wkeOnMouseOverUrlChanged](#wkeOnMouseOverUrlChanged)
  * [wkeOnAlertBox](#wkeOnAlertBox)
  * [wkeOnConfirmBox](#wkeOnConfirmBox)
  * [wkeOnPromptBox](#wkeOnPromptBox)
  * [wkeOnConsole](#wkeOnConsole)
  * [wkeOnDownload](#wkeOnDownload)
  * [wkeOnDocumentReady2](#wkeOnDocumentReady2)
  * [wkeNetOnResponse](#wkeNetOnResponse)
  * [wkeOnLoadUrlBegin](#wkeOnLoadUrlBegin)
  * [wkeOnLoadUrlEnd](#wkeOnLoadUrlEnd)
  * [wkeOnLoadUrlFail](#wkeOnLoadUrlFail)
  * [wkeOnLoadingFinish](#wkeOnLoadingFinish)
  * [wkeNetGetFavicon](#wkeNetGetFavicon)


## Methods

### wkeCreateWebWindow

| Parameter | Type | description
| --- | --- | --- |
| _type | int |0:normal window,1:transparent window,3:embedded window |
| hwnd | int |embedded other window's handle |
| x | int | x axis |
| y | int | y axis |
| width | int | window's width |
| height | int | window's height |
| __Return__ | int | webview |

### wkeShowWindow

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| _bool | bool | -- |
| __Return__ | None | -- |

### wkeCreateWebView

| Parameter | Type | description
| --- | --- | --- |
| __Return__ | int | webview |

### wkeDestroyWebView

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| __Return__ | None | -- |

### wkeMoveToCenter

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| __Return__ | None | -- |

### wkeRunMessageLoop

| Parameter | Type | description
| --- | --- | --- |
| __Return__ | None | -- |

### wkeSetUserAgentW

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| ua | string | -- |
| __Return__ | None | -- |

### wkeGetUserAgent

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| __Return__ | None | -- |

### wkeSetDragEnable

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| _bool | bool | -- |
| __Return__ | None | -- |

### wkeAddPluginDirectory

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| _path | string | -- |
| __Return__ | None | -- |

### wkeSetNpapiPluginsEnabled

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| _bool | bool | -- |
| _path | string | -- |
| __Return__ | None | -- |

If you want to use flash must ues this method 

### wkeSetCspCheckEnable

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| _bool | bool | -- |
| __Return__ | None | -- |

### wkeSetDebugConfig

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| debug | string | -- |
| param | string | -- |
| __Return__ | None | -- |

### wkeSetCspCheckEnable

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| _bool | bool | -- |
| __Return__ | None | -- |

### wkeSetHeadlessEnabled

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| _bool | bool | -- |
| __Return__ | None | -- |

### wkeSetNavigationToNewWindowEnable

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| _bool | bool | -- |
| __Return__ | None | -- |

### wkeSetWebViewName

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| name | string | -- |
| __Return__ | None | -- |

### wkeSetZoomFactor

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| factor | int | -- |
| __Return__ | None | -- |

### wkeSetContextMenuEnabled

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| _bool | bool | -- |
| __Return__ | None | -- |

### wkeSetWindowTitleW

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| title | string | -- |
| __Return__ | None | -- |

### wkeSetHandleOffset

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| x | int | -- |
| y | int | -- |
| __Return__ | None | -- |

### wkeSetHandle

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| hwnd | int | -- |
| __Return__ | None | -- |

### wkeResize

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| width | int | -- |
| height | int | -- |
| __Return__ | None | -- |

### wkeWidth

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| __Return__ | int | width |

### wkeHeight

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| __Return__ | int | height |

### wkeContentsWidth

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| __Return__ | int | contentswidth |

### wkeContentsHeight

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| __Return__ | int | contentsheight |

### wkeGoForward

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| __Return__ | None | -- |

### wkeGoForward

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| __Return__ | None | -- |

### wkeGetWindowHandle

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| __Return__ | int |hwnd |

### wkeGetViewDC

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| __Return__ | int | DC |

### wkeSetTouchEnabled

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| _bool | bool | -- |
| __Return__ | None | -- |

### simulate_device

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| key | string | -- |
| value | string | -- |
| _int | int | -- |
| _float | float | -- |
| __Return__ | None | -- |

### bind_window

| Parameter | Type | description
| --- | --- | --- |
| hwnd | int | -- |
| _bool | bool | -- |
| __Return__ | int | webview |

### run_js

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| js_code | string | -- |
| __Return__ | string | -- |

### run_js_file

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| file_name | string | -- |
| __Return__ | string | -- |

### run_js_byframe

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| frameId | int | -- |
| js_code | string | -- |
| isInClosure | bool | -- |
| __Return__ | string | -- |

### run_js_global

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| func_name | string | -- |
| param_ls | list | -- |
| this_func | string | -- |
| __Return__ | string | -- |

### wkeSetProxy

| Parameter | Type | description
| --- | --- | --- |
| ip | string | -- |
| port | string | -- |
| proxy_type | int | 0:WKE_PROXY_NONE,1:WKE_PROXY_HTTP,2:WKE_PROXY_SOCKS4,3:WKE_PROXY_SOCKS4A,4:WKE_PROXY_SOCKS5,5:WKE_PROXY_SOCKS5HOSTNAME |
| user | string | -- |
| password | string | -- |
| __Return__ | None | -- |

### wkeSetViewProxy

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| ip | string | -- |
| port | string | -- |
| proxy_type | int | -- |
| user | string | -- |
| password | string | -- |
| __Return__ | None | -- |

### wkeLoadURLW

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| url | string | -- |
| __Return__ | None | -- |

### wkeLoadHTMLW

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| html | string | -- |
| __Return__ | None | -- |

### wkeLoadFile

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| file_path | string | -- |
| __Return__ | None | -- |

### wkeReload

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| __Return__ | None | -- |

### wkeStopLoading

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| __Return__ | None | -- |

### wkeGetURL

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| __Return__ | string | url |

### wkeGetFrameUrl

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| frameId | int | -- |
| __Return__ | string | url |

### wkeGetSource

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| __Return__ | string | html |

### wkeUtilSerializeToMHTML

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| __Return__ | string | mhtml |

### save_buf_data

| Parameter | Type | description
| --- | --- | --- |
| url | string | -- |
| buf | int | -- |
| lens | int | -- |
| __Return__ | None | -- |

Use it in the wkeLoadUrlEndCallback method

### cancel_request

| Parameter | Type | description
| --- | --- | --- |
| job | int | -- |
| url | string | -- |
| ident_ls | list | -- |
| __Return__ | bool | -- |

### get_js_args_val

| Parameter | Type | description
| --- | --- | --- |
| es | int | -- |
| arg_count | int | -- |
| __Return__ | list | args |

### to_js_args_val

| Parameter | Type | description
| --- | --- | --- |
| es | int | -- |
| val | -- | string/int/float/bool/list |
| __Return__ | int | jsvalue |

### bind_func

| Parameter | Type | description
| --- | --- | --- |
| func_name | string | callback funtion name |
| arg_count | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function: python_func

### wkeGetCookieW

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| __Return__ | string | cookie |

### wkeSetCookie

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| url | string | -- |
| cookie | string | -- |
| __Return__ | None | -- |

### wkeSetCookieJarPath

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| path | string | F:\MBPython |
| __Return__ | None | -- |

### wkeSetCookieJarFullPath

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| path | string | F:\MBPython\mycookie.dat |
| __Return__ | None | -- |

### wkeClearCookie

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| __Return__ | None | -- |

### wkeFireMouseEvent

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| msg | int | -- |
| x | int | -- |
| y | int | -- |
| flags | int | -- |
| __Return__ | bool | -- |

### wkeFireKeyDownEvent

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| virtualKeyCode | int | -- |
| flags | int | -- |
| __Return__ | bool | -- |

### wkeFireKeyUpEvent

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| virtualKeyCode | int | -- |
| flags | int | -- |
| __Return__ | bool | -- |

### wkeFireKeyPressEvent

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| virtualKeyCode | int | -- |
| flags | int | -- |
| __Return__ | bool | -- |

### wkeFireWindowsMessage

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| hwnd | int | -- |
| msg | int | -- |
| wParam | int | -- |
| lParam | int | -- |
| result | int | -- |
| __Return__ | bool | -- |

### bind_webview

| Parameter | Type | description
| --- | --- | --- |
| hwnd | int | -- |
| isTransparent | bool | -- |
| isZoom | bool | -- |
| __Return__ | int | webview |

### wkeOnCreateView

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkeCreateViewCallback

### wkeOnWindowClosing

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkeWindowClosingCallback

### wkeOnWindowDestroy

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkeWindowDestroyCallback

### wkeOnPaintUpdated

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkePaintUpdatedCallback

### wkeOnPaintBitUpdated

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkePaintBitUpdatedCallback

### wkeOnNavigation

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkeNavigationCallback

### wkeOnTitleChanged

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkeTitleChangedCallback

### wkeOnURLChanged2

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkeURLChangedCallback2

### wkeOnMouseOverUrlChanged

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkeMouseOverUrlChangedCallback

### wkeOnAlertBox

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkeAlertBoxCallback

### wkeOnConfirmBox

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkeConfirmBoxCallback

### wkeOnPromptBox

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkePromptBoxCallback

### wkeOnConsole

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkeConsoleCallback

### wkeOnDownload

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkeDownloadCallback

### wkeOnDocumentReady2

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkeDocumentReady2Callback

### wkeNetOnResponse

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkeNetResponseCallback

### wkeOnLoadUrlBegin

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkeLoadUrlBeginCallback

### wkeOnLoadUrlEnd

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkeLoadUrlEndCallback

### wkeOnLoadUrlFail

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkeLoadUrlFailCallback

### wkeOnLoadingFinish

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkeLoadingFinishCallback

### wkeNetGetFavicon

| Parameter | Type | description
| --- | --- | --- |
| webview | int | -- |
| param | int | ptr |
| __Return__ | None | -- |
self-defined callback function:wkeOnNetGetFaviconCallback



