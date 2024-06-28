# Automatic loading of a mode
config.set("input.mode_override", "passthrough", "monkeytype.com")
config.set("input.mode_override", "passthrough", "play.typeracer.com")

# Open every tab as a new window, Vimb style
# c.tabs.tabs_are_windows = True
# c.tabs.last_close = "close"

c.auto_save.session = False
c.scrolling.smooth = True
c.session.lazy_restore = True
c.content.autoplay = False

c.downloads.location.directory = '~/Downloads'

c.tabs.show = "never"
c.statusbar.show = "never"

c.url.default_page = 'https://start.duckduckgo.com/'
c.url.start_pages = 'https://start.duckduckgo.com/'

c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}', 'am': 'https://www.amazon.com/s?k={}', 'aw': 'https://wiki.archlinux.org/?search={}', 'goog': 'https://www.google.com/search?q={}', 'hoog': 'https://hoogle.haskell.org/?hoogle={}', 're': 'https://www.reddit.com/r/{}', 'ub': 'https://www.urbandictionary.com/define.php?term={}', 'wiki': 'https://en.wikipedia.org/wiki/{}', 'yt': 'https://www.youtube.com/results?search_query={}', 'aur': 'https://aur.archlinux.org/packages/?O=0&K={}', 'od': 'https://odysee.com/$/search?q={}'}

c.input.insert_mode.auto_load = True

c.editor.command = ["emacsclient", "+{line}:{column}", "{file}"]

c.fonts.completion.category = 'bold 12pt Fira Code'
c.fonts.completion.entry = '12pt Fira Code'
c.fonts.debug_console = '12pt Fira Code'
c.fonts.downloads = '12pt Fira Code'
c.fonts.hints = 'bold 12pt Fira Code'
c.fonts.keyhint = '12pt Fira Code'
c.fonts.messages.error = '12pt Fira Code'
c.fonts.messages.info = '12pt Fira Code'
c.fonts.messages.warning = '12pt Fira Code'
c.fonts.prompts = '12pt Fira Code'
c.fonts.statusbar = '12pt Fira Code'

# Vim-style movement keys in command mode
config.bind('<Ctrl-j>', 'completion-item-focus --history next', mode='command')
config.bind('<Ctrl-k>', 'completion-item-focus --history prev', mode='command')

# More binding hints here: https://gitlab.com/Kaligule/qutebrowser-emacs-config/blob/master/config.py

config.bind('X', 'wq')
config.unbind('d') # Dont want to accidentally delete my tab
config.bind('Q', 'bookmark-add')
config.bind('W', 'bookmark-del')
config.bind('E', 'bookmark-list')
config.bind('b', 'cmd-set-text -s :tab-select ', mode='normal')
config.bind('Z', 'spawn mpv {url}')
config.bind('z', 'hint links spawn mpv {hint-url}')
config.bind('t', 'cmd-set-text -s :open -t')
config.bind('xb', 'config-cycle statusbar.show always never')
config.bind('xt', 'config-cycle tabs.show always never')
config.bind('xx', 'config-cycle statusbar.show always never;; config-cycle tabs.show always never')

config.load_autoconfig()
