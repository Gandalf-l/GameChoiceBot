from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

genres = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text="Action"),
      KeyboardButton(text="Simulation"),
      KeyboardButton(text="Indie")
    ],
    [
      KeyboardButton(text="Strategy"),
      KeyboardButton(text="Casual"),
      KeyboardButton(text="RPG")
    ],
    [
      KeyboardButton(text="Racing"),
      KeyboardButton(text="Adventure"),
      KeyboardButton(text="Massively Multiplayer")
    ],
    [
      KeyboardButton(text="Utilities"),
      KeyboardButton(text="Animation & Modeling"),
      KeyboardButton(text="Free to Play")
    ],
    [
      KeyboardButton(text="Audio Production"),
      KeyboardButton(text="Design & Illustration"),
      KeyboardButton(text="Monolith Productions")
    ],
    [
      KeyboardButton(text="Sports"),
      KeyboardButton(text="Video Production"),
      KeyboardButton(text="Web Publishing")
    ]
  ],
  resize_keyboard=True
)

price = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text="Free(0$)"),
      KeyboardButton(text="5$"),
      KeyboardButton(text="10$")
    ],
    [
      KeyboardButton(text="15$"),
      KeyboardButton(text="20$"),
      KeyboardButton(text="30$")
    ],
    [
      KeyboardButton(text="40$"),
      KeyboardButton(text="50$"),
      KeyboardButton(text="100$")
    ]
  ],
  resize_keyboard=True
)

platform = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text="PC"),
      KeyboardButton(text="Xbox one"),
      KeyboardButton(text="Xbox 360")
    ],
    [
      KeyboardButton(text="PS3"),
      KeyboardButton(text="PS4")
    ]
  ],
  resize_keyboard=True
)

operatingSystem = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text="Windows"),
      KeyboardButton(text="Linux"),
      KeyboardButton(text="Mac OS")
    ]
  ],
  resize_keyboard=True
)

languages = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text="English"),
      KeyboardButton(text="Czech"),
      KeyboardButton(text="Danish")
    ],
    [
      KeyboardButton(text="Dutch"),
      KeyboardButton(text="Finnish"),
      KeyboardButton(text="French")
    ],
    [
      KeyboardButton(text="German"),
      KeyboardButton(text="Hungarian"),
      KeyboardButton(text="Italian")
    ],
    [
      KeyboardButton(text="Japanese"),
      KeyboardButton(text="Korean"),
      KeyboardButton(text="Norwegian")
    ],
    [
      KeyboardButton(text="Polish"),
      KeyboardButton(text="Portuguese"),
      KeyboardButton(text="Romanian")
    ],
    [
      KeyboardButton(text="Russian"),
      KeyboardButton(text="Swedish"),
      KeyboardButton(text="Turkish")
    ],
    [
      KeyboardButton(text="Bulgarian"),
      KeyboardButton(text="Ukrainian"),
      KeyboardButton(text="Greek")
    ]
  ],
  resize_keyboard=True
)

start = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text="Subscription"),
      KeyboardButton(text="Recommend")
    ]
  ],
  resize_keyboard=True
)

subscribe = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text="Subscribe to newsletter")
    ],
    [
      KeyboardButton(text="Back")
    ]
  ],
  resize_keyboard=True
)

unsubscribe = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text="Unsubscribe to newsletter")
    ],
    [
      KeyboardButton(text="Back")
    ]
  ],
  resize_keyboard=True
)