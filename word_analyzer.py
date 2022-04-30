from action import Action
from yt_player import Yt_music
from api_weather import weather


def analyze(words):
    next_command = True

    action = Action()
    executor_url, session_id = action.open_session_file()
    driver = action.attach_to_session(executor_url, session_id)

    yt = Yt_music(driver)

    if "play" in words:
        # pause play music 
        try:
            yt.pause_play_music()
        except:
            print("Opening Browser ...")
            yt.music()

    elif "pause" in words:
        # pause play music
        try:
            yt.pause_play_music()
        except:
            print("Music is not playing ...")

    elif "next" in words:
        # next song
        try:
            yt.next_song()
        except:
            print("Music is not playing ...")

    elif "quit" in words:
        # close browser
        try:
            yt.close()
        except:
            print("Music is not playing ...")

    elif "weather" in words:
        # temperature of one of the selected cities
        weather("brasov")

    else:
        next_command = False

    return next_command
