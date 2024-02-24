from sportradar import NHL
import ast

VGK_ID = "42376e1c-6da8-461e-9443-cfcf0a9fcc4d"
sr = NHL.NHL("API_KEY")

def get_team_content(team_id)->dict:
    byte_response = sr.get_team_profile___roster(team_id).content
    byte_to_str = byte_response.decode("UTF-8")
    team_json = ast.literal_eval(byte_to_str)
    return team_json

def get_team_injuries(team)->dict:
    byte_response = sr.get_injuries().content
    byte_to_str = byte_response.decode("UTF-8")
    injuries_json = ast.literal_eval(byte_to_str)
    injuries_list = injuries_json.get("teams")
    team_injuries = []
    for injured_player in injuries_list:
        if injured_player.get("name") == team:
            print(injured_player)
            team_injuries.append(injured_player)
    return team_injuries


def main():
    VGK_team = get_team_content(VGK_ID)    
    coach = VGK_team.get("coaches")
    players = VGK_team.get("players")
    injured_players = get_team_injuries("Golden Knights")
    print(coach)
    print(players)
    print(injured_players)

if __name__ == "__main__":
    main()