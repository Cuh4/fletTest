# ----------------------------------------------------
# ----- // GUI
# ----------------------------------------------------

# -- // Imports
import flet
import modules
import webbrowser

# -- // Variables

# -- // GUI
def main(page: flet.Page):
    # // Handlers
    # Launch Stormworks
    def launchButtonHandler(button: flet.IconButton):
        webbrowser.open("steam://rungameid/573090")
    
    # // Creation
    # Page
    page.title = "Stormworks Launcher"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    
    page.fonts = {
        "Montserrat" : "fonts/MontSerrat-Regular.ttf",
        "MontserratBold" : "fonts/MontSerrat-Bold.ttf",
        "MontserratBlack" : "fonts/MontSerrat-Black.ttf"
    }
    
    page.window_width = 500
    page.window_height = 150
    page.window_resizable = False
    page.window_maximizable = False
    
    # Components
    titleText = flet.Text(
        value="Stormworks Launcher",
        text_align=flet.TextAlign.CENTER,
        size=30,
        color=modules.misc.RGBToHex(255, 255, 255),
    )
    
    authorText = flet.Text(
        value="By Cuh4",
        text_align=flet.TextAlign.CENTER,
        size=15,
        color=modules.misc.RGBToHex(200, 200, 200),

        style=flet.TextStyle(
            font_family="MontserratBlack"
        )
    )
    
    iconImage = flet.Image(
        src="images/swicon.png",
        width=50,
        height=50,
    )
    
    launchButton = flet.TextButton(
        text="Launch Stormworks",
        on_click=launchButtonHandler,
        width=200,
        height =50,
        
        style=flet.ButtonStyle(
            color=modules.misc.RGBToHex(255, 255, 255),
            bgcolor=modules.misc.RGBToHex(25, 25, 25)
        )
    )
    
    # // Finalization
    page.padding = 0

    page.add(
        flet.Stack(
            [
                flet.Container(
                    image_src="images/background.png",
                    image_fit=flet.ImageFit.COVER,
                    expand=True,

                    width=page.window_width,
                    height=page.window_height,
                ),
                
                flet.Container(
                    bgcolor=modules.misc.RGBToHex(5, 5, 5),
                    opacity=0.8,
                    height=40
                ),
                
                flet.Row(
                    [
                        iconImage,
                        titleText,
                        authorText,
                    ],
                    
                    alignment=flet.MainAxisAlignment.CENTER,
                    height = 40
                ),
                
                flet.Row(
                    [
                        launchButton
                    ],
                    
                    alignment=flet.MainAxisAlignment.CENTER,
                    height=160
                )
            ]
        )
    )
    