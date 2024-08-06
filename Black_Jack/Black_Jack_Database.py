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
    "\033[91m": "Red",
    "\033[92m": "Green",
    "\033[0m": "Reset"
}

# Close card representation
close_card = [
    f"{color_code_map.get('Green')}┌─────────────┐{color_code_map.get('Reset')}",
    f"{color_code_map.get('Green')}|░░░░░░░░░░░░░|{color_code_map.get('Reset')}",
    f"{color_code_map.get('Green')}|░░░░░░░░░░░░░|{color_code_map.get('Reset')}",
    f"{color_code_map.get('Green')}|░░░░░░░░░░░░░|{color_code_map.get('Reset')}",
    f"{color_code_map.get('Green')}|░░░░░░░░░░░░░|{color_code_map.get('Reset')}",
    f"{color_code_map.get('Green')}|░░░░░░░░░░░░░|{color_code_map.get('Reset')}",
    f"{color_code_map.get('Green')}|░░░░░░░░░░░░░|{color_code_map.get('Reset')}",
    f"{color_code_map.get('Green')}|░░░░░░░░░░░░░|{color_code_map.get('Reset')}",
    f"{color_code_map.get('Green')}└─────────────┘{color_code_map.get('Reset')}",
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

