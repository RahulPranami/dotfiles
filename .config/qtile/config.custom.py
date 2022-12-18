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
    "folder": "\uf07b",  # fa-folder
    "chat": "\uf4ad",  # fa-comment-dots
    "web": "\uf268",  # fa-chrome
    "terminal": "\ue236",  # fa-rectangle-terminal
    "dev": "\uf6cc",  # fa-dev
    "discord": "\uf392",  # fa-discord
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

groups = [Group(i) for i in ["", "", "", "", "ﭮ", "", "", "", "",]]

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

colors = [["#2e3440", "#2e3440"],  # color 0  dark grayish blue
          ["#2e3440", "#2e3440"],  # color 1  dark grayish blue
          ["#3b4252", "#3b4252"],  # color 2  very dark grayish blue
          ["#434c5e", "#434c5e"],  # color 3  very dark grayish blue
          ["#4c566a", "#4c566a"],  # color 4  very dark grayish blue
          ["#d8dee9", "#d8dee9"],  # color 5  grayish blue
          ["#e5e9f0", "#e5e9f0"],  # color 6  light grayish blue
          ["#eceff4", "#eceff4"],  # color 7  light grayish blue
          ["#8fbcbb", "#8fbcbb"],  # color 8  grayish cyan
          ["#88c0d0", "#88c0d0"],  # color 9  desaturated cyan
          ["#81a1c1", "#81a1c1"],  # color 10 desaturated blue
          ["#5e81ac", "#5e81ac"],  # color 11 dark moderate blue
          ["#bf616a", "#bf616a"],  # color 12 slightly desaturated red
          ["#d08770", "#d08770"],  # color 13 desaturated red
          ["#ebcb8b", "#ebcb8b"],  # color 14 soft orange
          ["#a3be8c", "#a3be8c"],  # color 15 desaturated green
          ["#b48ead", "#b48ead"]]  # color 16 grayish magenta


screens = [
    Screen(
        top=bar.Bar(
            [
                # widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
                widget.TextBox(
                    # background=colors[1],
                    font='Ubuntu Nerd Font',
                    fontsize=24,
                    foreground=colors[6],
                    padding=0,
                    text=''
                ),
                widget.Image(filename="~/.config/qtile/icons/Launch.png", iconsize=10,
                             background=colors[6], mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('rofi -show run')}),
                widget.TextBox(
                    # background=colors[1],
                    font='Ubuntu Nerd Font',
                    fontsize=24,
                    foreground=colors[6],
                    padding=0,
                    text=''
                ),
                widget.Spacer(length=10),
                # widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
                # widget.CurrentLayout(),
                widget.TextBox(
                    # background=colors[1],
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
                    # hide_unused=True,
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
                widget.Sep(
                    background=colors[6], foreground=colors[13], linewidth=2, padding=10),
                widget.Prompt(
                    background=colors[6],
                    foreground=colors[1],
                    fontsize=18,
                    prompt='',
                    bell_style='audible'

                ),
                widget.Sep(
                    background=colors[6], foreground=colors[13], linewidth=2, padding=10),
                widget.TextBox(
                    # background=colors[1],
                    font='Ubuntu Nerd Font',
                    fontsize=24,
                    foreground=colors[6],
                    padding=0,
                    text=''
                ),

                # widget.WindowName(),
                widget.Spacer(),
                # widget.Chord(
                #     chords_colors={
                #         "launch": ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),
                #widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.TextBox(
                    #  background=colors[1],
                    font='Ubuntu Nerd Font',
                    fontsize=24,
                    foreground=colors[6],
                    padding=0,
                    text=''
                ),
                widget.Sep(
                    background=colors[6], foreground=colors[13], linewidth=2, padding=10),
                widget.CheckUpdates(
                    no_update_string='',
                    colour_have_updates=colors[12],
                    background=colors[6],
                    foreground=colors[1],
                ),
                widget.Sep(
                    background=colors[6], foreground=colors[13], linewidth=2, padding=10),
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
                    # step=
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
                # widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
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
                    # emoji=True,
                    # fmt='{}',
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
                # widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
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
                # widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
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
                # widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
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
                # widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
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
                    # mouse_callbacks={}
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
                    custom_icon_paths=[os.path.expanduser(
                        "~/.config/qtile/icons")],
                    foreground=colors[6],  # e5e9f0
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
                # widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
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
                    # font='Ubuntu',
                    # fontsize=12,
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
                # widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
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
                # widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
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
                    # mouse_callbacks={}
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
                # widget.Sep(background=colors[6],foreground=colors[13],linewidth=2,padding=10),
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
                    # font='Ubuntu',
                    # fontsize=12,
                    format='{down} ↓ ',
                    # interface='all',
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
        # margin=5,
        # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
        # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
    ),
]
