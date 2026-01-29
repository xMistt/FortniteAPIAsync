import datetime


class GamemodeStats:
    def __init__(self, data: dict) -> None:
        self.raw = data

        self.score = data.get('score')
        self.score_per_min = data.get('scorePerMin')
        self.score_per_match = data.get('scorePerMatch')
        self.wins = data.get('wins')

        self.top_3 = data.get('top3')
        self.top_5 = data.get('top5')
        self.top_6 = data.get('top6')
        self.top_10 = data.get('top10')
        self.top_12 = data.get('top12')
        self.top_25 = data.get('top25')

        self.kills = data.get('kills')
        self.kills_per_min = data.get('killsPerMin')
        self.kills_per_match = data.get('killsPerMatch')

        self.deaths = data.get('deaths')
        self.kd = data.get('kd')
        self.matches = data.get('matches')
        self.win_rate = data.get('winRate')
        self.minutes_played = data.get('minutesPlayed')
        self.players_outlived = data.get('playersOutlived')
        self.last_modified = datetime.datetime.fromisoformat(
            data.get('lastModified').replace('Z', '+00:00')
        )


class Stats:
    def __init__(self, data: dict) -> None:
        self.raw = data

        self.id = data.get('account').get('id')
        self.display_name = data.get('account').get('name')

        self.level = data.get('battlePass').get('level')
        self.level_progress = data.get('battlePass').get('progress')

        self.inputs = {}
        for input_type, gamemodes in data.get('stats').items():
            self.inputs[input_type] = {
                mode: GamemodeStats(stats)
                for mode, stats in gamemodes.items()
            }