from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_url, send_button_carousel, show_recent_games, show_standings, send_button_message, show_todays_mvp, show_players, show_player_menu, show_teams, show_team_menu, send_leader_carousel, show_leader_points, start_draft_mocking

import pyimgur


CLIENT_ID = "b25f2d4c262e825"



class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_fsm(self, event):
        text = event.message.text
        return text.lower() == "fsm"

    def is_going_to_start(self,event):
        text = event.message.text
        return True

    def is_going_to_showgame(self,event):
        text = event.message.text
        return text.lower() == "watch games"

    def is_going_to_showstandings(self,event):
        text = event.message.text
        return text.lower() == "analysis"

    def is_going_to_east(self,event):
        text = event.message.text
        return text.lower() == "east"

    def is_going_to_west(self,event):
        text = event.message.text
        return text.lower() == "west"

    def is_going_to_mvp(self,event):
        text = event.message.text
        return text.lower() == "mvp"

    def is_going_to_player(self,event):
        text = event.message.text
        return text.lower() == "player"

    def is_going_to_searchplayer(self,event):
        text = event.message.text
        return True

    def is_going_to_team(self,event):
        text = event.message.text
        return text.lower() == "team"

    def is_going_to_searchteam(self,event):
        text = event.message.text
        return True

    def is_going_to_leader(self,event):
        text = event.message.text
        return text.lower() == "leader"

    def is_going_to_point(self,event):
        text = event.message.text
        return text.lower() == "point leader"

    def is_going_to_rebound(self,event):
        text = event.message.text
        return text.lower() == "rebound leader"

    def is_going_to_assist(self,event):
        text = event.message.text
        return text.lower() == "assist leader"

    def is_going_to_steal(self,event):
        text = event.message.text
        return text.lower() == "steal leader"

    def is_going_to_block(self,event):
        text = event.message.text
        return text.lower() == "block leader"

    def is_going_to_draft(self,event):
        text = event.message.text
        return text.lower() == "start draft"

    def is_going_back_to_start(self,event):
        text = event.message.text
        return text.lower() == "menu"


    def on_enter_start(self, event):
        print("I'm entering start")
        userid = event.source.user_id
        send_button_carousel(userid)

    
    def on_enter_fsm(self,event):
        print("I am entering fsm")

        reply_token = event.reply_token
        im = pyimgur.Imgur(CLIENT_ID)
        image = im.get_image("S0ce0Ol")
        send_image_url(reply_token, image.link)


    def on_enter_showgame(self, event):
        print("I am entering showgame")
        reply_token = event.reply_token
        show_recent_games(reply_token)

    def on_enter_showstandings(self, event):
        print("I am entering showstandings")
        user_id = event.source.user_id
        send_button_message(user_id)


    def on_enter_east(self, event):
        print("I am entering east")
        reply_token = event.reply_token
        show_standings(reply_token,"east")

    def on_enter_west(self, event):
        print("I am entering west")
        reply_token = event.reply_token
        show_standings(reply_token,"west")

    def on_enter_mvp(self,event):
        print("I am entering mvp")
        reply_token = event.reply_token
        show_todays_mvp(reply_token)

    def on_enter_player(self,event):
        print("I am entering player")
        reply_token = event.reply_token
        show_player_menu(reply_token)
        
    def on_enter_searchplayer(self,event):
        print("Enter search")
        reply_token = event.reply_token
        name = event.message.text
        show_players(reply_token,name)

    def on_enter_team(self,event):
        print("Enter team")
        reply_token = event.reply_token
        show_team_menu(reply_token)

    def on_enter_searchteam(self,event):
        print("Enter search")
        reply_token = event.reply_token
        name = event.message.text
        show_teams(reply_token,name)

    def on_enter_leader(self,event):
        print("Enter leader")
        userid = event.source.user_id
        send_leader_carousel(userid)

    def on_enter_point(self,event):
        print("Points")
        reply_token = event.reply_token
        show_leader_points(reply_token,"leaders_pts","points")
    
    def on_enter_rebound(self,event):
        print("Rebounds")
        reply_token = event.reply_token
        show_leader_points(reply_token,"leaders_trb","rebounds")

    def on_enter_assist(self,event):
        print("Assists")
        reply_token = event.reply_token
        show_leader_points(reply_token,"leaders_ast","assists")

    def on_enter_steal(self,event):
        print("Steals")
        reply_token = event.reply_token
        show_leader_points(reply_token,"leaders_stl","steals")

    def on_enter_block(self,event):
        print("Blocks")
        reply_token = event.reply_token
        show_leader_points(reply_token,"leaders_blk","blocks")

    def on_enter_draft(self,event):
        print("Draft")
        reply_token = event.reply_token
        start_draft_mocking(reply_token)
