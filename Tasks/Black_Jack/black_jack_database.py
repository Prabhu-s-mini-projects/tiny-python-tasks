""" Resources needed for black jack game"""
# Logo
LOGO = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |                
      `------'                           |__/           
"""

COLOR_CODE_MAP = {
    "red": "\033[91m",
    "green": "\033[92m",
    "reset": "\033[0m"
}

# Close card representation
CLOSE_CARD = [
    f"{COLOR_CODE_MAP.get('green')}┌─────────────┐{COLOR_CODE_MAP.get('reset')}",
    f"{COLOR_CODE_MAP.get('green')}|░░░░░░░░░░░░░|{COLOR_CODE_MAP.get('reset')}",
    f"{COLOR_CODE_MAP.get('green')}|░░░░░░░░░░░░░|{COLOR_CODE_MAP.get('reset')}",
    f"{COLOR_CODE_MAP.get('green')}|░░░░░░░░░░░░░|{COLOR_CODE_MAP.get('reset')}",
    f"{COLOR_CODE_MAP.get('green')}|░░░░░░░░░░░░░|{COLOR_CODE_MAP.get('reset')}",
    f"{COLOR_CODE_MAP.get('green')}|░░░░░░░░░░░░░|{COLOR_CODE_MAP.get('reset')}",
    f"{COLOR_CODE_MAP.get('green')}|░░░░░░░░░░░░░|{COLOR_CODE_MAP.get('reset')}",
    f"{COLOR_CODE_MAP.get('green')}|░░░░░░░░░░░░░|{COLOR_CODE_MAP.get('reset')}",
    f"{COLOR_CODE_MAP.get('green')}└─────────────┘{COLOR_CODE_MAP.get('reset')}",
]

# Types of cards
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

CARD_SYMBOLS = {
    'spade': '♠',
    'heart': '♥',
    'diamond': '♦',
    'club': '♣',
    'closeCard': CLOSE_CARD
}
