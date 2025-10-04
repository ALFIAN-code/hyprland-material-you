from src.services.hyprland_keybinds.common import KeyBind, main_mod, Category

key_binds = (
    KeyBind(
        (main_mod, "Q"),
        "killactive",
        "Close window",
        Category.WINDOWS
    ),
    KeyBind(
        (main_mod, "F"),
        "fullscreen",
        "Open window in fullscreen mode",
        Category.WINDOWS
    ),
    KeyBind(
        (main_mod, "W"),
        "togglefloating",
        "Toggle floating mode",
        Category.WINDOWS
    ),
    KeyBind(
        (main_mod, "J"),
        "togglesplit",
        "Toggle split mode",
        Category.WINDOWS
    ),
    KeyBind(
        (main_mod, "left"),
        ("movefocus", "l")
    ),
    KeyBind(
        (main_mod, "right"),
        ("movefocus", "r")
    ),
    KeyBind(
        (main_mod, "up"),
        ("movefocus", "u")
    ),
    KeyBind(
        (main_mod, "down"),
        ("movefocus", "d")
    ),
    KeyBind(
        (main_mod, "mouse:272"),
        "movewindow"
    ),
    KeyBind(
        (main_mod, "mouse:273"),
        "resizewindow"
    ),
    KeyBind(
        (main_mod, "TAB"),
        "cyclenext",
        Category.WINDOWS
    ),
    KeyBind(
        (main_mod, "shift", "left"),
        ("movewindow", "l"),
        Category.WINDOWS
    ),
    KeyBind(
        (main_mod, "shift", "right"),
        ("movewindow", "r"),
        Category.WINDOWS
    ),
    KeyBind(
        (main_mod, "shift", "up"),
        ("movewindow", "u"),
        "Move window up",
        Category.WINDOWS
    ),
    KeyBind(
        (main_mod, "shift", "down"),
        ("movewindow", "d"),
        Category.WINDOWS
    ),
    KeyBind(
        (main_mod, "G"),
        "togglegroup",
        "Toggle group",
        Category.WINDOWS
    ),


)
