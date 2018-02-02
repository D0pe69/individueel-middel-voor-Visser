#bewegen plaatjes
$ move = MoveTransition(1.0)
$ movefast = MoveTransition(0.5)
$flash = Fade(.25, 0, .75, color="#fff")
$saver = False
transform bounce:
    xalign 0.3 yalign 0.5
    linear 0.3 yalign 0.0
    linear 0.3 yalign 0.5

    xalign 0.3 yalign 0.5
    linear 0.5 yalign 0.0
    linear 0.5 yalign 0.5
    alignaround (.5,.5)
    linear 2.0 yalign 0.0 clockwise circles 5



transform wiggle:
    #Start positie animatie
    #xalign 1.0 yalign 1.0

    linear 0.2 xalign 0.99
    linear 0.2 xalign 1.0
    repeat 6



#people
define d = Character("Mr. Skills")
define m =Character("Me", color="#00FF33")
define mr= Character("Mark")
define me =Character("Me speaking", color="#FF0000")
define kok=Character("Female employee")
define uv =Character("Unknown voice")
define r =Character("Meul Ronman")
define c=Character("Camera Desk Lady")
define b =Character("Bat")
define n =Character("Neta Bosdoorn")


#background Images
image klaslokaaldick ="klaslokaal_dick.jpg"
image beginscherm ="beginscherm.png"
image volgende_dag= "volgende_dag.png"
image gang = "gang.png"
image gameover ="gameover.png"
image kantine ="kantine.png"
image soviet ="russia.png"
image america ="america.png"
image horror = "horror.png"
image counter ="counter.png"
image dddag ="5dag.png"
image avonddag ="avonddag.png"
image hanze ="titel.jpg"
image donkergang ="donkergang.png"
image exit ="exit.png"
image exit2 ="exit2.png"
image monster ="monster.png"
image listened ="luister.png"
image trap ="trap.png"
image foto ="foto.png"
image victory="victory.png"
image ronhor:
    "kantine.png"
    "horror.png" with dissolve
    pause 0.1
    "kantine.png" with dissolve
    pause 0.1
    repeat 4


image ronhor2:
    "exit2.png"
    "horror.png" with dissolve
    pause 0.1
    "horror.png" with dissolve
    pause 0.1
    repeat 40

image ronhor3:
    "klaslokaal_dick.jpg"
    "horror.png" with dissolve
    pause 0.1
    "horror.png" with dissolve
    pause 0.1
    repeat 40

image ronhor4:
    "counter.png"
    "horror.png" with dissolve
    pause 0.1
    "horror.png" with dissolve
    pause 0.1
    repeat 40

image ronhor5:
    "foto.png"
    "horror.png" with dissolve
    pause 0.1
    "horror.png" with dissolve
    pause 0.1
    repeat 40

#characters sprites
image teacher = "Teacher.png"
image mark = "Mark.png"
image kok ="kok.png"
image pizza ="pizzaman.png"
image gun ="pistol.png"
image camera ="camera.png"
image pizzamove:
    "pizzaman.png"
    0.3
    "pizzaman1.png"
    0.3
    "pizzaman2.png"
    0.3
    repeat
image neta ="neta.png"
image bat ="bat.png"
#image teacher = im.Scale("Teacher.png", 70, 100) #Enter specific numbers <--


label splashscreen:
    scene black
    with Pause (2)

    show text "Welcome to the Hanze adventure game. In this game you will experience the adventure of a student currently following the minor Communication and Campaigning. This game has been specifically created for my Skills Teacher D. Visser. So I hope you will enjoy it!" with dissolve
    with Pause (10)

    hide text with dissolve
    with Pause (2)
    return

