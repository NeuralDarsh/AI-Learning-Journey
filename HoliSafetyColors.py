# Generates random vibrant colors and checks their brightness 'safety'

import random

def generate_holi_color():
    # Generating random RGB values
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    # Converting to Hex format
    hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    
    # Safety Check: Calculate Brightness (Luminance)
    # Formula: (0.299*R + 0.587*G + 0.114*B)
    brightness = (0.299 * r) + (0.587 * g) + (0.114 * b)
    
    return hex_color, brightness

if __name__ == "__main__":
    print("--- 🎨 Happy Holi & National Safety Day! 🎨 ---")
    print("Generating 5 vibrant colors for your next UI project:\n")
    
    for i in range(5):
        color, level = generate_holi_color()
        # If brightness is low, it's 'safe' for white text. If high, use black text.
        safety_tip = "Use BLACK text" if level > 128 else "Use WHITE text"
        
        print(f"Color {i+1}: {color.upper()} | Brightness: {level:.2f} | 🛡️ Tip: {safety_tip}")

    print("\nGo enjoy the real colors now! Happy Holi!")