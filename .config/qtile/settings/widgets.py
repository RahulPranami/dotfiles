from libqtile import widget
# from .theme import colors


# def workspaces():
#    return [
#            widget.GroupBox(),
#            widget.WindowName(),
#    ]

primary_widgets = [
        widget.CurrentLayout(),
#        *workspaces(),
        widget.GroupBox(),
        widget.Prompt(),
        widget.WindowName(),
        widget.Systray(),
        widget.Clock(format = "%Y-%m-%d %a %I:%M %p"),
        widget.QuickExit(),
        ]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    # padding=1,
)

extension_defaults = widget_defaults.copy()
