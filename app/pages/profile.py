from taipy.gui import Markdown, navigate
import pyperclip
import json

from app.pages.choice import choice_md

def on_init(state):
    print("on init (profile)")

token = None

username = None
email = None
budgetMin = None
budgetMax = None
region = None
travellingMode = None
place = None
prevUser = None
numberOfBedroom = None

# <username|
# ## **Name**{: .color-primary}

# <|{username}|input|label=Name|on_change=set_username|>
# |username>

# <email|
# ## **Email**{: .color-primary}

# <|{email}|input|label=Email|>
# |email>

profile_md = Markdown("""
<|layout|columns=1 1 1|gap=30px|

<budget|
## **Budget per month**{: .color-primary}

£ <|{budgetMin}|input|label=Min|class_name=short_label|> - £ <|{budgetMax}|input|label=Max|class_name=short_label|>
|budget>

<region|
## **Region**{: .color-primary}

<|{region}|input|label=Region|>
|region>

<travellingMode|
## Preferred **travelling**{: .color-primary} mode

<|{travellingMode}|selector|lov=Walking;Cycling;Public Transport;Driving|dropdown|>     

|travellingMode>
                                     
|>
                      
<numberOfBedroom|
## **Number of Rooms**{: .color-primary}

<|{numberOfBedroom}|input|label=Number of Room|>
|numberOfBedroom>
                      
|>
                                                        
<place|
## Tell us **where**{: .color-primary} you work/ study

<|{place}|input|label=e.g. Grocery store, gym, Royal Holloway|class_name=fullwidth|>
|place>
                               
<br />
<|Create Accountt|button|on_action=create_account|label=Generate text|class_name=success text-center|>
                      
"""
)

def create_account(state):
    token = None
    try:
        print("PASTE",pyperclip.paste())
        token = json.loads(pyperclip.paste())
        print("token decoded")
    except:
        print("invalid token")
    state.token = token

    # places = state.placesString.split(',')
    userData = {
        "email": token["userinfo"]["email"],
        "budgetMin": state.budgetMin,
        "budgetMax": state.budgetMax,
        "region": state.region,
        "travellingMode": state.travellingMode,
        "place": state.place,
        "numberOfBedroom": state.numberOfBedroom
        # "places": state.placesString,
    }
    state.prevUser = userData
    print(userData)
    navigate(state,to="choice")
    #TODO: save this to DB

def on_navigate(state, page_name):
    # if page_name == "results" and not state.results_ready:
    #     return "no_results"
    # return page_name
    print("on_navigate")
