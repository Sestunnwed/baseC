#include <X11/Xlib.h>
#include <X11/keysym.h>

int main() {
    Display *display;
    Window root_window;
    XEvent event;

    // 打开与X服务器的连接
    display = XOpenDisplay(NULL);
    if (display == NULL) {
        return -1;  // 打开显示失败
    }

    root_window = DefaultRootWindow(display);

    // 初始化按键按下事件
    memset(&event, 0, sizeof(XEvent));
    event.xkey.display = display;
    event.xkey.window = root_window;
    event.xkey.root = root_window;
    event.xkey.subwindow = root_window;
    event.xkey.time = CurrentTime;
    event.xkey.x = 0;
    event.xkey.y = 0;
    event.xkey.x_root = 0;
    event.xkey.y_root = 0;
    event.xkey.same_screen = True;

    // 模拟按下 'A' 键
    event.xkey.keycode = XKeysymToKeycode(display, XStringToKeysym("a"));
    event.type = KeyPress;
    XSendEvent(display, root_window, True, KeyPressMask, &event);

    // 模拟松开 'A' 键
    event.type = KeyRelease;
    XSendEvent(display, root_window, True, KeyReleaseMask, &event);

    // 清理资源
    XCloseDisplay(display);

}
