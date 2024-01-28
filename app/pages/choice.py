from taipy.gui import notify, Markdown

user = None
formatted_places = "Default"

def on_init(state):
    print("on init (choice)")
    print(state.user)
    state.user = state.user

def on_navigate(state, page_name):
    # if page_name == "results" and not state.results_ready:
    #     return "no_results"
    # return page_name
    print("on_navigate")

myProperty = {
    "name": "Press any button to start!",
    "gym": 0,
    "supermarket": 0,
    "trainStation": 0,
    "restaurant": 0,
    "image": "app/static/img/royalhackerway.webp"
}

# Definition of the page
choice_md = Markdown("""
<|container|

<br />

<|layout|class_name=d-flex top_layout|

<|app/static/img/logo-transparent.png|image|label=this is an image|width=30px|height=30px|> <|Domus.ai|text|class_name=big_font|>

[<|Logout|button|hover_text=View/Edit profile|class_name=secondary|>](/logout)

|>
                     
<br />



<|layout|columns=4 8|columns[mobile]=1|class_name=buttons_layout|

<|{myProperty.image}|image|label=this is an image|>

<second|
<|{myProperty.name}|text|class_name=big_font|>
                     
### Distance to your closest... 

<|Gym: {myProperty.gym}|>

<|Supermarket: {myProperty.supermarket}|>

<|Train Station: {myProperty.trainStation}|>

<|Restaurant: {myProperty.restaurant}|>                           

|second>
                     
|>

<br />
                     
<|layout|columns=1 1 1|columns[mobile]=1 1 1|class_name=buttons_layout|

<|✗|button|hover_text=I hate this|on_action=add_to_dislikes|class_name=error bigbtn|>

<|✓|button|hover_text=I like this|on_action=add_to_likes|class_name=success bigbtn|>

<|+|button|hover_text=Add to saved|on_action=add_to_saved|class_name=secondary bigbtn|>

|>

<br />
|>
""")

# My text: <|{text}|>

# <|{text}|input|>

# <|Run local|button|on_action=on_button_action|>

def add_to_saved(state):
    state.myProperty = {
        "name": "Royal Holloway",
        "gym": 20,
        "supermarket": 30,
        "trainStation": 40,
        "restaurant": 50,
        "image": "app/static/img/test.jpeg"
    }
    state.user = state.prevUser
    notify(state,'success','Property saved')
    # TODO: communication with DB

def add_to_likes(state):
    state.myProperty = {
        "name": "Royal Holloway",
        "gym": 20,
        "supermarket": 30,
        "trainStation": 40,
        "restaurant": 50,
        "image": "app/static/img/test.jpeg"
    }
    state.user = state.prevUser
    notify(state,'success','Property saved')
    # TODO: communication with DB

def add_to_dislikes(state):
    state.myProperty = {
        "name": "Royal Holloway",
        "gym": 20,
        "supermarket": 30,
        "trainStation": 40,
        "restaurant": 50,
        "image": "app/static/img/test.jpeg"
    }
    state.user = state.prevUser
    notify(state,'success','Property saved')
    # TODO: communication with DB

def display_abouts(state):
    pass

def on_button_action(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"





