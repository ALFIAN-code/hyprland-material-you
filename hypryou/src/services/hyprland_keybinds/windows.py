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
        (main_mod, "T"),
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
        (main_mod, "SHIFT", "right"),
        ("movewindow", "r")
    ),
    KeyBind(
        (main_mod, "SHIFT", "left"),
        ("movewindow", "l")
    ),
    KeyBind(
        (main_mod, "SHIFT", "up"),
        ("movewindow", "u")
    ),
    KeyBind(
        (main_mod, "SHIFT", "down"),
        ("movewindow", "d")
    ),

    KeyBind(
        ("alt", "Shift" ,"left"),
        ("resizeactive", "-30 0")
    ),
    KeyBind(
        ("alt", "Shift" ,"right"),
        ("resizeactive", "30 0")
    ),
    KeyBind(
        ("alt", "Shift" ,"up"),
        ("resizeactive", "0 -30")
    ),
    KeyBind(
        ("alt", "Shift" ,"down"),
        ("resizeactive", "0 30")
    ),
    KeyBind(
        (main_mod, "G"),
        "togglegroup",
        "Toggle group",
        Category.WINDOWS
    )
)
