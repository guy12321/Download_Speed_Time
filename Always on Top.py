import ctypes
import ctypes.wintypes
import win32con

user32 = ctypes.windll.user32

def set_window_topmost(window_handle):
    # Imposta la finestra come sempre in primo piano
    user32.SetWindowPos(window_handle, ctypes.c_void_p(win32con.HWND_TOPMOST), 0, 0, 0, 0,
                        win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

def get_active_window():
    # Ottieni la finestra attualmente selezionata
    return user32.GetForegroundWindow()

def get_window_text(window_handle):
    # Ottieni il testo della finestra
    length = user32.GetWindowTextLengthW(window_handle) + 1
    buffer = ctypes.create_unicode_buffer(length)
    user32.GetWindowTextW(window_handle, buffer, length)
    return buffer.value

def toggle_always_on_top(window_handle):
    # Verifica lo stato corrente della finestra
    ex_style = user32.GetWindowLongPtrW(window_handle, win32con.GWL_EXSTYLE)
    if ex_style & win32con.WS_EX_TOPMOST:
        # Se già in primo piano, rimuovi l'opzione "always on top"
        user32.SetWindowPos(window_handle, ctypes.c_void_p(win32con.HWND_NOTOPMOST), 0, 0, 0, 0,
                            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        print(f"Finestra '{get_window_text(window_handle)}' sbloccata")
    else:
        # Altrimenti, imposta l'opzione "always on top"
        set_window_topmost(window_handle)
        print(f"Finestra '{get_window_text(window_handle)}' bloccata")

def handle_hotkey():
    # Funzione richiamata quando viene premuta la combinazione di tasti
    window_handle = get_active_window()
    toggle_always_on_top(window_handle)

def main():
    print("Programma avviato.")
    
    # Registra la combinazione di tasti come hotkey (Alt + Spacebar)
    if not user32.RegisterHotKey(None, 1, win32con.MOD_ALT, win32con.VK_SPACE):
        raise RuntimeError("Impossibile registrare la hotkey")

    # Loop principale del programma
    try:
        msg = ctypes.wintypes.MSG()
        while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
            if msg.message == win32con.WM_HOTKEY and msg.wParam == 1:
                handle_hotkey()

            user32.TranslateMessage(ctypes.byref(msg))
            user32.DispatchMessageW(ctypes.byref(msg))
    finally:
        # Deregistra la hotkey alla fine del programma
        user32.UnregisterHotKey(None, 1)
        print("Programma terminato.")

if __name__ == '__main__':
    main()
