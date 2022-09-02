from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess

mod = "mod4"
terminal = guess_terminal()
browser = "chromium"
file_manager = "thunar"

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Keybindings to launch user defined Programs
    Key([mod], "f", lazy.spawn(file_manager), desc="Launch File Manager"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch Browser"),
    Key([mod], "c", lazy.spawn("code"), desc="Launch VS Code"),
    Key([mod], "space", lazy.spawn('rofi -show run'), desc="Launch Rofi"),

    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),

    # Keyboard Backlight
    Key([mod], "Up", lazy.spawn("brightnessctl --device='asus::kbd_backlight' set +1")),   
    Key([mod], "Down", lazy.spawn("brightnessctl --device='asus::kbd_backlight' set 1-")),
    
    # Monitor Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl --device='intel_backlight' set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl --device='intel_backlight' set 10-%")),

]



# groups = [Group(i) for i in "123456789"]

# for i in groups:
#     keys.extend(
#         [
#             # mod1 + letter of group = switch to group
#             Key(
#                 [mod],
#                 i.name,
#                 lazy.group[i.name].toscreen(),
#                 desc="Switch to group {}".format(i.name),
#             ),
#             # mod1 + shift + letter of group = switch to & move focused window to group
#             Key(
#                 [mod, "shift"],
#                 i.name,
#                 lazy.window.togroup(i.name, switch_group=True),
#                 desc="Switch to & move focused window to group {}".format(i.name),
#             ),
#             # Or, use below if you prefer not to switch to that group.
#             # # mod1 + shift + letter of group = move focused window to group
#             # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#             #     desc="move focused window to group {}".format(i.name)),
#         ]
#     )

icons = {
        "folder": "\uf07b", # fa-folder
        "chat": "\uf4ad", # fa-comment-dots
        "web": "\uf268", # fa-chrome
        "terminal": "\ue236" , # fa-rectangle-terminal
        "dev": "\uf6cc", # fa-dev
        "discord": "\uf392", # fa-discord
}


# groups = []
# group_names = ["1", "2", "3", "4", "5"]
# #group_labels = [icons[dev], icons[web], icons[terminal], icons[folder], icons[discord]]
# group_labels = ["\uf121", "\uf268", "\uf120", "\uf07b", "\ufb6e"]

# group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]

# for i in range(len(group_names)):
#     groups.append(
#             Group(
#                 name=group_names[i],
#                 layout=group_layouts[i].lower(),
#                 label=group_labels[i],
#             )
#     )

# for i in groups:
#     keys.extend([
#         Key([mod], i.name, lazy.group[i.name].toscreen()),
#         Key([mod], "Tab", lazy.screen.next_group()),
#         Key([mod, "shift"], "Tab", lazy.screen.prev_group()),

#         ])


# Icons: 
# nf-fa-firefox, 
# nf-fae-python, 
# nf-dev-terminal, 
# nf-fa-code, 
# nf-oct-git_merge, 
# nf-linux-docker,
# nf-mdi-image, 
# nf-mdi-layers

groups = [Group(i) for i in ["","","","","ﭮ","","","","",]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])




# groups = [
#     Group("1", layout="monadtall",  matches=[Match(wm_class=["navigator", "firefox", "vivaldi-stable", "chromium", "brave"])]),
#     Group("2", layout="monadtall",  matches=[Match(wm_class=["emacs", "geany", "subl"])]),
#     Group("3", layout="monadtall",  matches=[Match(wm_class=["inkscape", "nomacs", "ristretto", "nitrogen","code"])]),
#     Group("4", layout="monadtall",  matches=[Match(wm_class=["qpdfview", "thunar", "nemo", "caja", "pcmanfm"])]),
#     Group("5", layout="max",        matches=[Match(wm_class=["discord"])]),
#     Group("6", layout="ratiotile"),
#     Group("7", layout="max",        matches=[Match(wm_class=["spotify", "pragha", "clementine", "deadbeef", "audacious"]), Match(title=["VLC media player"])]),
#     Group("8", layout="tile"),
# ]

