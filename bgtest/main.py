# ----------------------------------------------------
# ----- // Background Test
# ----------------------------------------------------

# -- // Imports
import flet
import modules

# -- // GUI
def main(page: flet.Page):
    # // Creation
    # Page
    page.title = "Background Test"

    page.fonts = {
        "Montserrat" : "fonts/MontSerrat-Regular.ttf",
        "MontserratBold" : "fonts/MontSerrat-Bold.ttf",
        "MontserratBlack" : "fonts/MontSerrat-Black.ttf"
    }
    
    page.window_width = 500
    page.window_height = 500
    
    # // Finalization
    page.padding = 0

    page.add(
        flet.Container(
            gradient = flet.LinearGradient(
                colors = [
                    modules.misc.RGBToHex(255, 125, 55),
                    modules.misc.RGBToHex(55, 55, 255)
                ],
                
                rotation = 45
            ),
            
            expand = True
        )
    )
    
flet.app(main)