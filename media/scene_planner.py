from core.logger import get_logger

logger = get_logger()

class ScenePlanner:

    def generate(self, topic, script):

        scenes = [

        {
        "scene":1,
        "time":"0-4",
        "character":"stick figure person standing near ATM machine",
        "background":"static simple bank ATM kiosk interior white wall ATM machine mounted on wall",
        "image_prompt":"minimal 2D stick figure animation frame plain white background simple grey ATM machine on wall small screen keypad cash slot stick figure standing slightly bent forward looking at ATM screen black stick lines round head no facial details clean flat animation style no shadows static background",
        "animation_prompt":"stick figure slowly walks toward ATM machine raises right hand toward keypad head tilts slightly forward",
        "movement":"0-1s stick figure step forward 1-2s hand lift toward keypad 2-3s head tilt 3-4s pause looking at ATM"
        },

        {
        "scene":2,
        "time":"4-8",
        "character":"stick figure using ATM",
        "background":"same static ATM kiosk background",
        "image_prompt":"2D stick figure pressing ATM keypad simple ATM machine mounted wall screen rectangle keypad grid minimal stick animation white background clean flat style",
        "animation_prompt":"stick figure presses keypad three times slight body lean forward",
        "movement":"4-5s finger press 5-6s keypad press again 6-7s small body lean 7-8s pause"
        },

        {
        "scene":3,
        "time":"8-12",
        "character":"stick figure receiving phone call",
        "background":"static plain room background simple table and phone",
        "image_prompt":"stick figure holding smartphone near head indicating phone call minimal animation white background simple table and chair stick style drawing clean lines",
        "animation_prompt":"phone vibration icon appears near phone stick figure lifts phone to ear head tilt listening",
        "movement":"8-9s phone vibration 9-10s hand lift phone 10-11s head tilt 11-12s listening pause"
        },

        {
        "scene":4,
        "time":"12-16",
        "character":"stick figure looking at OTP message",
        "background":"same static room background",
        "image_prompt":"stick figure looking at smartphone screen showing message box labeled OTP code minimal UI rectangle message bubble simple stick drawing white background",
        "animation_prompt":"message bubble pops above phone stick figure raises eyebrows slightly leaning toward screen",
        "movement":"12-13s message popup 13-14s lean forward 14-16s pause reading"
        },

        {
        "scene":5,
        "time":"16-20",
        "character":"stick figure sharing OTP unknowingly",
        "background":"static background with phone",
        "image_prompt":"stick figure speaking into phone while looking at OTP message bubble simple stick animation white background phone icon and message bubble",
        "animation_prompt":"speech bubble appears stick figure hand gesture talking on phone",
        "movement":"16-17s speech bubble appear 17-18s hand gesture 18-20s head nod"
        },

        {
        "scene":6,
        "time":"20-24",
        "character":"stick figure receiving bank alert",
        "background":"same room background",
        "image_prompt":"stick figure holding phone surprised alert icon above smartphone bank notification message bubble minimal stick animation white background",
        "animation_prompt":"alert icon flashes stick figure jumps slightly backward",
        "movement":"20-21s alert flash 21-22s body jerk 22-24s frozen surprise"
        },

        {
        "scene":7,
        "time":"24-28",
        "character":"money leaving bank account visual",
        "background":"simple bank icon and arrow graphic",
        "image_prompt":"simple infographic style stick animation bank building icon money coin icons moving through arrow to unknown account minimal vector style white background",
        "animation_prompt":"coins slide along arrow toward second account icon",
        "movement":"24-26s coins move across arrow 26-28s disappear into second account"
        },

        {
        "scene":8,
        "time":"28-32",
        "character":"stick figure shocked",
        "background":"static room background",
        "image_prompt":"stick figure holding empty wallet icon above head shocked pose arms raised minimal stick animation white background clean flat design",
        "animation_prompt":"wallet icon flips open showing empty stick figure raises both hands",
        "movement":"28-29s wallet appear 29-31s arms raise 31-32s freeze"
        },

        {
        "scene":9,
        "time":"32-36",
        "character":"stick figure warning sign",
        "background":"clean white background warning icon",
        "image_prompt":"stick figure pointing at warning sign with text do not share OTP minimal stick animation educational infographic style white background",
        "animation_prompt":"warning triangle icon pulse stick figure points toward sign",
        "movement":"32-33s sign appear 33-35s icon pulse 35-36s pointing pose"
        }

        ]

        logger.info("9 stick animation scenes generated")

        return scenes
