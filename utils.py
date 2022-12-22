import os
import bs4
import requests
import numpy as np
from bs4 import BeautifulSoup
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, MessageTemplateAction, TemplateSendMessage, CarouselTemplate, CarouselColumn, ButtonsTemplate,ImageCarouselTemplate, URITemplateAction, ImageCarouselColumn, FlexSendMessage
from fake_useragent import UserAgent
import random

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

user_agent = UserAgent()

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    print(channel_access_token)
    return "OK"


def send_image_url(id, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(id, ImageSendMessage(
        preview_image_url=img_url,
        original_content_url=img_url
    ))

    return "OK"

def send_button_message(id):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(id, TemplateSendMessage(
       alt_text='Buttons',
       template = ButtonsTemplate(
         thumbnail_image_url = 'https://cdn.nba.com/manage/2022/04/Full-Play-In-Tournament-Bracket-16x9-1-768x432-copy.png',
         title = 'Conference Standings',
         text = 'find east or west season\'s standings',
         actions = [
            MessageTemplateAction(
               label = 'West',
               text = 'west'
            ),
            MessageTemplateAction(
               label = 'East',
               text = 'east'
            ),
         ]
       )
    ))
    return "OK"

def send_image_carousel(reply_token,img_url,name, uri):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TemplateSendMessage(
       alt_text='Image Carousel',
       template = ImageCarouselTemplate(
         columns = [
            ImageCarouselColumn(
                image_url= img_url,
                action=URITemplateAction(
                    label= name,
                    uri = uri
                )
            ),
         ]
       )
    ))
    return "OK"


