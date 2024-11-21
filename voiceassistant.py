import time
import speech_recognition as sr
import pyaudio
import pyttsx3
import os
import webbrowser
from customtkinter import *
import cv2
import mediapipe as mp
import pyautogui

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_for_audio():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        audio = listener.listen(source)
    
    try:
        return listener.recognize_google(audio).lower()
    except sr.UnknownValueError:
        print("I didn't catch that.")
        return None
    except sr.RequestError:
        print('API is unavailable')
        return None
    
def web_searching():
    while True:
        print('Here, you can browse any topic of your choice!')
        speak('Here, you can browse any topic of your choice!')
        time.sleep(0.5)
        print('What would you like to browse?')
        speak('What would you like to browse?')
        query = listen_for_audio()
        if query is None:
            print("sorry I didn't catch that.")
            continue
        query = query.strip()
        if 'stop' in query.lower():
            print('Exiting Search...')
            speak('Exiting Search')
            break
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(search_url)
        print(f"Searching for: {query}")

def opening_applications():
    Apps = {
    'google':r"C:\Users\Harris\OneDrive\Desktop\Softwares\Google Chrome.lnk",
    'vs': r"C:\Users\Harris\OneDrive\Desktop\Softwares\Visual Studio Code.lnk",
    'file':r"C:\Users\Harris\OneDrive\Desktop\Softwares\This PC - Shortcut.lnk",
    'code': r"C:\Users\Harris\OneDrive\Desktop\Code"
    }
    Tabs = {
    'netflix': "https://www.netflix.com/browse",
    'video': "https://www.youtube.com/",
    'mail' : "https://mail.google.com/mail/u/0/#inbox",
    'google meet' : "https://meet.google.com/landing"
    }

    while True:
        print('Here, you can open Media like Netflix Applications and more!')
        speak('Here, you can open Media like Netflix Applications and more!')
        time.sleep(0.5)
        print('What would you like to open?')
        speak('What would you like to open?')
        choice = listen_for_audio()
        
        if choice:
            choice = choice.lower()
            if choice in ['stop','quit']:
                print('Exiting Task Opener...')
                speak('Exiting Task Opener')
                break
            elif choice in Apps:
                os.startfile(Apps[choice])
            elif choice in Tabs:
                webbrowser.open(Tabs[choice])
                time.sleep(3)
                if choice == 'netflix' or choice == 'video':
                    mp_hand = mp.solutions.hands
                    hands = mp_hand.Hands()

                    def pause_gesture(hand_landmarks):
                    
                        index_tip = hand_landmarks.landmark[mp_hand.HandLandmark.INDEX_FINGER_TIP]
                        index_dip = hand_landmarks.landmark[mp_hand.HandLandmark.INDEX_FINGER_DIP]

                        thumb_tip = hand_landmarks.landmark[mp_hand.HandLandmark.THUMB_TIP]

                        middle_tip = hand_landmarks.landmark[mp_hand.HandLandmark.MIDDLE_FINGER_TIP]
                        middle_dip = hand_landmarks.landmark[mp_hand.HandLandmark.MIDDLE_FINGER_DIP]

                        ring_tip = hand_landmarks.landmark[mp_hand.HandLandmark.RING_FINGER_TIP]
                        ring_dip = hand_landmarks.landmark[mp_hand.HandLandmark.RING_FINGER_DIP]

                        pinky_tip = hand_landmarks.landmark[mp_hand.HandLandmark.PINKY_TIP]
                        pinky_dip = hand_landmarks.landmark[mp_hand.HandLandmark.PINKY_DIP]

                        index_down = index_dip.y < index_tip.y
                        thumb_down = thumb_tip.y < index_tip.y
                        middle_down = middle_dip.y < middle_tip.y
                        ring_down = ring_dip.y < ring_tip.y
                        pinky_down = pinky_dip.y < pinky_tip.y

                        return index_down and thumb_down and middle_down and ring_down and pinky_down

                    def vol_down(hand_landmarks):
                    
                        index_tip = hand_landmarks.landmark[mp_hand.HandLandmark.INDEX_FINGER_TIP]
                        index_dip = hand_landmarks.landmark[mp_hand.HandLandmark.INDEX_FINGER_DIP]

                        thumb_tip = hand_landmarks.landmark[mp_hand.HandLandmark.THUMB_TIP]

                        middle_tip = hand_landmarks.landmark[mp_hand.HandLandmark.MIDDLE_FINGER_TIP]

                        ring_tip = hand_landmarks.landmark[mp_hand.HandLandmark.RING_FINGER_TIP]

                        pinky_tip = hand_landmarks.landmark[mp_hand.HandLandmark.PINKY_TIP]


                        index_extend = index_tip.y < index_dip.y
                        thumb_extend = thumb_tip.y < index_dip.y
                        ring_down =  ring_tip.y > index_dip.y
                        middle_down = middle_tip.y > index_dip.y
                        pinky_down = pinky_tip.y > index_dip.y

                        return index_extend and thumb_extend and ring_down and middle_down and pinky_down

                    def vol_up(hand_landmarks):

                        index_tip = hand_landmarks.landmark[mp_hand.HandLandmark.INDEX_FINGER_TIP]
                        index_dip = hand_landmarks.landmark[mp_hand.HandLandmark.INDEX_FINGER_DIP]

                        thumb_tip = hand_landmarks.landmark[mp_hand.HandLandmark.THUMB_TIP]

                        middle_tip = hand_landmarks.landmark[mp_hand.HandLandmark.MIDDLE_FINGER_TIP]

                        ring_tip = hand_landmarks.landmark[mp_hand.HandLandmark.RING_FINGER_TIP]

                        pinky_tip = hand_landmarks.landmark[mp_hand.HandLandmark.PINKY_TIP]

                        index_extend = index_tip.y < index_dip.y
                        middle_extend = middle_tip.y < index_dip.y
                        ring_down = ring_tip.y > index_dip.y
                        pinky_down = pinky_tip.y > index_dip.y

                        return index_extend and middle_extend and ring_down and pinky_down

                    def forward(hand_landmarks):
                        index_tip = hand_landmarks.landmark[mp_hand.HandLandmark.INDEX_FINGER_TIP]
                        index_dip = hand_landmarks.landmark[mp_hand.HandLandmark.INDEX_FINGER_DIP]

                        middle_tip = hand_landmarks.landmark[mp_hand.HandLandmark.MIDDLE_FINGER_TIP]
                        middle_dip = hand_landmarks.landmark[mp_hand.HandLandmark.MIDDLE_FINGER_DIP]

                        ring_tip = hand_landmarks.landmark[mp_hand.HandLandmark.RING_FINGER_TIP]
                        ring_dip = hand_landmarks.landmark[mp_hand.HandLandmark.RING_FINGER_DIP]

                        pinky_tip = hand_landmarks.landmark[mp_hand.HandLandmark.PINKY_TIP]
                        pinky_dip = hand_landmarks.landmark[mp_hand.HandLandmark.PINKY_DIP]

                        thumb_tip = hand_landmarks.landmark[mp_hand.HandLandmark.THUMB_TIP]

                        index_down = index_tip.y > index_dip.y
                        middle_down = middle_tip.y > middle_dip.y
                        ring_down = ring_tip.y > ring_dip.y
                        pinky_extend = pinky_tip.y < pinky_dip.y 
                        thumb_extend = thumb_tip.y < index_dip.y   

                        return index_down and middle_down and ring_down and pinky_extend and thumb_extend

                    def backwards(hand_landmarks):

                        index_tip = hand_landmarks.landmark[mp_hand.HandLandmark.INDEX_FINGER_TIP]
                        index_dip = hand_landmarks.landmark[mp_hand.HandLandmark.INDEX_FINGER_DIP]

                        middle_tip = hand_landmarks.landmark[mp_hand.HandLandmark.MIDDLE_FINGER_TIP]
                        middle_dip = hand_landmarks.landmark[mp_hand.HandLandmark.MIDDLE_FINGER_DIP]

                        ring_tip = hand_landmarks.landmark[mp_hand.HandLandmark.RING_FINGER_TIP]
                        ring_dip = hand_landmarks.landmark[mp_hand.HandLandmark.RING_FINGER_DIP]

                        pinky_tip = hand_landmarks.landmark[mp_hand.HandLandmark.PINKY_TIP]
                        pinky_dip = hand_landmarks.landmark[mp_hand.HandLandmark.PINKY_DIP]

                        thumb_tip = hand_landmarks.landmark[mp_hand.HandLandmark.THUMB_TIP]

                        index_extend = index_tip.y < index_dip.y 
                        middle_extend = middle_tip.y < middle_dip.y
                        ring_extend = ring_tip.y < ring_dip.y
                        pinky_extend = pinky_tip.y < pinky_dip.y
                        thumb_down = thumb_tip.y > index_dip.y 

                        return index_extend and middle_extend and ring_extend and pinky_extend and thumb_down
                    mp_draw = mp.solutions.drawing_utils
                    cap = cv2.VideoCapture(0)

                    while True:
                        Success, img = cap.read()
                        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        result = hands.process(img_rgb)

                        if result.multi_hand_landmarks:
                            for hand_landmarks in result.multi_hand_landmarks:
                                if pause_gesture(hand_landmarks):
                                    pyautogui.press('space')
                                    time.sleep(0.6)
                                elif vol_down(hand_landmarks):
                                    pyautogui.press('down')
                                    time.sleep(0.2)
                                elif vol_up(hand_landmarks):
                                    pyautogui.press('up')
                                    time.sleep(0.2)
                                elif forward(hand_landmarks):
                                    pyautogui.press('right')
                                    time.sleep(0.1)
                                elif backwards(hand_landmarks):
                                    pyautogui.press('left')
                                    time.sleep(0.1)
                                mp_draw.draw_landmarks(img, hand_landmarks, mp_hand.HAND_CONNECTIONS)

                        cv2.imshow('Hand Tracker', img)
                        if cv2.waitKey(5) & 0XFF == 27:
                            break
                        
                    cap.release()
                    cv2.destroyAllWindows()
        elif choice == 'google meet':
                    pyautogui.click(800,400,duration=0.5)
                    pyautogui.click(800,435,duration=0.5)
        else:
            print('Sorry I could not find that')
            speak('Sorry I could not find that')
        
