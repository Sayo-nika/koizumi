label ca4:
    stop music fadeout 1.0
    scene bg library_out
    with wipeleft
    "We arrive at something called... the library."
    "And me, still acting like a snobby gentleman because apparently it turned into my true personality, I gently open the door for Sayonika and enter."
    scene bg library_in
    with wipeleft
    "Hey, the library looks just like, well... like a library."
    "Mountains of books in the bookshelves and no one in sight..." 
    "I really can’t help but think about Yuri picking up an anatomy book and doing the act..."
    "We proceed to the main counter where I spy someone I recognize."
    "Yuri."
    "She glances at me, then at Sayonika."
    play music t6
    show yuri 1 at t11
    y 3bn "S-Sayonika? What are you doing here? I thought you said you didn’t like reading in here..."
    show yuri at t21
    show sayonika 2b at f22
    sm "Ehehe... well..."
    sm 4e "I was just showing someone around the city, sooo I decided to come over with him to the library: my good friend [player]!"
    mc "More like acquaintance."
    sm 1i "Yeah... I suppose that’s a better way of putting it. We met each other earlier at the train station."
    sm 3b "He’s gonna stay with me for summer school."
    "Yuri appears to look at me, trying to confirm what she hears."
    show sayonika at t22
    mc "Yes, that’s quite right."
    show sayonika at f22
    sm 1r "Is there something wrong Yuri?"
    show yuri at f21
    show sayonika at t22
    y 3bp "A-Ah...!"
    y 4bb "Everything is fine... I just wasn’t expecting you here. The Portrait of Markov sucked me in again so I’m glad you came..."
    y 2ba "How may I help you?"
    show yuri at t21
    mc "Well, we were here to meet you."
    mc "Though the last place I would expect you to be working in is a library."
    mc "Essentially, Sayonika mentioned you’re going to summer school with us."
    show yuri at f21
    y 2bq "O-oh. She did?"
    y 2bj "Well... it’s true that I {i}am{/i} going to summer school as well..."
    y 3bn "Not because I failed this year’s classes...!"
    y 4bb "That would be awful for my mental health..."
    y 1bh "But because Monika forced us to come, what with that contract of hers..."
    show yuri at t21
    mc "And I guess I was a part of that contract too..."
    
    "That reminds me... hey, Yuri?"
    show yuri 1be at t21
    menu:
        "Snitch on Sayonika.":
            $ sayonika_snitch = 1
            jump sayonika_snitch_return

        "Stay quiet.":
            $ sayonika_snitch = 0
            y "Hm?"
            mc "...nah."
            mc "So I was just thinking, Yuri... you get decent paychecks, right?"
            show yuri at f21
            y 1bf "Yes, yes I do."
            mc "How much do they pay you?"
            y 4bb "I'd rather not say. I-it's a little embarrassing."
            show yuri at t21
            mc "I understand."
            jump ca4_cont1
    
    label sayonika_snitch_return:
        stop music fadeout 1.5
        mc "Sayonika made a {i}cutting{/i} joke about you before we came."
        play music t7
        show yuri at f21
        y 3bp "S-Sayonika!"
        show sayonika at f22
        show yuri at t21
        sm 1p "[player]!!"
        show sayonika at t22
        "I smugly shrug her away, knowing I put her in an awkward position."
        "But she deserves it, after all."
        show yuri at f21
        y 2br "You know I hate those jokes! They're... really starting to get on my nerves."
        show sayonika at f22
        show yuri at t21
        sm 2i "S-Sorry Yuri, I swear I’ll stop this time..."
        "Stop {i}this time?{/i}"
        show yuri at f21
        show sayonika at t22
        y 2br "This is the fifth time you’ve made one of those jokes this week!"
        y 2bt "You always say you’ll stop, but you never do..."
        y 2br "How do I expect you to keep your word this time?"
        show sayonika at f22
        show yuri at t21
        sm 1i "U-um... ehehe..."
        show yuri at f21
        show sayonika at t22
        y 1bw "Fine... I’ll forgive you, but this is your last chance."
        y 1bg "But if I hear another one of those jokes coming out of your lips..."
        y 1bg "Or if someone tells me you've made another one..."
        show sayonika 1x at h22
        $ style.say_dialogue = style.edited
        y 2by7 "I won’t hesitate to shove some soap into your filthy, disgusting, putrid mouth, you big bag of shit!"
        y "I'll drown you in holy water! You deserve every ounce of bleach, every kilo of soap!"
        y "Every!{w=1.0} Single!{w=1.0} Bit!"
        $ style.say_dialogue = style.normal
        "After that catastrophe and almost shoving soap down Sayonika's throat, she relaxes."
        jump ca4_cont1
        
    label ca4_cont1:
        stop music fadeout 1.5
        y 1be "Ahm...{w=0.5} anyway! What kind of books should I get you two?"
        show yuri at t21
        show sayonika 1k at t22
        mc "I would like... hm..."
        play music t8
        show yuri at f21
        y 1bb "Wait. I think I know of a book you two might like."
        show yuri at t21
        "Yuri heads towards a bookshelf and returns with two books in her hands."
        show yuri at f21
        y 2bf "[player], I know you don’t read a lot, so I thought this book might be kind of fitting for you."
        y "It’s a short read so it will be a little easier for you to read along."
        show yuri at t21
        "I take a look at the book’s cover."
        "The first sentence I can see is {i}\"Go the Fuck to Sleep.\"{/i}"
        "I am not disappointed."
        mc "Thanks Yuri. This definitely does look like a must-read..."
        show yuri at f21
        y 3bc "I’m glad."
        y 1bb "As for you, Sayonika..."
        y 2bj "You have to read this book about... PHP."
        show sayonika at f22
        show yuri at t21
        sm 1f "PHP?"
        show yuri at f21
        show sayonika at t22
        y 1bf "It’s some programming language that I suppose fits you as a person so I thought why not give it a read."
        show sayonika at f22
        show yuri at t21
        sm 2i "Oh... uh, thank you, Yuri!"
        show yuri at f21
        show sayonika at t22
        y 2bf "By the way, those are the books you will be reading this summer."
        show yuri at t21
        mc "Guess I got the easy book to read then."
        show sayonika at f22
        sm 1v "Wait, whaat? No fair! Why do I have to read a 500 page textbook about a coding language while [player] gets a little book with a short story about how he can go the heck to sleep?!"
        show yuri at f21
        show sayonika at t22
        y 2br "Sayonika! Shhh...!"
        y "This is a library! Please! Don’t you have any manners?"
        show sayonika at f22
        show yuri at t21
        sm 1i "Ehehe..."
        show yuri at f21
        show sayonika at t22
        y 3bw "For goodness sake..."
        y 1bg "Come on, I’m sure you already know about how dense [player] is by now."
        show yuri at t21
        mc "{i}I’m not dense! Hmph!{/i}"
        "I notice my tsundere tone and blush in embarrassment."
        show yuri at f21
        y 2bt "Sorry, I meant you’re not familiar with reading books. I remember when you told me that novel books are your mortal enemy because they lack pictures."
        y 2br "What did you expect me to do? Give him a biography? Give him some geography?"
        y 1bv "He’s too new to read something without pictures to go along with the words."
        y 1bw "And he wouldn't possibly know how to answer the questions in Monika’s Summer Reading Test Papers if I gave him something different."
        show yuri at t21
        "Are you calling me a child? Ow, my feelings...!"
        show sayonika at f22
        sm 2p "But this doesn’t explain why I have to read a textbook while he gets to read a short story!"

        if sayonika_snitch == 0:
            sm "Is it because you think I can read this?"
            show yuri at f21
            show sayonika at t22
            y 2br "If you can read books, then you can read that book on PHP!"
            show sayonika at f22
            show yuri at t21
            sm 1o "Okay, I understand. You want me to read this because I'm stupid and I need more brain."
            show yuri at f21
            show sayonika at t22
            y 1bj "You've already nailed your first assignment from me on realising your stupidity. Good job~"
            show sayonika at f22
            show yuri at t21
            sm 1y "Meanieee!"
            show sayonika at t22
            mc "Come on, you two... Sayonika, we need to find Sayori now."
            show sayonika at f22
            sm 2i "Oh yeaaah. I forgot!"
            mc "What did you forget?"
            sm 1b "I forgot about Sayori, we still need to check on her!"
            mc "Now that I think about it... why exactly didn't you check beforehand?"
            sm 1i "Um... I didn't think about that."
            mc "Hello; Sayonika's Brain? This is [player] asking you to think harder!"
            sm 1x "Uwaa~! I'm sorry!"
            show sayonika at t22
            mc "I'm kidding. Let's go, then!"
        if sayonika_snitch == 1:
            sm 1j "Is this revenge for the joke I made?"
            show yuri at f21
            show sayonika at t22
            y 2br "What did you think? Did you think I gave it to you just because I thought you wanted to code? I already know you’re nothing like Monika!"
            show sayonika 1x at h22
            y 2by7 "So take a spoonful of my medicine and see how it feels!"
            show sayonika at f22
            show yuri at t21
            sm 1o "Oh... oh. Oh. W-well, now we need to find Sayori and make sure she’s going as well, even though I have a feeling everyone from the Literature Club is going, including me..."
            mc "Where could she be right now though?"
            show yuri at f21
            show sayonika at t22
            y 1bf "I did see her come in here to run some errands, and then left. I think she was heading... south possibly?"
            mc "Well, I guess we should go and find her then!"
            show yuri at t21

        "Hmmm..."
        menu:
            "Leave the Library quietly.":
                mc "Alright then. See you later, Yuri!"
                pass
                $ slap_sayonika = False
            "Slap Sayonika before leaving." if sayonika_snitch == 1:
                "I slap Sayonika so painfully that the noise can be audibly heard throughout the huge library."
                show sayonika 1x at h22
                sm "Uwaaaaaaaah!!"
                mc "Alright. See you later Yuri."
                show yuri at f21
                y 1ba "See you two later!"
                $ slap_sayonika = True
        
        if slap_sayonika = True:
            sm "W-what was thaaat for?!"
            mc "For the shitty joke."
            sm "Okay, I'll admit it... I deserve it..."
            sm "But that doesn't give you permission to slap me so heartlessly!!"
            mc "Hell yeah it does! I've known Yuri for longer than you!"
            "We walk down the street in silence for a moment before I speak up."
            mc "Hey, Sayonika..."
            mc "When I get ready to hit the hay, could you read me my book?"
            sm "No! You're a meanieee!"
            mc "Well I'm sorry I told Yuri the truth."
            sm "Tattle-tale, goodie two-shoes!"
            mc "Jeez, okay! Okay!"
            "We continue to walk in silence. My cheeks had turned red from embarrassment during the conversation."
            $ read_sayonika = False
            return
            
        if sayonika_snitch == 1:
            mc "Hey, sorry for snitching by the way."
            sm "It's... okay."
            pass
            
        scene bg library_out
        with wipeleft
        "We walk out of the library through the glass door entrance and wave Yuri goodbye before beginning to walk down the street."
        "We stop for a moment, so I decide to say something embarrassing to her to see how she’d react. As they say, it’s better to get to know the kind of person the girl you're going to be living with for the whole summer is."
        mc "Hey... Sayonika?"
        show sayonika 1a at t11
        sm 1g "What’s up [player]? {i}Uh oh...{/i}"
        mc "When we get back to your place tonight... "
        mc "Can you read me the book Yuri gave me when I go to bed?"
        show sayonika at h11
        sm 1u "Uwaaa!!"
        sm 2o "You have to be joking... right?"
        mc "Do I look like I’m joking?"
        sm 1i "Eheh..."
        sm "Uhmm..."
        sm 1o "I guess... I c-can...?"
        "I roll in excitement and laughter as she gives me the thumbs up."
        "I know that doing this will definitely help me find out more about who Sayonika is as a person."
        "But there is no way I can stop now, for there are ways to go further!"
        "I must stretch the dough as far as it goes, by showing her the book and telling her about how I’m about to ‘going the fuck to sleep’ so she can read me it."
        "Delightfully devilish, Seymour!"
        mc "Thanks Sayonika! You’re the greatest!"
        show sayonika 1i at t11
        "The day continues to get better and better as time advances."
        $ read_sayonika = True
        return