def send_button_carousel(id):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(id, TemplateSendMessage(
        alt_text='Carousel',
        template = CarouselTemplate(
            columns=[
            CarouselColumn(
                thumbnail_image_url = 'https://img.washingtonpost.com/wp-apps/imrs.php?src=https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/WEIKA36KCVFA5GNFAE5IPZMFLE.jpg&w=1800',
                title='NBA Todays',
                text='search for the recent games!',
                actions=[
                    MessageTemplateAction(
                        label='Watch games',
                        text='watch games',
                    ),
                    MessageTemplateAction(
                        label='Todays MVPs',
                        text='mvp',
                    ),
                    MessageTemplateAction(
                        label='Analysis',
                        text='analysis'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url = 'https://img.washingtonpost.com/wp-apps/imrs.php?src=https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/JI4CISXQ75HFXCEZYCI3BIAI4I.jpg&w=1800',
                title='Searching Options',
                text='search for your favorite players!',
                actions=[
                    MessageTemplateAction(
                        label='Show Player List',
                        text='player',
                    ),
                    MessageTemplateAction(
                        label='Show Team List',
                        text='team',
                    ),
                    MessageTemplateAction(
                        label='Leaders In NBA',
                        text='leader'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url = 'https://hoopshabit.com/wp-content/uploads/imagn-images/2017/07/12702527.jpeg',
                title='Draft Mocking',
                text='for the future!',
                actions=[
                    MessageTemplateAction(
                        label='start draft',
                        text='start draft',
                    ),
                    MessageTemplateAction(
                        label='None',
                        text='none',
                    ),
                    MessageTemplateAction(
                        label='None',
                        text='none'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url = 'https://www.itemis.com/hubfs/yakindu/statechart-tools/documentation/images/overview_simple_moore.jpg',
                title='Finite State Machine',
                text='check for fsm!',
                actions=[
                    MessageTemplateAction(
                        label='FSM',
                        text='fsm',
                    ),
                    MessageTemplateAction(
                        label='None',
                        text='none',
                    ),
                    MessageTemplateAction(
                        label='None',
                        text='none'
                    )
                ]
            ),
        ]
      )
    )
    )
    return "OK"

def send_leader_carousel(id):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(id, TemplateSendMessage(
        alt_text='Carousel',
        template = CarouselTemplate(
            columns=[
            CarouselColumn(
                thumbnail_image_url = 'https://upload.wikimedia.org/wikipedia/en/9/93/Wilt_Chamberlain_100-point.jpg',
                title='Points Leader',
                text='search for highest!',
                actions=[
                    MessageTemplateAction(
                        label='Point leader',
                        text='point leader',
                    ),
                ]
            ),
            CarouselColumn(
                thumbnail_image_url = 'https://dygtyjqp7pi0m.cloudfront.net/i/29442/25629314_1.jpg?v=8D3D73971FBB180',
                title='Rebound leader',
                text='search for highest!',
                actions=[
                    MessageTemplateAction(
                        label='Rebound leader',
                        text='rebound leader',
                    ),
                ]
            ),
            CarouselColumn(
                thumbnail_image_url = 'https://qph.cf2.quoracdn.net/main-qimg-9d2e471dd233dba59faac02f336ec0a1-lq',
                title='Assist leader',
                text='search for highest!',
                actions=[
                    MessageTemplateAction(
                        label='Assist leader',
                        text='assist leader',
                    ),
                ]
            ),
            CarouselColumn(
                thumbnail_image_url = 'https://images2.minutemediacdn.com/image/fetch/c_fill,g_auto,f_auto,h_1559,w_1600/http%3A%2F%2Fhoopshabit.com%2Fwp-content%2Fuploads%2Fgetty-images%2F2018%2F08%2F1191301449.jpeg',
                title='Steal leader',
                text='search for highest!',
                actions=[
                    MessageTemplateAction(
                        label='Steal leader',
                        text='steal leader',
                    ),
                ]
            ),
            CarouselColumn(
                thumbnail_image_url = 'https://i.pinimg.com/originals/9a/e8/43/9ae8439ab386ed14db9ef82709f16b11.jpg',
                title='Block leader',
                text='search for highest!',
                actions=[
                    MessageTemplateAction(
                        label='Block leader',
                        text='block leader',
                    ),
                ]
            )
        ]
      )
    )
    )
    return "OK"


def send_rank_carousel(reply_token,img_urls,name,leadings):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, FlexSendMessage(
     alt_text='flex',
     contents= {
     "type": "carousel",
     "contents": [
     {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": img_urls[0],
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "gravity": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://cdn-icons-png.flaticon.com/512/3188/3188674.png",
                "align": "end",
                "margin": "none",
                "size": "md"
              }
            ],
            "position": "absolute",
            "background": {
              "type": "linearGradient",
              "angle": "0deg",
              "endColor": "#00000000",
              "startColor": "#00000099"
            },
            "width": "100%",
            "height": "40%",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": name[0],
                        "size": "xl",
                        "color": "#ffffff"
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": leadings[0],
                        "color": "#ffffff"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [],
                        "flex": 0,
                        "spacing": "lg"
                      }
                    ]
                  }
                ],
                "spacing": "xs"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "paddingAll": "20px"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": img_urls[1],
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "gravity": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://cdn-icons-png.flaticon.com/512/3188/3188675.png",
                "align": "end",
                "margin": "none"
              }
            ],
            "position": "absolute",
            "background": {
              "type": "linearGradient",
              "angle": "0deg",
              "endColor": "#00000000",
              "startColor": "#00000099"
            },
            "width": "100%",
            "height": "40%",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": name[1],
                        "size": "xl",
                        "color": "#ffffff"
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": leadings[1],
                        "color": "#ffffff"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [],
                        "flex": 0,
                        "spacing": "lg"
                      }
                    ]
                  }
                ],
                "spacing": "xs"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "paddingAll": "20px"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": img_urls[2],
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "gravity": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://cdn-icons-png.flaticon.com/512/3188/3188676.png",
                "align": "end",
                "margin": "none"
              }
            ],
            "position": "absolute",
            "background": {
              "type": "linearGradient",
              "angle": "0deg",
              "endColor": "#00000000",
              "startColor": "#00000099"
            },
            "width": "100%",
            "height": "40%",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": name[2],
                        "size": "xl",
                        "color": "#ffffff"
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": leadings[2],
                        "color": "#ffffff"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [],
                        "flex": 0,
                        "spacing": "lg"
                      }
                    ]
                  }
                ],
                "spacing": "xs"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "paddingAll": "20px"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
 }
))
    return "OK"

