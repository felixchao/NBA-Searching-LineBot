from fsm import TocMachine


def create_machine():
  machine = TocMachine(
    states=["user", "start", "fsm", "showgame", "showstandings", "east", "west", 'mvp', 'player', 'searchplayer','team','searchteam','leader','point','rebound','assist','steal','block'],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "start",
            "conditions": "is_going_to_start",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "fsm",
            "conditions": "is_going_to_fsm",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "showgame",
            "conditions": "is_going_to_showgame",
        },
        {
            "trigger": "advance",
            "source": ["start","west","east"],
            "dest": "showstandings",
            "conditions": "is_going_to_showstandings",
        },
        {
            "trigger": "advance",
            "source": ["showstandings","west"],
            "dest": "east",
            "conditions": "is_going_to_east",
        },
        {
            "trigger": "advance",
            "source": ["showstandings","east"],
            "dest": "west",
            "conditions": "is_going_to_west",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "mvp",
            "conditions": "is_going_to_mvp",
        },
        {
            "trigger": "advance",
            "source": ["start","searchplayer","mvp",'searchteam','point','rebound','assist','steal','block'],
            "dest": "player",
            "conditions": "is_going_to_player",
        },
        {
            "trigger": "advance",
            "source": "player",
            "dest": "searchplayer",
            "conditions": "is_going_to_searchplayer",
        },
        {
            "trigger": "advance",
            "source": ["start","searchteam","west",'east','showstandings','showgame','searchplayer'],
            "dest": "team",
            "conditions": "is_going_to_team",
        },
        {
            "trigger": "advance",
            "source": "team",
            "dest": "searchteam",
            "conditions": "is_going_to_searchteam",
        },
        {
            "trigger": "advance",
            "source": ["start","point","rebound",'assist','steal','block'],
            "dest": "leader",
            "conditions": "is_going_to_leader",
        },
        {
            "trigger": "advance",
            "source": "leader",
            "dest": "point",
            "conditions": "is_going_to_point",
        },
        {
            "trigger": "advance",
            "source": "leader",
            "dest": "rebound",
            "conditions": "is_going_to_rebound",
        },
        {
            "trigger": "advance",
            "source": "leader",
            "dest": "assist",
            "conditions": "is_going_to_assist",
        },
        {
            "trigger": "advance",
            "source": "leader",
            "dest": "steal",
            "conditions": "is_going_to_steal",
        },
        {
            "trigger": "advance",
            "source": "leader",
            "dest": "block",
            "conditions": "is_going_to_block",
        },
        {
            "trigger": "advance",
            "source": ["showgame","fsm","showstandings","east","west","mvp",'player','searchplayer','team','searchteam','leader','point','rebound','assist','steal','block'],
            "dest": "start",
            "conditions": "is_going_back_to_start",
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
   )
  return machine