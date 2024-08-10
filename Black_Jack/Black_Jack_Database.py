# Logo
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |                
      `------'                           |__/           
"""

color_code_map = {
    "red": "\033[91m",
    "green": "\033[92m",
    "reset": "\033[0m"
}

# Close card representation
close_card = [
    f"{color_code_map.get('green')}┌─────────────┐{color_code_map.get('reset')}",
    f"{color_code_map.get('green')}|░░░░░░░░░░░░░|{color_code_map.get('reset')}",
    f"{color_code_map.get('green')}|░░░░░░░░░░░░░|{color_code_map.get('reset')}",
    f"{color_code_map.get('green')}|░░░░░░░░░░░░░|{color_code_map.get('reset')}",
    f"{color_code_map.get('green')}|░░░░░░░░░░░░░|{color_code_map.get('reset')}",
    f"{color_code_map.get('green')}|░░░░░░░░░░░░░|{color_code_map.get('reset')}",
    f"{color_code_map.get('green')}|░░░░░░░░░░░░░|{color_code_map.get('reset')}",
    f"{color_code_map.get('green')}|░░░░░░░░░░░░░|{color_code_map.get('reset')}",
    f"{color_code_map.get('green')}└─────────────┘{color_code_map.get('reset')}",
]

# Types of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

card_symbols = {
    'spade': '♠',
    'heart': '♥',
    'diamond': '♦',
    'club': '♣',
    'closeCard': close_card
}