def send_draft_carousel(reply_token,names,images,overalls,teams):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, FlexSendMessage(
    alt_text='flex',
    contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": images[0],
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "gravity": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://img.onl/Cf0PPD",
                "align": "end",
                "offsetBottom": "none",
                "offsetEnd": "5px",
                "offsetTop": "35px"
              },
              {
                "type": "image",
                "url": teams[0],
                "align": "start",
                "margin": "none",
                "offsetBottom": "100px"
              },
              {
                "type": "text",
                "text": overalls[0],
                "align": "center",
                "offsetBottom": "140px",
                "offsetStart": "95px",
                "size": "3xl",
                "style": "italic",
                "weight": "bold",
                "color": "#DAA520"
              }
            ],
            "position": "absolute",
            "background": {
              "type": "linearGradient",
              "angle": "0deg",
              "endColor": "#00000000",
              "startColor": "#00000099"
            },
            "width": "100%",
            "height": "50%",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": names[0],
                        "size": "xl",
                        "color": "#ffffff",
                        "offsetTop": "4px"
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [],
                        "flex": 0,
                        "spacing": "lg"
                      }
                    ]
                  }
                ],
                "spacing": "xs"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "paddingAll": "20px"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": images[1],
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "gravity": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://img.onl/Cf0PPD",
                "align": "end",
                "offsetBottom": "none",
                "offsetEnd": "5px",
                "offsetTop": "35px"
              },
              {
                "type": "image",
                "url": teams[1],
                "align": "start",
                "margin": "none",
                "offsetBottom": "100px"
              },
              {
                "type": "text",
                "text": overalls[1],
                "align": "center",
                "offsetBottom": "140px",
                "offsetStart": "95px",
                "size": "3xl",
                "style": "italic",
                "weight": "bold",
                "color": "#DAA520"
              }
            ],
            "position": "absolute",
            "background": {
              "type": "linearGradient",
              "angle": "0deg",
              "endColor": "#00000000",
              "startColor": "#00000099"
            },
            "width": "100%",
            "height": "50%",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": names[1],
                        "size": "xl",
                        "color": "#ffffff",
                        "offsetTop": "4px"
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [],
                        "flex": 0,
                        "spacing": "lg"
                      }
                    ]
                  }
                ],
                "spacing": "xs"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "paddingAll": "20px"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": images[2],
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "gravity": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://img.onl/Cf0PPD",
                "align": "end",
                "offsetBottom": "none",
                "offsetEnd": "5px",
                "offsetTop": "35px"
              },
              {
                "type": "image",
                "url": teams[2],
                "align": "start",
                "margin": "none",
                "offsetBottom": "100px"
              },
              {
                "type": "text",
                "text": overalls[2],
                "align": "center",
                "offsetBottom": "140px",
                "offsetStart": "95px",
                "size": "3xl",
                "style": "italic",
                "weight": "bold",
                "color": "#DAA520"
              }
            ],
            "position": "absolute",
            "background": {
              "type": "linearGradient",
              "angle": "0deg",
              "endColor": "#00000000",
              "startColor": "#00000099"
            },
            "width": "100%",
            "height": "50%",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": names[2],
                        "size": "xl",
                        "color": "#ffffff",
                        "offsetTop": "4px"
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [],
                        "flex": 0,
                        "spacing": "lg"
                      }
                    ]
                  }
                ],
                "spacing": "xs"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "paddingAll": "20px"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
}))
    return "OK"
    
def show_recent_games(reply_token):
    url = 'https://www.basketball-reference.com/boxscores/'
    source = requests.get(url, headers={'user-agent': user_agent.random}).text
    soup = BeautifulSoup(source, 'html.parser')
    games = soup.find_all('div', class_="game_summary expanded nohover")

    result = ""
    date = soup.find('span', class_="button2 index").text
    result += ("Recent Game Date:\n{} \n\n" .format(date))

    for game in games:
        winteamname = ""
        winteam = game.find('tr', class_="winner").text
        winteamlist = winteam.partition('\n')[2].split()
        if winteamlist[len(winteamlist)-1] == 'Final':
            winteamlist.remove('Final')
        for s in winteamlist:
            if(not s.isdigit()):
                winteamname += s
                winteamname += ' '
            else:
                winpoint = s

        loseteamname = ""
        loseteam = game.find('tr', class_="loser").text
        loseteamlist = loseteam.partition('\n')[2].split()
        if loseteamlist[len(loseteamlist)-1] == 'Final':
            loseteamlist.remove('Final')
        for s in loseteamlist:
            if(not s.isdigit()):
                loseteamname += s
                loseteamname += ' '
            else:
                losepoint = s

        result += ("WinTeam:\n   \U0001f3c6:    {}\n   \U0001f3c0:    {}points\n" .format(winteamname, winpoint))
        result += ("LossTeam:\n   \U0001f40d:    {}\n   \U0001f3c0:    {}points\n\n" .format(loseteamname, losepoint))
        result += ("----------------------------------\n\n")

    send_text_message(reply_token, result)


