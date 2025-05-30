from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl

def open_browser_window():
    # Open the Pokémon Showdown Team Builder in the default web browser
    url = "https://pokepast.es/"
    QDesktopServices.openUrl(QUrl(url))

# Define the function to open the Pokémon Showdown Team Builder
def open_team_builder():
    # Specify the URL of the Pokémon Showdown Team Builder
    team_builder_url = "https://play.pokemonshowdown.com/teambuilder"

    # Open the Team Builder in the default web browser
    QDesktopServices.openUrl(QUrl(team_builder_url))

def rate_addon_url():
    # Specify the URL of the Pokémon Showdown Team Builder
    rating_url = "https://ankiweb.net/shared/review/1908235722"

    # Open the Team Builder in the default web browser
    QDesktopServices.openUrl(QUrl(rating_url))

def report_bug():
    # Specify the URL of the Pokémon Showdown Team Builder
    bug_url = "https://github.com/Unlucky-Life/ankimon/issues"

    # Open the Team Builder in the default web browser
    QDesktopServices.openUrl(QUrl(bug_url))

def join_discord_url():
    # Specify the URL of the Pokémon Showdown Team Builder
    discord_url = "https://discord.gg/hcq53X5mcu"

    # Open the Team Builder in the default web browser
    QDesktopServices.openUrl(QUrl(discord_url))

def open_leaderboard_url():
    # Specify the URL of the Pokémon Showdown Team Builder
    leaderboard_url = "https://leaderboard.ankimon.com/"

    # Open the Team Builder in the default web browser
    QDesktopServices.openUrl(QUrl(leaderboard_url))