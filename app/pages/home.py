from taipy.gui import Markdown, navigate

home_md = Markdown("""
<|container|id=home_container
<|app/static/img/logo-big.png|image|label=our logo|id=home_logo|width=500px|>

<br />

<br />
                   
[<|Login / sign up|button|hover_text=Add to saved|class_name=secondary|>
|>](/login)
""")

# <|{username}|input|label=Username|>
                   
# <|{password}|input|label=Password|>