def show_standings(reply_token, text):
     idx = 0
     result_east = "Current Season's East Conference Standing:\n\n"
     if(text == 'west'):
        idx = 1
        result_east = "Current Season's West Conference Standing:\n\n"

     url = 'https://www.basketball-reference.com/boxscores/'
     source = requests.get(url, headers={'user-agent': user_agent.random}).text
     soup = BeautifulSoup(source, 'html.parser')
     standings = soup.find_all('div', class_="table_wrapper")

     east = standings[idx].find_all('tr', class_ = "full_table")




     id_e = 1

     for team in east:
        name = team.find('th', class_='left').text
        wins = team.find('td', {'data-stat': 'wins'}).text
        loss = team.find('td', {'data-stat': 'losses'}).text
        pct = team.find('td', {'data-stat': 'win_loss_pct'}).text
        gb = team.find('td', {'data-stat': 'gb'}).text
        ppg = team.find('td', {'data-stat': 'pts_per_g'}).text
        oppg = team.find('td', {'data-stat': 'opp_pts_per_g'}).text
        
        if(id_e == 1):
           gb = "0.0"
           result_east += '\U0001f947 '
        elif(id_e == 2):
           result_east += '\U0001f948 '
        elif(id_e == 3):
           result_east += '\U0001f949 '
        elif(id_e > 3 and id_e <= 8):
           result_east += '\U0001f606 '
        elif(id_e == 9 or id_e == 10):
           result_east += '\U0001f6a8 '
        else:
           result_east += '\U000026a1 '

        result_east += name + '\n  \U0001f3c6: ' + wins + ' times   \U0001f40d: ' + loss + ' times   \U0001f463: ' + pct + '   \U0001f53a' + gb + ' games   \U0001f3c0: ' + ppg + ' points   \U0000274c:' + oppg + ' points   ' + '\n\n'
        id_e = id_e + 1
        
     send_text_message(reply_token, result_east)

def show_todays_mvp(reply_token):
    urlhead = 'https://www.basketball-reference.com'
    url = 'https://www.basketball-reference.com/boxscores/'
    source = requests.get(url, headers={'user-agent': user_agent.random}).text
    soup = BeautifulSoup(source, 'html.parser')
    standings = soup.find_all('table', class_="stats")


    links_points = []
    points = []


    for player in standings:
        link = player.find('a')
        point = player.find('td', class_='right')
   
        if("tied" not in link.text):
           links_points.append(urlhead + link['href'])
           points.append(point.text)
        else:
           links_points.append(None)
           points.append(None)

    message = ""

    for i in range(len(links_points)):
        if(links_points[i] != None):
           source = requests.get(links_points[i], headers={'user-agent': user_agent.random}).text
           soup = BeautifulSoup(source, 'html.parser')
           player_name = soup.find('h1').text.strip()
           teams = soup.find('a', class_='poptip default')['data-tip'].split(',')
           team = teams[0]
           message += '\U0001f3c0 '+ team + ':\n     '+ player_name + '  ' + points[i] + ' points\n\n'

    send_text_message(reply_token,message)


def show_player_menu(reply_token):
    message = 'Which player do you want to search ?\U0001f525\U0001f525'
    send_text_message(reply_token,message)

def show_team_menu(reply_token):
    message = 'Which team do you want to show ?\U0001f525\U0001f525'
    send_text_message(reply_token,message)


