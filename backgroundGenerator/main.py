from PIL import Image, ImageDraw, ImageFont

def create_wallpaper(shortcuts,
                     image_size=(1920, 1080),
                     background_color=(30, 30, 30),
                     text_color=(255, 255, 255),
                     font_path=None,  # Provide a path to a .ttf file if available.
                     font_size=80,
                     output_file="wallpaper.png"):
    # Create a new image with the given background color.
    image = Image.new("RGB", image_size, color=background_color)
    draw = ImageDraw.Draw(image)
    
    # Try to load the specified TrueType font, or fallback to the default font.
    if font_path:
        try:
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            print("Could not load the font. Falling back to default.")
            font = ImageFont.load_default()
    else:
        font = ImageFont.load_default()
    
    # Starting coordinates for text.
    x, y = 50, 50
    # Calculate the height of a line of text.
    line_height = 50

    # Draw each shortcut on the image.
    for shortcut in shortcuts:
        draw.text((x, y), shortcut, fill=text_color, font=font)
        y += line_height  # Move down for the next shortcut

    # Save the final wallpaper image.
    image.save(output_file)
    print(f"Wallpaper saved as {output_file}")

if __name__ == "__main__":
    # List of macOS shortcuts to display.
    macos_shortcuts = [
        "Command + C: Copy",
        "Command + V: Paste",
        "Command + X: Cut",
        "Command + Z: Undo",
        "Command + Shift + Z: Redo",
        "Command + A: Select All",
        "Command + F: Find",
        "Command + H: Hide Window",
        "Command + Q: Quit Application",
        "Option + Command + Esc: Force Quit"
    ]
    
    # Call the function to create the wallpaper.
    create_wallpaper(macos_shortcuts)
