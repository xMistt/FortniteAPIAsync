import datetime


class Playlist:
    """Represents a Fortnite playlist.

    Attributes
    ----------
    id: :class:`str`
        The ID of the playlist.
    name: :class:`str`
        The name of the playlist.
    game_type: :class:`str`
        The game type of the playlist.
    min_players: :class:`int`
        The minimum number of players.
    max_players: :class:`int`
        The maximum number of players.
    max_teams: :class:`int`
        The maximum number of teams.
    max_team_size: :class:`int`
        The maximum team size.
    max_squads: :class:`int`
        The maximum number of squads.
    max_squad_size: :class:`int`
        The maximum squad size.
    is_default: :class:`bool`
        Whether the playlist is a default playlist.
    is_tournament: :class:`bool`
        Whether the playlist is a tournament playlist.
    is_ltm: :class:`bool`
        Whether the playlist is a limited time mode.
    is_large_team_game: :class:`bool`
        Whether the playlist is a large team game mode.
    accumulate_to_profile_stats: :class:`bool`
        Whether matches count towards profile statistics (this value is not
        actually used for anything and isn't an indicator of whether or not
        the playlist accumulates to profile stats on websites such as
        FortniteTracker).
    gameplay_tags: :class:`list`[:class:`str`]
        List of gameplay tags associated with the playlist.
    path: :class:`str`
        File path of playlist.
    added: :class:`datetime.datetime`
        Datetime object which represents when the playlist was added to the API.
    """

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