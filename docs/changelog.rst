.. currentmodule:: FortniteAPIAsync

Changelog
=========

Detailed version changes.

v2.0.0
------

Updated the library to support all Fortnite-API endpoints & to fix/update any changes made since the last release.

Added
~~~~~

- Added the following functions to :class:`APIClient`:
    - :meth:`APIClient.get_aes()`
    - :meth:`APIClient.get_creator_code()`
    - :meth:`APIClient.get_map()`
    - :meth:`APIClient.get_news()`
    - :meth:`APIClient.get_playlists()`
    - :meth:`APIClient.get_playlist_by_id()`
    - :meth:`APIClient.get_stats()`
    - :meth:`APIClient.get_stats_by_id()`
    - :meth:`APIClient.get_banners()`
    - :meth:`APIClient.get_banner_colors()`
    - :meth:`APIClient.get_shop()`
- Added the following functions to :class:`Cosmetics`:
    - :meth:`Cosmetics.get_all_cosmetics()`
    - :meth:`Cosmetics.get_all_track_cosmetics()`
    - :meth:`Cosmetics.get_all_instrument_cosmetics()`
    - :meth:`Cosmetics.get_all_car_cosmetics()`
    - :meth:`Cosmetics.get_all_lego_cosmetics()`
    - :meth:`Cosmetics.get_all_lego_kit_cosmetics()`
    - :meth:`Cosmetics.get_all_bean_cosmetics()`

Bug Fixes
~~~~~

- Fixed all previous errors with the library caused by API changes.

Changes
~~~~~~~

- (**Breaking**) Old `Cosmetics.get_all_cosmetics()` renamed to :meth:`Cosmetics.get_all_cosmetics()`.
- (**Breaking**) :meth:`Cosmetics.get_new_cosmetics()` now returns a :class:`NewCosmetics` object.
- (**Breaking**) The following attributes of :class:`BRCosmetic` have been updated from a dictionary to a data class: `type`, `rarity`, `series`, `set`, `introduction`.


