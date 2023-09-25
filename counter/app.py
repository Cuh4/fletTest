# ----------------------------------------------------
# ----- // GUI
# ----------------------------------------------------

# -- // Imports
import flet

# -- // Variables

# -- // GUI
def main(page: flet.Page):
    # // Handlers
    # Add Button
    def addHandler(button: flet.IconButton):
        count.value = str(int(count.value) + 1)
        page.update()
    
    # Subtract Button 
    def subtractHandler(button: flet.IconButton):
        count.value = str(int(count.value) - 1)
        page.update()
    
    # // Creation
    # Page
    page.title = "Simple Counter"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    
    page.fonts = {
        "Montserrat" : "fonts/MontSerrat-Regular.ttf"
    }
    
    page.window_width = 400
    page.window_height = 200
    page.window_resizable = False
    page.window_maximizable = False
    
    # Components
    title = flet.Text(
        value="Simple Counter",
        text_align=flet.TextAlign.CENTER,
        size=25,

        style=flet.TextStyle(
            weight=flet.FontWeight.BOLD,
            font_family="Montserrat"
        )
    )
    
    author = flet.Text(
        value="By Cuh4",
        text_align=flet.TextAlign.CENTER,
        size=10,

        style=flet.TextStyle(
            font_family="Montserrat"
        )
    )
    
    count = flet.TextField(
        value="0",
        text_align=flet.TextAlign.CENTER,
        width=100,
        border_color=flet.colors.WHITE,
        text_size=25,

        text_style=flet.TextStyle(
            weight=flet.FontWeight.BOLD,
            font_family="Montserrat"
        )
    )

    subtractButton = flet.IconButton(
        icon=flet.icons.REMOVE,
        tooltip="Subtract",
        on_click=subtractHandler,
        icon_color=flet.colors.RED_200
    )
    
    addButton = flet.IconButton(
        icon=flet.icons.ADD,
        tooltip = "Add",
        on_click=addHandler,
        icon_color=flet.colors.LIGHT_GREEN_200
    )
    
    # // Finalization
    page.add(
        title,
        author,
        
        flet.Row(
            [
                subtractButton,
                count,
                addButton
            ],

            alignment=flet.MainAxisAlignment.CENTER
        )
    )