# for k, group in zip(["1", "2", "3", "4", "5", "6", "7", "8"], groups):
#     keys.extend(
#         [
#             Key(
#                 [mod],
#                 k, 
#                 lazy.group[k].toscreen(), 
#                 #desc="Switch to group {}".format(k),
#             ),
#             Key(
#                 [mod, "shift"],
#                 k, 
#                 lazy.window.togroup(k), 
#                 #desc="Switch to & move focused window to group {}".format(k),
#             ),
#         ]
#     )








layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4,margin=2),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

colors = [["#2e3440", "#2e3440"], # color 0  dark grayish blue
          ["#2e3440", "#2e3440"], # color 1  dark grayish blue
          ["#3b4252", "#3b4252"], # color 2  very dark grayish blue
          ["#434c5e", "#434c5e"], # color 3  very dark grayish blue
          ["#4c566a", "#4c566a"], # color 4  very dark grayish blue
          ["#d8dee9", "#d8dee9"], # color 5  grayish blue
          ["#e5e9f0", "#e5e9f0"], # color 6  light grayish blue
          ["#eceff4", "#eceff4"], # color 7  light grayish blue
          ["#8fbcbb", "#8fbcbb"], # color 8  grayish cyan
          ["#88c0d0", "#88c0d0"], # color 9  desaturated cyan
          ["#81a1c1", "#81a1c1"], # color 10 desaturated blue
          ["#5e81ac", "#5e81ac"], # color 11 dark moderate blue
          ["#bf616a", "#bf616a"], # color 12 slightly desaturated red
          ["#d08770", "#d08770"], # color 13 desaturated red
          ["#ebcb8b", "#ebcb8b"], # color 14 soft orange
          ["#a3be8c", "#a3be8c"], # color 15 desaturated green
          ["#b48ead", "#b48ead"]] # color 16 grayish magenta

