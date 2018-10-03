label ca3:
    # TODO: Replace this with bakery background
    stop music fadeout 0.5
    scene bg bakery
    with wipeleft
    play music t3
    $ b_name = "Baker 1"
    $ b2_name = "Baker 2"
    "We arrive at the bakery pretty quickly." 
    "But then again, Sayonika was profusely sweating and panting just to get here." 
    "I open the door for her as she enters sheepishly licking her lips." 
    "As she enters, myself included, I hear the baker shout towards her."
    
    $ n_name = "Baker"
    n "Jeez, Sayonika! Have you been running a marathon again? You're way too hyperactive for your age!"
    show natsuki 3be at t11
    "I perk my head up and notice Natsuki in a baker’s outfit behind the counter." 
    "Her outfit was much different to the other bakers."
    mc "Natsuki?"
    $ n_name = "Natsuki"
    n 2bc "Eh?"
    n "[player]! I didn’t think you'd be in this part of town! What are you here for, anyway?"
    show natsuki at t21
    show sayonika 2x at f22
    sm "I... *pant* brought him... here..."
    show sayonika at t22
    mc "I didn’t know you worked for a bakery!"
    show natsuki 5be at f21
    show sayonika at t22
    n "My bakery, mind you! Sayonika, if you’re going to bring Sherlock here, at least tell me first! Hmph!"
    mc "What’s that supposed to mean?"
    n 5bx "Don’t you know what it means? A-and why does it concern {i}you?!{/i}"
    "She walks sluggishly back to the counter, intently staring down at the dough she had been kneading earlier." 
    "She then continues kneading it before putting it in the oven."
    mc "So, how long have you had this bakery for?"
    n 1bq "A while. A good friend helped me get this place going."
    show sayonika at f22
    show natsuki at t21
    sm 2h "Why’re you so wary of mentioning her name, Suki?"
    show sayonika at t22
    show natsuki at f21
    n 4bf "Don’t call me that you baka!" 
    n 5bh "Look, just don’t push it; he got pretty weirded out from the last visit. I’m sure he’s fine {i}not{/i} seeing her after like, a year..."
    mc "I-it’s fine, Natsuki..."
    n 2bc "Well, what do you want, dummy?"
    mc "I, uh... well... ummm..."
    "I... don’t really know what I want right now."
    show sayonika at f22
    show natsuki at t21
    sm 1i "Just give him some time, Natsuki..."
    show sayonika at t22
    show natsuki at f21
    n 5bz "Screw it. I’ll make something special for you!"
    n 4br "Consider it compensation for dealing with... you know who."
    show sayonika at f22
    show natsuki at t21
    sm 1p "Heey! That’s mean..."
    show sayonika 1k at s22
    n 2bk "I feel almost sorry for you, [player]. She’s a bit of a handful to deal with." 
    n "I’m surprised you two hadn’t really interacted with each other during the spring break..."
    mc "Natsuki, I literally just met her properly this morning." 
    mc "I might’ve seen her back there, but she must’ve been more interested in Monika than me..."

    "Suddenly, A short, red-haired girl steps out from the side of the bakery."
    $ mi_name = "???"
    show natsuki at t32
    show sayonika 1f at t33
    show mio 8s at l31
    mi "What in the world is going on here?"
    show natsuki at f32
    n 1bf "Get back to your darn danishes, toots!"
    show mio at f31
    show natsuki at t32
    mi 8u "There will never be a day... oh!" 
    mi 6e "Hi, [player]!"
    mc "Oh, dear God..."
    "Ah, yes. Mio..." 
    "She was the club’s newest member back in the winter and we often read Japanese classics with each other."
    "At one point, we were reading {i}The Illusion of Living{/i} with Yuri."
    "Before the spring break, she was a unique individual: cute, proper, charming..."
    "Completely out of my league at that time."
    "Things got a little out of hand during spring break when we went on a trip to Disney's animation studio."
    "Okay, {i}maybe{/i} that was a bit of an understatement."
    "Her personality drastically changed from a proper lady to a downright ruthless monster."
    "I don’t know exactly why or how, but I’m pretty sure Monika or her boss knows. in a matter of days."
    "I think Monika said something about it being too difficult for me to understand...?"
    "Her boss was certainly less than enthusiastic about it, and things went down."
    "I try to keep my distance, but she always seems to blatantly disregard it."
    "The only word I understood from that was monster..."
    "I already know one monster, but she's not... the right kind of monster."
    $ mi_name = "Mio"
    mi 4h "What? Are you going to sta{nw}"
    $ _history_list[-1].what = "What? Are you going to stare—"
    show natsuki at f32
    show mio at t31
    n 2be "I said {i}get back to your danishes{/i}! I don’t want you giving my customer here a heart attack."
    mi 3u "As you wish, Missus Drew..."
    "Mio slips back to the side."
    show mio at lhide
    hide mio
    show natsuki at f21
    show sayonika at t22
    n 5bc "She’s still shaken up from the break, you know?"
    mc "I’m surprised she’s working for you. Especially you!"
    show sayonika at f22
    show natsuki at t21
    sm 2h "Yeah, me too. She’s been practically barred from the boss's presence."
    show natsuki at f21
    show sayonika at t22
    n 4bd "Right. It’s both a rehab program and eternal torture for her. Whatever, works for me!"
    n 4bk "Say, [player]... it’ll take a few minutes for this to finish. You’re not in a rush, are you?"
    mc "Yeah, yeah! Totally fine by me, I’m in no rush."
    show sayonika at f22
    show natsuki at t21
    sm 1i "I’m with him, so..."
    show sayonika at t22
    show natsuki at f21
    n 3bd "Well, duh! He doesn’t have a clue about the bakery, how would he manage to get here without you? Anyway, what did you want?"
    show sayonika at f22
    show natsuki at t21
    sm "Just a donut will do..."
    show sayonika at t22
    show natsuki at f21
    n 5by "Jeez, a donut? Might as well order a coffee, too. Toots!"
    "She signals towards Mio."
    show mio at l31
    show natsuki at t32
    show sayonika at t33
    mi 3r "Ugh, really?"
    show natsuki at f32
    n 4bd "Get a pot brewing, please..."
    show mio at f31
    show natsuki at t32
    mi 8v "Whatever."
    show mio at lhide
    hide mio
    "Mio walks over to the counter and turns on the coffee machine." 
    "Meanwhile, another baker walks towards Natsuki with a phone in his hand while covering it up."
    show baker 1d at l31
    b "Ma\'am, we got a big order comin\'."
    show natsuki at f32
    n 4bd "Ha! Of course..." 
    n "Well, my hands are a bit tied up at the moment." 
    n 5by "Soldier! Are you ready to make history?!"
    show baker at f31
    show natsuki at t32
    b 1j "W-what do you mean?!"
    show natsuki at f32
    show baker at t31
    n 4bd "I want you to lead the team and handle the order while I take care of this very important order!" 
    n 5bz "Ganbatte!"
    b 1l "Yes, ma’am!"
    show baker at lhide
    hide baker
    show natsuki at t21
    show sayonika at t22
    "The baker signals the rest of the team, gradually informing them of the order at hand."
    show natsuki at f21
    n 4bl "He’s new here, so I’m training him myself. Pretty good chap if I must say so myself..."
    mc "Ah."
    show sayonika at f22
    show natsuki at t21
    sm 3k "She’s pretty good at training these guys."
    show natsuki at f21
    show sayonika at t22
    n 4bc "So, what brings you to this part of town, hmm?"
    mc "Well, I somehow managed to land in... summer school??"
    show natsuki 4bz at t21
    "Natsuki breaks out in laughter as Sayonika smirks."
    show natsuki at f21
    n 4bt "And what? Sayonika’s bunking with you or something?"
    show sayonika at f22
    show natsuki at t21
    sm 3c "Y-yeah..."
    show sayonika at s22
    "Natsuki continues, laughing harder."
    mc "What’s so funny, Natsuki?"
    show natsuki at f21
    n 4bd "It’s not what you think it is, [player]! I’ll tell you this much, it’s not dealing with school. We’re done with school, my friendo!"
    mc "Yeah, I kinda {i}was{/i} wondering how I managed to get into summer school."
    n "Because it’s not, you big dummy." 
    n 5bc "It’s an organized event by Monika. She must have taken a lesson or two from Sayonika’s ol’ you know who."
    show natsuki 5bz at t21
    "Natsuki giggles shamelessly."
    show sayonika at f22
    sm 1x "Uwaa?"
    show natsuki at f21
    show sayonika at t22
    n 4bq "My God, Sayonika... you know, I thought you were supposed to be the smart one."
    n 2be "Did you seriously think that you, a senior, would have to go back to summer school? After you graduated and everything?"
    n 1bp "How did you out of all people not figure this out?" 
    n 5bx "Hell, I’m not one to read things other than manga, but I still saw it! I can totally see [player] having not realised ‘cus he’s fit yet stupid, but I didn’t know you were so... gullible."
    show natsuki at t21
    show sayonika at f22
    sm 2w "B-but..."
    show sayonika at t22
    mc "Are you trying to say I’m a stereotypical jock? Well whatever, that clears things up nicely anyway, doesn’t it?"
    show sayonika at f22
    sm 1p "It’s not fair! How was I supposed to know?!"
    show natsuki at f21
    show sayonika at t22
    n 2bb "It is if you look at the fine print, Sayonie! The darn thing was in quotation marks!"
    mc "Well, isn't Monika a little devil darling?"
    n 5bz "Dannng! That's a good one, I need to write that down and save it for later!"
    show natsuki at t21
    "As Natsuki pulls something out of the oven, she cackles like a witch from something out of a movie." 
    "A couple of other bakers join her in the cacklefest. Really, a spookfest more than anything."
    show natsuki at f21
    n 5bc "Don’t stress it, [player]." 
    n "If it’s anything I’ve learned about this chica filet over here, she may have Monika’s brains, but it never pulls through mornings." 
    n 5bq "It’s almost like she goes braindead or something while she’s sleeping, and all of a sudden recovers midday after eating a donut from my bakery!" # Shameless plug lol
    n 5bc "Reminds me a lot of Sayori, too..."
    mc "So you're saying Sayonika is Monika's stupid cousin?"
    n 4by "Ooh burn!"
    sm 1p "What?! I'm not stupid!!"
    "As Natsuki finishes the pastry with chocolate filling, Mio struts over sassily with the coffee in hand."
    show mio 5r at l31
    show natsuki at t32
    show sayonika 1g at t33
    mi "Here, bossy boots..."
    show natsuki at f32
    n 4bf "Hello? There’s clearly two people here and only one cup!"
    show mio at f31
    show natsuki at t32
    mi 6t "Ugh, {i}so{w=0.5}-rry{/i}."
    "Mio waltzes over sloppily to the coffee machine again and makes another cup." 
    "She returns to the counter again, cup in hand."
    mi 8r "We good now, boss?"
    show natsuki at f32
    show mio at t31
    n "Perfect. Now continue your danishes."
    show mio at f31
    show natsuki at t32
    mi 1v "Well, just let me know if you{w=0.75}{nw}"
    $ _history_list[-1].what = "Well, just let me know if you—"
    show natsuki at f32
    show mio 5p at t31
    n "{b}You speak when spoken to, toots!{/b}"
    "A baker nearby chuckles before replying."
    b2 "Got it, JonTron!"
    n 5bz "Finally! Someone who understands my intellectual humor."
    "She smiles intently as she looked at the both of us."
    "Without saying a word, Mio slowly slips into the back storage, embarassed and probably angry."
    show mio at lhide
    hide mio
    show natsuki at t21
    show sayonika at t22
    mc "So, how much will I be paying?"
    show natsuki at f21
    n 4bc "Isn’t she paying?"
    show sayonika at f22
    show natsuki at t21
    sm 2i "Ummm... yeah... ehehe..."
    show natsuki at f21
    show sayonika at t22
    n 5bd "I figured. [player], don’t sweat it. It’s on the house~"
    mc "Natsuki, you don’t have to..."
    n 5bz "It’s fine!" 
    n 4bt "I’ll be seeing your smug face anyway after this round-the-clock busy shift."
    show sayonika at f22
    show natsuki at t21
    sm 1p "Wait, heey! What does that mean?"
    show natsuki at f21
    show sayonika at t22
    n 4bb "Well, I’m a part of this event too, you know." 
    n 4bt "Someone needs to take charge of the food!"
    mc "Well, it makes sense. The only other person who could make food is Monika, but I’m not exactly too keen on her skills..." 
    mc "Mucho gracias, Natsuki."
    n 5bz "No problem. You better get a move on, I got a big order going out the counter, so... you may want to move before donuts start flying and all an’ all that jazz!"
    mc "Alright. See you soon!"

    scene bg plaza_day
    with wipeleft
    "As we head out the door, Sayonika starts to babble."
    show sayonika 1g at t11
    sm "That’s so weird. She seems so playful today."
    mc "Well, I guess running that bakery makes her happy, you know?"
    sm 1i "I guess... well, there’s one stop I want to make first. See a good librarian."
    mc "Oh?"
    sm 4f "I have a funny feeling she’ll be joining us in \"summer school,\" too..."
    mc "Okay..."
    sm 1q "She runs a library that’s on the {i}cutting edge{/i} of technology."
    mc "Wha?! I can’t believe you just...! You can’t be serious!"
    "Suddenly, I remember the good times I’ve had with her." 
    "She was always calm, even when things got a bit intense." 
    "Luckily for us, she and Natsuki got along well after the spring break!" 
    "Monika now keeps tabs on her so that we don’t worry about her... eccentric hobbies."
    mc "Bad pun! Bad pun! No encore!"
    sm 3b "Ehehe~ she’s quite a gal!"
    mc "Don’t give me a heart attack, honestly... I thought she was being monitored to prevent this kind of stuff."
    sm 2q "Come on, you have to admit that was a good pun!"
    "Reluctantly, I follow Sayonika to the public library. Maybe I should snitch on Sayori." 
    "But I don't really know Sayonika well. Maybe Yuri enjoys her stupid jokes." 
    "Natsuki seemed to be quite comfortable with her around." 
    "{i}This will be a very interesting summer...{/i}"
    return
