import datetime


class Playlist:
    def __init__(self, data: dict) -> None:
        self.id = data.get('id')
        self.name = data.get('name')
        self.game_type = data.get('gameType')

        self.min_players = data.get('minPlayers')
        self.max_players = data.get('maxPlayers')
        self.max_teams = data.get('maxTeams')
        self.max_team_size = data.get('maxTeamSize')
        self.max_squads = data.get('maxSquads')
        self.max_squad_size = data.get('maxSquadSize')

        self.is_default = data.get('isDefault')
        self.is_tournament = data.get('isTournament')
        self.is_ltm = data.get('isLimitedTimeMode')
        self.is_large_team_game = data.get('isLargeTeamGame')
        self.accumulate_to_profile_stats = data.get('accumulateToProfileStats')
        self.gameplay_tags = data.get('gameplayTags')
        self.path = data.get('path')

        self.added = datetime.datetime.fromisoformat(
            data.get('added').replace('Z', '+00:00')
        )