def specified_players(name,image):
    if(name.lower() == 'lebron james' ):
       image = 'https://cdn.britannica.com/19/233519-050-F0604A51/LeBron-James-Los-Angeles-Lakers-Staples-Center-2019.jpg?w=400&h=300&c=crop'
    elif(name.lower() == 'kevin durant'):
       image = 'https://upload.wikimedia.org/wikipedia/commons/7/75/Kevin_Durant_2022.jpg'
    elif(name.lower() == 'stephen curry'):
       image = 'https://image-cdn.essentiallysports.com/wp-content/uploads/ratio3x2_1800-1-1110x1065.jpg'
    elif(name.lower() == 'giannis antetokounmpo'):
       image = 'https://cdn.nba.com/manage/2022/11/giannis-antetokounmpo-reacts.jpg'
    elif(name.lower() == 'chris paul'):
       image = 'https://www.si.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTg5MjkxMDQ5NjkxMTI5MTg2/chris-paul-suns-nba-playoffs-lead.jpg'
    elif(name.lower() == 'jayson tatum'):
       image = 'https://www.masslive.com/resizer/18uj8cPZ-L-in79LkSoL2T91mjY=/1280x0/smart/cloudfront-us-east-1.images.arcpublishing.com/advancelocal/CZGPJGN4CRH2DJV7EM7DZXIN3M.jpg'
    elif(name.lower() == 'devin booker'):
       image = 'https://cdn.vox-cdn.com/thumbor/c3TzY4ms529PQLWxC-D_2tz2gOg=/811x0:2601x1183/1200x800/filters:focal(1410x45:1986x621)/cdn.vox-cdn.com/uploads/chorus_image/image/71549625/1244228168.0.jpg'
    elif(name.lower() == 'lamelo ball'):
       image = 'https://swarmandsting.com/wp-content/uploads/getty-images/2017/07/1390195372.jpeg'
    elif(name.lower() == 'trae young'):
       image = 'https://www.si.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cg_xy_center%2Cq_auto:good%2Cw_1200%2Cx_3117%2Cy_770/MTg4MDE1MjM1MjkzNTIxNzA2/usatsi_17877160.jpg'
    elif(name.lower() == 'joel embiid'):
       image = 'https://www.si.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTkzMzUxOTU3Mzc1NjI1MTIz/joel-embiid-76ers-slow-start.jpg'
    elif(name.lower() == 'anthony davis'):
       image = 'https://www.si.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTkyNzk4NzU1Mzg3MzUyNzg0/anthony-davis-lakers-10-3-22.jpg'
    elif(name.lower() == 'james harden'):
       image = 'https://i.guim.co.uk/img/media/395a1d4bc5870b755b7d60e2471c710ad0c952aa/0_183_4315_2589/master/4315.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=df2d8645bf4b6a6c61130c916fdb34cf'
    elif(name.lower() == 'zach lavine'):
       image = 'https://imageio.forbes.com/specials-images/imageserve//62a94c2e23cb09057249c82b/0x0.jpg?format=jpg&width=1200'
    elif(name.lower() == 'ja morant'):
       image = 'https://static01.nyt.com/images/2021/05/19/sports/19nba-ja-morant/19nba-ja-morant-mediumSquareAt3X.jpg'
    elif(name.lower() == 'zion williamson'):
       image = 'https://static01.nyt.com/images/2022/10/15/sports/14nba-zion-pelicans-print/14nba-zion-pelicans-1-mediumSquareAt3X.jpg'
    elif(name.lower() == 'luka dončić'):
       image = 'https://www.yardbarker.com/media/7/8/7898202ae181c6e0ed7650272c122fbf9b160c58/thumb_16x9/luka-doncic-joins-exclusive-club-continued.jpg?v=1'

    name = name.split()[1]
    if(name.lower() == 'antetokounmpo'):
        name = 'The Greek'

    return name,image



def show_players(reply_token,text):
    urlhead = 'https://www.basketball-reference.com'
    url = 'https://www.basketball-reference.com/leagues/NBA_2023_totals.html'
    source = requests.get(url, headers={'user-agent': user_agent.random}).text
    soup = BeautifulSoup(source, 'html.parser')
    standings = soup.find_all('tr', class_="full_table")

    name = ''
    link = ''
    find = 0

    for player in standings:
        name = player.find('a').text
        link = player.find('a')['href']
        if(name.lower() == text.lower()):
            find = 1
            break

    link = urlhead+link

   
    source = requests.get(link, headers={'user-agent': user_agent.random}).text
    soup = BeautifulSoup(source, 'html.parser')
    image = soup.find('img',{'itemscope':'image'})['src']

    name,image = specified_players(name,image)

    if(find == 1):
       send_image_carousel(reply_token,image,name,link)
    else:
       send_text_message(reply_token,"Can't find your player.\U0001f976\nHmm... \U0001f914\nPerhaps:\n(1) try again (2) menu (3) find another player")

