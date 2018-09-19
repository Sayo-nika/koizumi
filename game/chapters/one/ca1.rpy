label ca1:
    stop music fadeout 1.0
    scene bg train_station
    with dissolve_scene_full
    play music t2
    "So here I am, waiting…"
    "Waiting…"
    "Waiting…"
    "The horizon looks nice - but I’m still unphased, with me being a couch potato and all."
    "That’s probably why I believe fate decided to take a dump in my sister’s mouth and have her sending me somewhere for the rest of the summer break."
    "And that means also means I have no manga or anime to watch until summer school is over."
    "Oh well… this is gonna be {i}fun…{/i}"
    "The train stops, marking the end of my journey and my window-gazing. Well... at the very least for now."
    "Nonetheless, I stand up carrying my things and walk outside of the train onto the station platform."
    "And so, the suffering begins."
    return

label ca2:
    scene bg plaza_day
    with wipeleft
    "After leaving the station, I sit down on a nearby bench before proceeding to call a number my sister handed to me before I left. She’ll take me to where I need to go, she said."
    "I sigh and call the number."
    mc "Hello?"
    "I didn’t expect she’d answer over my greeting."
    $ sm_name = "???"
    sm "Hello? Who is this?"
    mc "Uhm… It’s me, [player]... my sister told me you knew each other… and{nw}"
    $ _history_list[-1].what = "Uhm… It’s me, [player]... my sister told me you knew each other… and—"
    "She gasps and squeals in the phone."
    sm "Oh my god, really?! You’re here?! Give me a second, I’ll be there in a jiffy!"
    mc "I’m just at the{nw}"
    $ _history_list[-1].what = "I’m just at the—"
    "And she drops the call."
    "Perfectly timed, as all things should…"
    "Does she already know where I am…? Only God knows, so I just continue sitting on the bench and carry on playing a visual novel I forgot to finish eons ago."
    scene bg plaza_day
    with dissolve_scene_full
    pause 3.0
    "It’s been like… three hours…"
    "And she’s not here…"
    "Temptation almost gets the better of me as I contemplate whether to drop her another call..."
    "But that {i}would{/i} be me doubting her abilities of finding the likes of me in a \"crowd.\""
    "Or maybe it’s a little nice practice for hide and seek later?"
    "Then I spot her in the distance, panting and catching her breath just a few meters away from the bench."
    "Because I’m a smug jerk, I didn’t call her over conventionally. I gave her a phone call instead."
    "I dial."
    show sayonika 1x zorder 3 at t11
    sm "Hey… I made it… *pant* where… are…. you…?"
    "Did she really run all the way from her home just to meet me here? I’m amazed."
    "Right behind you, m’lady~"
    "As she turns around, I quickly pose in a gentlemanly manner."
    "And I dramatically drop the phone call like what those smug protagonists do in anime."
    sm "Right… I’m Sayonika… you must be—"
    mc "I’m the one who gave you a call earlier."
    $ sm_name = "Sayonika"
    sm "Ah! [player], right?"
    mc "Yes, that’s absolutely right."
    "Why am I acting like a British gentleman all of a sudden? Oh well, I should probably keep this guise for now, I guess." 
    "I mean, after all, I’m stuck here for about three or four months, so let’s make a good first impression to the cute girl."
    sm "Well… You do act and sound classy, I’ll give you that."
    sm "Anyways, you must be what your sister told me about!"
    mc "About what, hm?"
    sm "We’re gonna be roommates and classmates in summer class!"
    "If I was drinking tea and eating crumpets, I’d have spit everything out of my mouth already."
    "I was {i}not{/i} informed that I’d be tagging along to this girl’s summer classes!"
    "Hell… as her ROOMMATE as well? Ain’t fate a real jerk."
    "Nevertheless, if my whole summer’s gonna be spent with such a cute girl, I think that can all change."
    mc "It’ll be fun… I suppose..."
    sm "Aw… why so sad all of a sudden? Am I not that likeable?"
    "N-no…! it’s not that…!"
    "Oh boy… I’m pretty sure I just offended a girl… time to pray to Hirohiko Araki hoping I won’t butcher my words with the filth of a thousand dumpyards."
    mc "I’m just not used being with a girl, let alone a whole season..."
    "She pulls out a smirk and winks."
    sm "Ahaha~! Let’s make your summer more interesting, then!"
    mc "At least take me out to dinner first."
    sm "Alright, you look famished already per se, let’s go grab a bite!"
    mc"Are you paying…?"
    "She fidgets a little while looking away from me."
    sm "Ehehe…"
    mc "I’ll take that as a no."
    "I wonder how in the world she was able to get here without bringing any money at all. But I let that slip on my mind and let her lead me to a bakery. I’m just hoping she doesn’t mistake me for a walking wallet."
    return