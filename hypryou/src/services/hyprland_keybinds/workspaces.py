from src.services.hyprland_keybinds.common import (
    KeyBindHint, main_mod, Category
)

key_binds = (
    KeyBindHint(
        (main_mod, "0-9"),
        "Switch workspace",
        Category.WORKSPACES
    ),
    KeyBindHint(
        (main_mod, "Shift", "0-9"),
        "Move window to workspace",
        Category.WORKSPACES
    ),
    KeyBindHint(
        (main_mod, "CTRL", "down"),
        "Switch to empty workspace",
        Category.WORKSPACES
    ),
    KeyBindHint(
        (main_mod, "Shift", "S"),
        ("movetoworkspacesilent", "special"),
        "Move to Special workspace",
        Category.WINDOWS
    ),
    KeyBindHint(
        (main_mod, "S"),
        ("exec", "hyprctl dispatch togglespecialworkspace"),
        "Special workspace",
        Category.WINDOWS
    ),
    KeyBindHint(
        (main_mod, "Z"),
        ("workspace", "-1"),
        "Players",
        Category.TOOLS
    ),
    KeyBindHint(
        (main_mod, "X"),
        ("workspace", "+1"),
        "Players",
        Category.TOOLS
    ),
)
