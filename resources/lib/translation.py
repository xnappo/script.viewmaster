import xbmcaddon
from simple_logging import SimpleLogging

log = SimpleLogging(__name__)
addon = xbmcaddon.Addon(id='plugin.video.embycon')


def i18n(string_id):
    try:
        return addon.getLocalizedString(STRINGS[string_id]).encode('utf-8', 'ignore')
    except Exception as e:
        log.error('Failed String Lookup: %s (%s)' % (string_id, e))
        return string_id


STRINGS = {
    'tvshows': 30229,
    'default_view': 30230,
    'movies': 30231,
    'boxsets': 30232,
    'series': 30233,
    'seasons': 30234,
    'episodes': 30235,
    'save': 30236,
    'widgets': 30247,
    'unknown': 30250,
    'change_user': 30253,
    'show_settings': 30254,
    'set_default_views': 30255,
    'missing_title': 30280,
    'extra_prompt': 30276,
    'skin_not_supported': 30281,
}