label start:
    stop music
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "fishing.mp3"
    scene beginscherm
    m "It has been quite some time since I finished highschool..."
    m "After graduating as a straight A student I first decided to go to university. I mean why shouldn't I have gone to university?"
    m "I was an amazing student and I thought the HBO was below me considering my VWO education degree"
    m "Adult life however, hasn't been as kind to me as highschool life was."
    m "I mean, dont get me wrong, it's not like I had some huge tragedy happening to me or something like that"
    m "it was more an issue of things not coming my way like they used to...."
    m "Back in highschool I never really had to try to succeed you know. Not that I didn't do anything, but I showed up to class, did my homework, studied for exams and enjoyed the ride"
    m "So coming out of highschool I felt that I could take my next level of education by storm just by doing what I always did."
    m "But after choosing a wrong field of education, giving in to the temptation of skipping classes because nothing was compulsory I failed drastically. "
    m "You know how they always say 'a donkey does not hit the same rock twice'? Well I did hit the same rock thrice and I'm not out of the clear yet..."
    m "That's right, after three consecutive years of dropping out of college I am currently going through my fourth try."
    m "This time I'm not at a college however, but an university of applied sciences. The Hanzehogeschool."
    m "Looking back I never thought it would end up like this, but here we are. Luckily thing seem to be going my way again"
    m "Currently I am in my third year and have to follow what is called a minor. So for the foreseeable future I will be communicating and creating campaigns."
    m "I'm curious to see how the Hanze will surprise me this time around, I have a feeling this will be interesting...."
    scene volgende_dag with fade
    with Pause (2)


    scene klaslokaaldick with fade#/ hpunch  dit zorgt ervoor dat het scherm gaat trillen
    scene klaslokaaldick with vpunch #/ hpunch  dit zorgt ervoor dat het scherm gaat trillen
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show teacher

    # These display lines of dialogue.
    play sound "punch.mp3"
    d "Hey you, stop daydreaming and pay attention!"
    show teacher at left with move
    d "Now as I was saying before, in this class me and my colleague will be helping you develop products for your campaign."

    m "So this is one of my teachers Dick Visser, or as I like to call him: Mr. Skills. I haven't known him for long but he seems like a nice guy. Very passionate about his proffesion too, which is always nice."
    m "He does have a tendency to punch students though, as we just saw. I mean I dont think punching students is politically accepted anymore but it is a quite refreshing take on teaching which I can definitely appreciate"
    m "He does punch quite hard though, so I better start paying attention again"
    show teacher at right with move
    d "... In the 18th century Peter Pratley invented the font Comic Sans ms which was very popular in the past two decades. Luckily its popularity has waned and nowadays we see it as the tacky font it is."
    d "Now onto more important things like homework! This week you will be filming or taking pictures of the Hanze and create your own ambience profile of the Hanze "
    d "Dismissed!"



    play music "mark.mp3"
    scene gang with fade
    with Pause(2)
    show mark at right with fade
    m "Now this is one of my classmates and one of my best friends Mark."
    m "Me and Mark actually used to be colleagues at a famous fastfoodchain and by chance we met again when we both started here at the Hanze a few years back."
    m "Usually Mark is accompanied by either Jesse or Remand, but both of them don't seem to be near. "
    m "I wonder where they are."
    me "Hey man whatsup? Jesse and Remand not here today?"

    mr "No man, looks like it's just us today. Awesome ..."
    mr "Anyway what did you think about skills class? "

    menu:
        "It was quite interesting, more interesting then I expected it to be anyways.":
            $skillcool = True

        "It sucked big time man, I can't believe I wasted my time on this!":
            $skillcool = False

    if skillcool:
        mr "Yeah same. Can't wait to show what we the IT boyz can do!"
    else:
        play music "gameover.mp3"
        with Pause(5)
        show teacher at left with fade
        d "What did you just say? Let's see how you enjoy being expelled from the minor!"
        scene gameover with fade
        with Pause(5)


        return

    me "Yeah I know right, can't wait to see the look on their faces when we as IT outsiders will be one of the top performers."
    me "Anyhow, I think we still have some time left, so let's grab something to eat?"
    mr "Sounds good, I heard the canteen had pizza today, so we better hurry before everything is gone"
    stop music
    scene kantine with fade
    play music "kantine.mp3"
    $renpy.sound.play("restaurant.mp3", loop=True)
    #play sound "restaurant.mp3"
    with Pause(2)
    show mark with vpunch
    with hpunch
    mr "WHAT???"
    show mark at right with move
    show mark at left with move
    show mark with move
    hide mark with moveoutright
    show mark with moveinright

    with vpunch
    with hpunch

    mr "The pizza is sold out!!!"
    mr "What kind of bullcrap is this? I pay thousands of euros  for tuition and these idiots can't even provide enough pizza?!?"
    m "Mark is usually an easy going guy, but some things like pizza make him really passionate haha..."
    m "Best practice is to stop him while I still can"

    show mark at right with move
    show kok at left with moveinleft
    kok "Excuse me sir, is there something wrong?"
    mr "Is there something wrong? IS THERE SOMEHING WRONG? {size=+10}IS THERE SOMETHING WRONG?{/size} "
    with vpunch
    with hpunch
    mr "{size=+15}DUH!!! THERE IS SOMETHING WRONG!{/size}"
    with vpunch
    with hpunch
    mr "{size=+20}THERE IS NO FUCKING PIZZA IN THIS CANTEEN, THAT'S WHAT WRONG!{/size}"
    m "Oh dear, here we go. I so hope this will not end badly, maybe I should interfere?"



    menu:
        "Best speak up before this comes back to bite us in the ass...":
            $action = True

        "Are you kidding me, this is pure comedic gold!":
            $action = False

    if action:
        me "Hey Mark, I think you should calm down a little, we could always eat a snickers."

    else:
        stop sound
        play music "gameover.mp3"
        with Pause(5)
        hide kok with moveoutleft
        show teacher at left with moveinleft
        d "Do you think this is acceptable behaviour for young proffesionals such as yourself? Go wash your mouth with soap, YOU SCUMBAGS!"
        me "Hey mr. Skills it was just a prank bro, just a prank, we didn't mean nothing with it!"
        m "Alas there was no tolerance for misbehaviour within this minor :("
        scene gameover with fade
        with Pause(5)
        return

    mr "Yeah you're probably right... Sorry miss"
    kok "Humph, as you should be. This rudeness!!! I tell you back home in my country that is unheard of."
    kok "If you are to be the Crème de la Crème of this country, I fear for the future!"
    hide kok with moveoutleft
    me "Well that could've gone worse..."
    uv "Psst you guys........"
    uv "Psst psssst hey guys, hey guys..... "
    uv "{size=+15}Oi listen up lads{/size}!"

    play music "ron.mp3"
    show pizza at left with fade
    r "Hey you guys I am Meul Ronman and I like pizza."
    r "You might have heard of my pizza communication theory. My theory is proof that all communication is substantially strengthened with the support of pizza!"
    r "Therefore I have made it my mission to collect all the pizza in the world HAHAHA!"
    mr "Wait, you are collecting all the pizza?..."
    mr "{size=+10}So it is your fault that all the pizza is gone!{/size}"
    show gun at Position(xpos=580, ypos= 150, xanchor=0, yanchor=0)
    play sound "gun.mp3"
    with Pause(3)
    hide pizza
    show pizzamove at left
    with Pause(1)
    play sound "shot.mp3"
    hide pizzamove
    show pizzamove at left
    with Pause(1)
    hide pizzamove
    show pizza at left
    r "THAT WAS CLOSE"
    r "Take it easy! Watch were you're pointing that gun!"
    r "Where did you even get that gun?!? This ain't America Brother!"
    r "Put that thing away or I will expell you!"
    hide gun with dissolve
    r "Good know that's done I can get to the point."
    r "You see, I think I might be able to help you guys out...."
    r "If you do something for me I'll do something for you, you scratch my back, I scratch your back"
    r "So what do you think? Heh not a bad deal right?"
    show pizza at right with move
    play sound "shuffle.mp3"
    show mark at left with move
    mr "Hah, do you take us for fools?"
    mr "How could we even trust a pizza hoarding professor as yourself?"
    mr "I bet this is some ploy to steal even more pizza so we the studens will be left with nothing!"
    me "{size=+5}Yeah no way that we will submit to the tyranny of capitalism!{/size} "
    m "Wait a minute what am I saying..."


    menu:
        "That's right, communism is the supreme form of government, my blood is red":
            $commie = True

        "What am I thinking, Capitalism is life":
            $commie = False

    if commie:
        play music "soviet.mp3"
        scene soviet with dissolve
        with Pause(10)
        "Allright lets get back on track"

    else:
        play music "america.mp3"
        scene america with dissolve
        with Pause(10)
        "Allright lets get back on track"

    scene kantine with dissolve
    play music "ron.mp3"
    show mark at left
    show pizza at right
    m "Did I just break the fourth wall? Or have I been breaking it the entire time? What do you think reader?"
    with vpunch
    mr "Tell me why we shouldn't report you now for stealing all the pizza?"
    r "Relax, relax, as I said before we can help eachother out just listen to me...."
    r "If you give me your studentcards for two days, I will let you eat as much pizza as you want!"
    show pizza at left with move
    play sound "shuffle.mp3"
    show mark at right with move
    with hpunch
    mr "Sweet baby jesus.... {size=+10}You have a deal Meul Ronman!{/size}"
    hide mark
    hide pizza
    show pizza
    stop music
    r "Dont worry, you just eat the pizza and I will return your cards in a few days time, {size=-8} If you guys are still on this earth by then.... {/size}"
    play sound "horror.ogg"
    show ronhor behind pizza
    show ronhor behind pizza
    with Pause(4)
    play music "kantine.mp3"
    m "What was that?"
    r "Anyhow nice doing business with you guys, ciaoi!"
    hide pizza with moveoutleft
    with Pause(1)
    show mark at right with moveinleft
    mr "What an eccentric professor..."
    mr "But I dont really care I'm just glad to eat my pizza."
    play sound "eat.mp3"
    play sound "eat.mp3"
    me "If cookiemonster ever would be rebranded as pizza monster it would look just like you do right now"
    me "You're like a pizza Snorlax haha"
    mr "Hey I resent that hahaha"
    mr "On that note, it's probably best if we go get ourselves a camera or else they all might be gone"
    stop music fadeout 1.0


    play music "enigmatic.mp3"
    scene counter with fade
    show camera at left with moveinleft
    show mark at right with moveinright
    c "So you guys want to borrow a camera, is that right?"
    me "yeah basically"
    c "How come I haven't seen you guys around before?"
    c "What are you studying? Are you even part of the cmi?"
    c "Well?"
    mr "Look I don't like your attitude can you just give us a camera?"
    c "That depends can I?"
    m "Well can you?"
    show camera:
        parallel:
            ease .5 zoom 1.5
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5 #or whatever fit.
    c "Perhaps I could"

    show mark:
        parallel:
            ease .5 zoom 1.5
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5 #or whatever fit.
    mr "Then just do it"
    show mark:
        parallel:
            ease .5 zoom 1
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5 #or whatever fit.
    mr "......"

    show camera:
        parallel:
            ease .5 zoom 1
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5 #or whatever fit.
    c "Well I would like to, I have a bit of a problem though."
    me "And what might that be?"
    c "You see,  there are only a few cameras left so you either have to share and wait, or just say screw the rest and make your profit."

    menu:
        "First come first serve, I do not feel like waiting around and sharing":
            $own = True

        "Fair is fair, it might not be the most practical solution, but we should all share the camera.":
            $own =False

    if own:
        if commie:
            stop music
            hide mark
            show camera:
                parallel:
                    ease .5 zoom 1.5
                parallel:
                    yalign 0.0
                    linear 0.5 yalign 0.5 #or whatever fit.
            play music "gameover.mp3"
            c "I heard you when you were talking to Meul Ronman!"
            c "How dare you say you are a communist and then act like this!"
            c "No way in hell I'm giving you a camera"
            scene gameover with fade
            with Pause(5)
            return
        else:
            show camera:
                parallel:
                    ease .5 zoom 1.5
                parallel:
                    yalign 0.0
                    linear 0.5 yalign 0.5 #or whatever fit.
            c "Gunning for the top and screw the rest huh. I like that you guys!"
            c "Here's your camera, better make sure you end up on top Time For IT!"

    else:
        if commie:
            c "What a coincidence that I overheard your conversation with Meul Ronman!"
            c "I'm a communist myself and it does me great joy to see you stand by your values!"
            show camera:
                parallel:
                    ease .5 zoom 1.5
                parallel:
                    yalign 0.0
                    linear 0.5 yalign 0.5 #or whatever fit.
            c "{size=+10}I salute you comrad!{/size}"
            c "Here is your camera"
        else:
            stop music
            hide mark
            show camera:
                parallel:
                    ease .5 zoom 1.5
                parallel:
                    yalign 0.0
                    linear 0.5 yalign 0.5 #or whatever fit.
            play music "gameover.mp3"
            c "I heard you when you were talking to Meul Ronman!"
            c "I thought you were a capitalist!!"
            c "How dare you give in to this communist propaganda rubbish!"
            c "You are not getting a camera from me!"
            scene gameover with fade
            with Pause(5)
            return
    show camera:
        parallel:
            ease .5 zoom 1
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5 #or whatever fit.

    stop music fadeout 4.0
    play music ["<silence 2>", "mark.mp3"]
    scene gang with fade
    show mark with moveinright
    mr "We had our pizza, we have the camera. I think we're all set to go out and finish the assignment for Mr. Skills"
    me "Yeah I guess we can start, we just have to decide whether we want to capture the ambiance of the Hanze by day or night."
    "Well what is it going to be?"

    menu:
        "Let's take it easy and just shoot during the day":
            $day=True

        "Let's do something special and shoot at night":
            $day=False

    if day:
        play music "gameover.mp3"
        scene dddag with fade
        with Pause(4)
        scene klaslokaaldick with fade
        show teacher at left with moveinright
        d "Did you think you would pass this assignment by just filming by daylight?"
        d "You thought wrong...."
        d "I'm disappointed, I expected more from you guys"
        scene gameover with fade
        with Pause(5)
        return

    else:
        stop music fadeout 2.0
        scene avonddag
        with Pause(4.0)
        play music ["<silence 2>", "memories.mp3"]
        scene hanze with dissolve

    me "Allright time to see what kind of secrets the Hanze reveals at night!"
    show mark at right with moveinleft
    mr "Probably just a bunch of teachers who are heavily drinking and having some secret teacher party."
    me "That would be something wouldn't it."
    play sound "bat.mp3"
    mr "{size=+10}what was that?{/size}"
    play sound "bat.mp3"
    with Pause(1)
    play sound "bat.mp3"
    with Pause(1)
    play sound "bat.mp3"
    with Pause(1)
    me "{size=+15}What is going on ?!?{/size}"
    play sound "bat.mp3"
    with Pause(1)
    show bat at Position(xpos=150, ypos= 150, xanchor=0, yanchor=0) with moveinright
    mr "Oh it's just a bat phew..."
    me "Are you certain nothing is wrong? It seems to be fixating on you quite a bit.."
    show bat:
        parallel:
            ease .5 zoom 1.5
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5 #or whatever fit.
    b "Staring at Mark intensifies"
    show bat:
        parallel:
            ease .5 zoom 2.0
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5 #or whatever fit
    b ".........."



    show bat at bounce
    play sound "bat.mp3"
    with Pause(1.5)
    play sound "bat.mp3"
    with Pause(1.5)
    play sound "bat.mp3"
    with Pause(1.0)
    mr "Oi What the hell, leave me alone you stupid bat!"

    show bat:
        parallel:
            ease .5 zoom 0.5
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5 #or whatever fit
    show mark at center with move
    with Pause(1)
    show bat at bounce
    play sound "bat.mp3"
    with Pause(1.5)
    play sound "bat.mp3"
    with Pause(1.5)
    play sound "bat.mp3"
    hide bat
    with Pause(1.0)
    show mark at left with move
    show mark at center with move
    show mark at right with move
    mr "Thank god, I think I chased it off..."
    mr "Stupid bats, scaring the hell out of me.."
    me "What a start of the night haha. But now it's time to get to work."
    me "Let's split up. I will go shoot in de Vandoorenveste and you can go to the van Olsttoren, that fine with you?"

    show mark at wiggle
    mr "Yeah that sounds about right, I'm still a bit spooked by that bat though. Let's hope it's not an omen or something"



    stop music
    scene donkergang with Dissolve(4.0, alpha=True)

    play music ["<silence 2>", "ofeliasdream.mp3"]
    m "I have to say that a deserted Hanze is quite freaky."






    ######################## Hoe maak je een keuze?
    uv "Do you like ghost stories?"
    me "Where are you?"
    uv "I said do you like ghost stories?"
    me "This is not funny!"
    uv "Do YoU L1k3 H0rroR St0R13S??"

    menu:
        "Ofcourse why wouldn't I?":
            $likehorror = True

        "Ghost stories are for people who have no life":
            $likehorror = False

    if likehorror:
        uv "I wonder how long you will hold this opinion....."

    else:
        uv "How sad... That means you are in for a tough night."

    me "Look enough is enough where are you?"
    me "Show yourself right now or I will call the cops on you!"
    show neta at center with Dissolve(4, alpha=False)
    me "Now tell me who you are, because I am not joking around here."
    uv ".............."
    with vpunch
    me "Well?!?"
    n "My name is Neta Bosdoorn and you would do well to hold your tongue... That is... if you know what's good for you."
    play sound "witch.mp3"
    show neta at left with Dissolve(2, alpha=True)
    me "How did you just do that? What was that."
    n "As I said before, for your own good, you better listen to me."
    me"what are you talking about?"
    play sound "witch.mp3"
    show neta at right with Dissolve(2, alpha=True)
    n "You should not have come here after midnight.... There is a reason this building has a closing time"
    me "What?"
    show neta at wiggle
    n "You can come in any time you like, but before dawn you can never leave"
    me "What is this some kind of a lame Hotel California joke?"
    n "I will tell you two things which you would do well to remember!"
    play sound "witch.mp3"
    show neta at center with Dissolve(2, alpha=True)
    n "Firstly there is a photostudio which will unlock with your studentcard... In this room you will be safe.. If you reach it."
    n "Secondly:"
    n "^ < >  "
    n "Do with this information what you want."
    me "Seriously, that's it? Not even some bullshit explanation for this bullshit story of yours?"
    me "Well whatever"
    play sound "witch.mp3"

    hide neta with Dissolve(10, alpha=True)
    me "Oi, come back here woman!."

    m "Well, I suppose that was that...."
    m "I wonder if I might have been halucinating or something"
    m "Anyhow my next course of action should be:"

    menu:
        "Screw this Lady, I'm turning around and walking back out the way I came in":
            $ba = True

        "I should find a map and go to the safePhotostudio...":
            $ba = False
    if ba:
        stop music
        scene exit with Pixellate(5, 5)
        play music "sadday.mp3"
        m "I wonder why I even bothered to worry."
        m "Did that lady really think I would listen to her? I'm leaving and that's all there is to it."
        m "......."
        m "......."
        m "I can see the door already, I will be out of here in no time!"
        "Shuffle shuffle"
        stop music
        m "What whas that?"
        "............."
        ".........................................."
        m "Must have been my imagination"
        play sound "hello.mp3"
        m "What the f"
        play sound "name.mp3"

        m "{size=+20} Screw this I'm getting out of here{/size}"
        play sound "run.mp3"
        scene exit2 with Dissolve(5, alpha=False)
        m "Thank god I made it, no way I'm dying as some horror cliche!"
        play sound "locked.mp3"
        m "oh my god this can't be happening"
        play sound "name.mp3"
        m "{size=+20}SOMEBODY HELP ME!!!{/size}"
        play sound "locked.mp3"
        play music "gameover.mp3"
        show monster
        play sound "locked.mp3"
        with Pause(2)
        play sound "dying.mp3"
        show ronhor2 behind monster
        with Pause(5)
        scene listened with fade

        with Pause(4)
        scene gameover with dissolve
        with Pause(5)
        return








    else:
        stop music
        "Alrighty then"

    play music "downtown.mp3"
    scene trap with fade
    m "As I'm wandering down the halls I cannot help but get an uneasy feeling"
    m "It feels as if someone, or SOMETHING is watching me."
    m "However me being the adventurer that I am will not let myself be scared so easily."
    m "My heart is filled with courage I soldier on in order to acquire that amazing grade for Mr. Skills his class"
    m "As I am walking through the halls, I suddenly spot a notepad, laying abandoned on the ground."
    m "I wonder if I should pick it up?"

    menu:
        "Duh I pick it up,  who knows how handy this might be?":
            $notepad = True

        "Yeah, after the creepy stuff that has happened to me, there is no way I'm going to pick that thing up!":
            $notepad=False

    if notepad:
        "Allright I picked up the notepad and found directions to the safe Photostudio!"

    else:
        "I do wonder who would leave their notes lying around however. Mmeh not my problem."

    m "For quite some time I simply wander on through the halls."
    m "Nothing interesting seems to happen."
    show neta at center with fade
    m "Well, besides Neta's random appearances. "
    show neta at left with move
    m "I mean it is kind of annoying, but I'm able to ignore her pretty well now."
    m "So while I'm ignoring Neta I take some nice pictures and videos of an abandoned Hanze."
    hide neta with dissolve


    m "At some point I arrive at a crossroad, I wonder which direction I should take?"
    if notepad:
        menu:
            "I should follow the directions of the notepad":
                $notepad2 =True
                $saver=True
                $badroute =False

            "I should go up the stairs":
                $saver=True
                $notepad2=True
                $badroute =False
            "I should go downstairs":
                $badroute=True
                $saver=False
                $notepad2=False

    else:
        menu:
            "I should go up the stairs":
                $saver=True
                $badroute =False
                $notepad2 =False

            "I should go downstairs":
                $badroute=True
                $saver=False
                $notepad2 =False



    if saver:
        play music "kantine.mp3"
        scene kantine with fade
        m "It feels as if I have come full circle, seems like just a few hours ago I was bargaining for pizza with Meul Ronman."
        m "What a day it has been."

    else:
        scene gang with fade
        m "That's weird I thought for sure that I went another way, how weird that I end up at this corridor"
        m "Seems like I've arrived at Mr. Skills classroom, I think I can take some nice shots for my assignment in here."
        menu:
            "Go in":
                scene klaslokaaldick with fade
                play music "gameover.mp3"
                show monster
                play sound "dying.mp3"
                show ronhor3 behind monster
                with Pause(5)
                scene listened with fade

                with Pause(4)
                scene gameover with dissolve
                with Pause(5)
                return
                return


    m "This cafetaria has some nice great shading at night. Best to take a few pictures for Mr. Skills."
    with hpunch
    with vpunch
    m "OUCH!!!"
    m "I'm such a klutz, tripping over my own feet... "
    m "This might be a sign from above to just move on quickly..."
    m "So far everything seems to be going just fine, you know except the whole illusion of Neta whom I keep seeing"
    show neta at right with dissolve
    play sound "witch.mp3"
    m "Ah well"
    hide neta with dissolve
    m "Anyhow I should call Mark."
    play sound "ring.mp3"
    "Beep beep beep"
    with Pause(3)
    stop sound
    mr "Hey man all good?"
    m "Yeah its allright I guess, I'm a bit spooked but that was bound to happen anyways."
    mr "So yeah I was thinking we could {size=- 25} finish up and meet shortly? {/size}"
    play sound "storing.mp3"
    m "Mark, hello Mark? OI OI."
    m "Ah well seems like bad reception"

    m "Time to move on"
    m "As I keep walking I keep feeling this strange presence watching me. I wonder what it is"
    scene counter with fade
    m "Looks like I'm back at the workplace of that slightly crazy woman."
    m "Where to go next I wonder?"
    "Well where do you go?"

    if notepad2:
        menu:
            "I should just follow the route to the save studio.":
                $notepad3 =True
                $bad2 =False
                $notepad2 =True
            "I have a feeling I should go left":
                $saver2 =True
                $bad2 =False
                $notepad2 =True
                $notepad3 =True
            "I should go down":
                $bad2 =True
                $notepad3 =False
                $saver2 =False
                $notepad2 =False


    else:
        menu:
            "I have a feeling I should go left":
                $notepad2 =False
                $saver2 =True
                $bad2 =False
                $notepad3 =False
            "I should go down":
                $bad2 =True
                $saver2 =False
                $notepad2 =False
                $notepad3 =False
    if bad2:
        scene counter with fade
        m "That's weird, have I been walking in circles?"
        m "Ah well, guess I best check behind the counter."
        menu:
            "Check behind the counter":
                scene counter with fade
                play music "gameover.mp3"
                show monster
                play sound "dying.mp3"
                show ronhor4 behind monster
                with Pause(5)
                scene listened with fade

                with Pause(4)
                scene gameover with dissolve
                with Pause(5)
                return
                return

    else:
        scene klaslokaaldick with fade
        play music "mark.mp3"

    m "Seems I'm back on the right track again"
    m  "....................................."
    m "Wait what was that?"
    m "......................................."
    play sound "bat.mp3"
    show bat at bounce
    play sound "bat.mp3"
    with Pause(1.5)
    play sound "bat.mp3"
    with Pause(1.5)
    play sound "bat.mp3"
    with Pause(1.0)
    m "C'mon really again? .........."

    show bat:
        parallel:
            ease .5 zoom 0.5
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5 #or whatever fit
    with Pause(1)
    show bat at bounce
    play sound "bat.mp3"
    with Pause(1.5)
    play sound "bat.mp3"
    with Pause(1.5)
    play sound "bat.mp3"
    hide bat
    with Pause(1.0)
    m "I wonder what the board of the Hanze would say if they knew they had a bat infestation."
    m "Wait a minute...."
    m "I should capture a picture of the bat and present it to the board."
    m "I never cease to be amazed by my own brilliance."
    m "Onwards we go........"
    stop music
    scene trap with fade
    play music "fishing.mp3"
    m "And we're back here again."
    with hpunch
    with vpunch
    m "My god this is just the gift that keeps on giving."
    m "How on earth can I get lost so many times??????"
    m "THIS TIME HOWEVER, I CAN FEEL IT."
    m "I feel like I might finally bring this journey to an end."
    m "Once again, where should I go? ......."
    "Well where do you go?"

    if notepad:
        menu:
            "I should just follow the route to the save studio.":
                $notepad4 =True
                $bad3 =False
                $saver4 =False
            "I have a feeling I should go right":
                $saver4 =True
                $bad3 =False
                $notepad4 =False
            "I should go down":
                $bad3 =True
                $notepad4 =False
                $saver4 =False

    else:
        menu:

            "I have a feeling I should go right":
                $saver4 =True
                $bad3 =False
                $notepad4 =False
            "I should go down":
                $bad3 =True
                $notepad4 =False
                $saver4 =False

    if bad3:
        scene kantine with fade
        m "That's weird, back at the restaurant again"
        m "Migh as well check if there''s still some pizza left."
        menu:
            "Search for pizza":
                scene kantine with fade
                play music "gameover.mp3"
                show monster
                play sound "dying.mp3"
                show ronhor behind monster
                with Pause(5)
                scene listened with fade

                with Pause(4)
                scene gameover with dissolve
                with Pause(5)
                return
                return

    if notepad4 and notepad3:
            scene foto with fade
            stop music
            play sound "hello.mp3"
            m "I think I just heard something"
            m "Anyways, seems like I made it safely to the Photostudio"
            play sound "name.mp3"
            m "The sounds are getting closer... No time for lazing around, let me get myself to safety!"
            "Well, what are you waiting for? Enter the room!"
            menu:
                "Enter the room":
                    scene foto with fade
                    play music "gameover.mp3"
                    m "I cannot enter the room, what kind of bullshit is this?"
                    show pizza
                    r "HAHAHAHAHAHAHAHA"
                    r "HAVE YOU FORGOTTEN?"
                    r "DID YOU NOT PAY ATTENTION?"
                    r "NETA SAID IT HERSELF, YOU NEED A STUDENT CARD TO ENTER THIS ROOM!!!!!"
                    r "HOW SAD, YOU HAVE TRADED YOUR TICKET TO SAFETY FOR A FEW SLICES OF PIZZA"
                    r "IT SEEMS THAT GLUTTONY TRULY IS THE DEADLIEST SIN!"
                    play sound "dying.mp3"
                    show ronhor5 behind pizza
                    with Pause(5)
                    scene listened with fade

                    with Pause(4)
                    scene gameover with dissolve
                    with Pause(5)
                    return
                    return

    if saver4:
        scene titel with dissolve
        m "Wow looks like I mad it through the night"
        stop music
        play music "mark.mp3"
        scene dddag with fade
        with Pause(4)
        scene klaslokaaldick with fade
        show teacher at left with moveinright
        d "Wow you guys of Time For IT have truly done a splendid job with this assignment."
        d "I cant believe how much you have outshined the other teams from your class!"
        d "You have done something to be proud of!"
        d "And I'm proud to have been your teacher"
        scene victory with fade
        with Pause(5)
        "click"
        return



    #    label ilikeh:
    #        d "cool"
    #        return
    #    label ihateh:
    #        d "whatever"
    #        return

    # This ends the game.

    return