def time_telling():
    app = CTk()
    app.geometry('600x300')

    set_appearance_mode('light')

    def update_time():
        current_time = time.strftime('%I:%M')
        time_label.configure(text=current_time)
        app.after(1000,update_time)

    time_label = CTkLabel(
        app,
        text="",
        font=('Arial',120),
        text_color='#63C5DA',
        fg_color='transparent',
    ) 
    time_label.pack(pady=100)

    update_time()
    
    app.mainloop()  

def help():
    print('''     
This is a list of tasks I am able to perform:
          
1. Web searching; keyword: "search"
2. Telling the Time; keyword: "time"
3. Executing files; keyword: "Media"
4. Play Music; keyword: "music"
5. Take a Screenshot; keyword: "screenshot"
6. Ask for help; keyphrase: "what can you do?"
''')
    speak('''     
This is a list of tasks I am able to perform:
          
1. Web searching; keyword: "search"
2. Telling the Time; keyword: "time"
3. Executing files; keyword: "Media"
4. Play Music; keyword: "music"
5. Take a Screenshot; keyword: "screenshot"
6. Ask for help; keyphrase: "what can you do?"
''')
    
def music():
    print('Opening Spoitify..')
    speak('Opening Spotify')
    music = "https://open.spotify.com/playlist/71Sh4WqH5OMOeRYE4M0mky"
    webbrowser.open(music)

def screenshot():
    speak('Taking a screenshot')
    pyautogui.hotkey('win','Shift','s')
    pyautogui.click(980,30, duration=1)
    pyautogui.click(980,100, duration=1)

def calculate():
    print('Opening Calculator..')
    speak('Opening Calculator')
    os.system('calc')

def main_assistant():
    print('Hello! I am Mark, your voice assistant, how can I help you?')
    speak('Hello! I am Mark, your voice assistant, how can I help you?')
    while True:
        task = listen_for_audio()
        
        if task:
            if 'search' in task:
                speak('Initiating Search Sequence')
                web_searching()
            elif 'media' in task:
                speak('Initiating Media Sequence')
                opening_applications()
            elif 'time' in task:
                time_telling()
            elif 'screenshot' in task:
                screenshot()
            elif "do" in task:
                help()
            elif 'music' in task:
                music()
            elif 'calculator' in  task:
                calculate()
            elif 'exit' or 'thank you' in task:
                print("You're welcome! Let me know if you need anything else.")
                speak("You're welcome! Let me know if you need anything else.!")
                break
        else:
            print("I didn't understand that command.")
main_assistant()