def show_teams(reply_token,text):
    urlhead = 'https://www.basketball-reference.com'
    url = 'https://www.basketball-reference.com/leagues/NBA_2023_standings.html'
    user_agent = UserAgent()
    source = requests.get(url, headers={'user-agent': user_agent.random}).text
    soup = BeautifulSoup(source, 'html.parser')
    teams = soup.find_all('th',{'scope':'row'})

    t = ''
    link = ''
    find = 0

    for team in teams:
        t = team.find('a').text
        link = urlhead+team.find('a')['href']
        if(text.lower() == t.lower()):
            find = 1
            break
  
    
     # print(t,link)

    source = requests.get(link, headers={'user-agent': user_agent.random}).text
    soup = BeautifulSoup(source, 'html.parser')
    image = soup.find('img',class_ = 'teamlogo')['src']
    
    names = t.split(' ')
    t = names[len(names)-1]

    if(find == 1):
       send_image_carousel(reply_token,image,t,link)
    else:
        send_text_message(reply_token,"Can't find any teams.\U0001f976\nHmm... \U0001f914\nPerhaps:\n(1) try again (2) menu (3) find another team")



def show_leader_points(reply_token,leader_type,type_end):
    urlhead = 'https://www.basketball-reference.com'
    url = 'https://www.basketball-reference.com/leagues/NBA_2023_leaders.html'
    source = requests.get(url, headers={'user-agent': user_agent.random}).text
    soup = BeautifulSoup(source, 'html.parser')
    players = soup.find('div',{'id':leader_type})
    ranks = players.find_all('tr')

    count = 0
    leaders = []
    points = []
    player_links = []
    images = []

    for player in ranks:
        point = player.find('td',class_ = 'value').text.strip()
        player_name = player.find('a').text
        link = player.find('a')['href']
        leaders.append(player_name)
        points.append(point + " " + type_end)
        player_links.append(urlhead + link)
        count = count + 1
        if(count == 3):
           break

    i = 0
    for link in player_links:
        source = requests.get(link, headers={'user-agent': user_agent.random}).text
        soup = BeautifulSoup(source, 'html.parser')
        image = soup.find('img',{'itemscope':'image'})['src']
        leaders[i],image = specified_players(leaders[i],image)
        images.append(image)
        i = i+1
        
    send_rank_carousel(reply_token,images,leaders,points)

def start_draft_mocking(reply_token):
    url = 'https://www.nbadraft.net/nba-mock-drafts/'
    source = requests.get(url, headers={'user-agent': user_agent.random}).text
    soup = BeautifulSoup(source, 'html.parser')
    players = soup.find_all('td',class_ = 'player')
    first_round = players[:3]

    names = []
    imgs = []
    overalls = []


    for player in first_round:
        name_l = player.find('a').text.split()
        name = name_l[len(name_l)-1]
        names.append(name)
        url = player.find('a')['href']
        source = requests.get(url, headers={'user-agent': user_agent.random}).text
        soup = BeautifulSoup(source, 'html.parser')
        overall_s = soup.find('div',class_ = 'overall')
        overall = overall_s.find('span',class_ = 'value')
        imgurl = soup.find('div',class_ = 'player-image')
        imgs.append(imgurl.find('img')['data-lazy-src'])
        if(overall == None):
           overalls.append("90")
        else:
           overalls.append(overall.text)

    


    url = 'https://loodibee.com/nba/'
    source = requests.get(url, headers={'user-agent': user_agent.random}).text
    soup = BeautifulSoup(source, 'html.parser')
    teams = soup.find_all('figure')
    teams = teams[:30]


    lotto = random.sample(teams,k=3)
    team_imgs = []
    for team in lotto:
        team_imgs.append(team.find('img')['src'])
    send_draft_carousel(reply_token,names,imgs,overalls,team_imgs)