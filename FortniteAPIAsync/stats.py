import datetime


class GamemodeStats:
    """Represents statistics for a specific game mode.

    Attributes
    ----------
    raw: :class:`dict`
        Raw data from FortniteAPI (can be used to reconstruct object)
    score: :class:`int`
        The total score.
    score_per_min: :class:`float`
        The score earned per minute.
    score_per_match: :class:`float`
        The score earned per match.
    wins: :class:`int`
        The number of wins.
    top_3: :class:`int`
        The number of top 3 finishes.
    top_5: :class:`int`
        The number of top 5 finishes.
    top_6: :class:`int`
        The number of top 6 finishes.
    top_10: :class:`int`
        The number of top 10 finishes.
    top_12: :class:`int`
        The number of top 12 finishes.
    top_25: :class:`int`
        The number of top 25 finishes.
    kills: :class:`int`
        The total number of kills.
    kills_per_min: :class:`float`
        The number of kills per minute.
    kills_per_match: :class:`float`
        The number of kills per match.
    deaths: :class:`int`
        The total number of deaths.
    kd: :class:`float`
        The kill/death ratio.
    matches: :class:`int`
        The total number of matches played.
    win_rate: :class:`float`
        The win rate percentage.
    minutes_played: :class:`int`
        The total number of minutes played.
    players_outlived: :class:`int`
        The total number of players outlived.
    last_modified: :class:`datetime.datetime`
        Datetime when the stats were last modified.
    """

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
    """Represents player statistics.

    Attributes
    ----------
    raw: :class:`dict`
        Raw data from FortniteAPI (can be used to reconstruct object)
    id: :class:`str`
        The account ID of the player.
    display_name: :class:`str`
        The display name of the player.
    level: :class:`int`
        The current Battle Pass level.
    level_progress: :class:`int`
        The Battle Pass level progress.
    image: :class:`str`
        URL of the rendered stats image.
    inputs: :class:`dict`
        Dictionary mapping input types to input-specific stats.
    """

    def __init__(self, data: dict) -> None:
        self.raw = data

        self.id = data.get('account').get('id')
        self.display_name = data.get('account').get('name')

        self.level = data.get('battlePass').get('level')
        self.level_progress = data.get('battlePass').get('progress')

        self.level = data.get('image')

        self.inputs = {}
        for input_type, gamemodes in data.get('stats').items():
            self.inputs[input_type] = {
                mode: GamemodeStats(stats)
                for mode, stats in gamemodes.items()
            }