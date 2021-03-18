init python:
    # Window Info
    window_subtitle = renpy.version()[:12]
    config.window_title = u"" +window_subtitle+ " '" +renpy.version_name+"' " 
    
    # Dark Theme
    config.defer_styles = True
    # The color of non-interactive text

    
    TEXT = "#D3D3D3"

    # Colors for buttons in various states.
    IDLE = "#2E9FE9"
    HOVER = "#ff7f7f"
    DISABLED = "#95a5a6"

    # Colors for reversed text buttons (selected list entries).
    REVERSE_IDLE = "#ff7f7f"
    REVERSE_HOVER = "#bfc9ca"
    REVERSE_TEXT = "#ffff"

    # Colors for the scrollbar thumb.
    SCROLLBAR_IDLE = "#ff7f7f"
    SCROLLBAR_HOVER = "#bfc9ca"

    # A displayable used for the background of everything.
    BACKGROUND = "images/dark/background.png"

    # An image used as a separator pattern.
    PATTERN = "images/pattern.png"

    # A displayable used for the background of windows
    # containing commands, preferences, and navigation info.
    WINDOW = Frame("images/dark/window.png", 0, 0, tile=True)

    # A displayable used for the background of the projects list.
    PROJECTS_WINDOW = Null()

    # A displayable used the background of information boxes.
    INFO_WINDOW = "#2c2c2c"

    # Colors for the titles of information boxes.
    ERROR_COLOR = "#f5b7b1"
    INFO_COLOR = "#a9cce3"
    INTERACTION_COLOR = "#fcf3cf"
    QUESTION_COLOR = "#fcf3cf"

    # The color of input text.
    INPUT_COLOR = "#d0d3d4"