widget_defaults = dict(
    font="Font Awesome 6",
    fontsize=18,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
                widget.TextBox(
                   # background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Image(filename="~/.config/qtile/icons/Launch.png",iconsize=10,background=colors[6],mouse_callbacks={'Button1': lambda : qtile.cmd_spawn('rofi -show run')}),
                widget.TextBox(
                   # background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Spacer(length=10),
                #widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
                # widget.CurrentLayout(),
                widget.TextBox(
                    #background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.GroupBox(
                    active=colors[16],
                    border_width=2,
                    disable_drag=True,
                    font='FontAwesome',
                    #hide_unused=True,
                    highlight_method='line',
                    inactive=colors[9],
                    fontsize=28,
                    background=colors[6],
                    foreground=colors[1],
                    # margin_x=3,
                    # margin_y=5,
                    # padding_x=5,
                    # padding_y=8,
                    # rounded=True,
                    this_current_screen_border=colors[12],
                    urgent_alert_method='line'
                ),
                widget.TextBox(
                    # background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Spacer(length=10),
                widget.TextBox(
                 # background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
                widget.Prompt(
                    background=colors[6],
                    foreground=colors[1],
                    fontsize=18,
                    prompt='',
                    bell_style='audible'
                
                ),
                widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
                widget.TextBox(
                        # background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),

                #widget.WindowName(),
                widget.Spacer(),
                # widget.Chord(
                #     chords_colors={
                #         "launch": ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.TextBox(
                        #  background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
                widget.CheckUpdates(
                    no_update_string='',
                    colour_have_updates=colors[12],
                    background=colors[6],
                    foreground=colors[1],
                ),
                widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
                widget.TextBox(
                        #                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Spacer(length=10),
                widget.TextBox(
                        #                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.TextBox(
                   background=colors[6],
                   font='Ubuntu Nerd Font',
                   fontsize=30,
                   foreground=colors[1],
                   text=''
                ),
                widget.Backlight(
                    brightnes_file='/sys/class/backlight/intel_backlight/brightness',
                    backlight_name='intel_backlight',
                    change_command="brightnessctl --device='intel_backlight' set {0}",
                    #step=
                    format='{percent:2.0%}',
                    background=colors[6],
                    foreground=colors[1],
                ),
                widget.TextBox(
                        #                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Spacer(length=10),
                #widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
                widget.TextBox(
                        #                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.TextBox(
                   background=colors[6],
                   font='Ubuntu Nerd Font',
                   fontsize=30,
                   foreground=colors[1],
                   text=''
                ),
                widget.Volume(
                    #emoji=True,
                    #fmt='{}',
                    background=colors[6],
                    foreground=colors[1],                                    
                ),
                widget.TextBox(
                        #                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Spacer(length=10),
                #widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
                widget.TextBox(
                        #                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Battery(
                    charge_char='',
                    discharge_char='',
                    format='{char} {percent:2.0%}',
                    background=colors[6],
                    foreground=colors[1],
                ),
                widget.TextBox(
                        #                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Spacer(length=10),
                #widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
                widget.TextBox(
                        #                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Systray(
                    background=colors[6],
                    foreground=colors[1],
                ),

                widget.TextBox(
                        #                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Spacer(length=10),
                widget.TextBox(
                        #                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                #widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
                widget.TextBox(
                   background=colors[6],
                   font='Ubuntu Nerd Font',
                   fontsize=30,
                   foreground=colors[1],
                   text=''
                ),
                widget.Clock(
                    background=colors[6],
                    foreground=colors[1],
                    font="FontAwesome",
                    fontsize=20,
                    format="%H:%M"
                    #format="%a %d, (%B) %H:%M "
                ),
                #widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
                widget.TextBox(
                        #                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Spacer(length=10),
                widget.TextBox(
                        #                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.QuickExit(
                    font="FontAwesome",
                    fontsize=22,
                    background=colors[6],
                    foreground=colors[1],
                    default_text='\uf011', 
                    countdown_format='{}'
                    #mouse_callbacks={}
                ),
                widget.TextBox(
                        #                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                
                
            ],
            26,
            margin=5,
            background="#00000000"
        ),
        bottom=bar.Bar(
            [
                widget.Spacer(length=10),
                widget.CurrentLayoutIcon(
                    background=colors[1],
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    foreground=colors[6], #e5e9f0
                    padding=0,
                    scale=0.65
                ),
                widget.Spacer(length=10),
                widget.TextBox(
                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.WindowName(
                    text="Name",
                    background=colors[6],
                    foreground=colors[1],
                    max_chars=30
                ),
                widget.TextBox(
                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Spacer(length=800),
                widget.TextBox(
                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.TextBox(
                    background=colors[6],
                    foreground=colors[1],
                    fontsize=24,
                    text=""
                ),
                widget.ThermalSensor(
                    background=colors[6],
                    foreground=colors[1],
                    update_interval=2,

                ),
                widget.TextBox(
                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Spacer(length=10),
                #widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
                widget.TextBox(
                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),

                widget.TextBox(
                    background=colors[6],
                    foreground=colors[1],
                    fontsize=26,
                    text=""
                ),
                widget.Memory(
                    background=colors[6],
                    foreground=colors[1],
                    #font='Ubuntu',
                    #fontsize=12,
                    format="{MemUsed: .0f}{mm}",
                    update_interval=1.0
                ),
                widget.TextBox(
                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Spacer(length=10),
                #widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
                widget.TextBox(
                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.TextBox(
                    background=colors[6],
                    foreground=colors[1],
                    fontsize=24,
                    text=""
                ),
                widget.CPU(
                    background=colors[6],
                    foreground=colors[1],
                    format='{load_percent}%',
                    update_interval=1
                ),
                widget.TextBox(
                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Spacer(length=10),
                #widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
                widget.TextBox(
                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.TextBox(
                   background=colors[6],
                   font='Ubuntu Nerd Font',
                   fontsize=30,
                   foreground=colors[1],
                   text=''
                ),
                widget.Wlan(
                    disconnected_message='X',
                    background=colors[6],
                    foreground=colors[1],
                    #mouse_callbacks={}
                ),
                widget.TextBox(
                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Spacer(length=10),
                #widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
                widget.TextBox(
                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Net(
                    background=colors[6],
                    foreground=colors[1],
                    #font='Ubuntu',
                    #fontsize=12,
                    format='{down} ↓ ',
                    #interface='all',
                    padding=0
                ),
                widget.TextBox(
                   background=colors[1],
                   font='Ubuntu Nerd Font',
                   fontsize=24,
                   foreground=colors[6],
                   padding=0,
                   text=''
                ),
                widget.Spacer(length=10),
            ],
            26,
            background='#00000000',
            margin=5,   
        ),
        #margin=5,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
