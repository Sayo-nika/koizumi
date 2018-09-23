label ca2:
    scene bg plaza_day
    with wipeleft
    "After leaving the station, I sit down on a nearby bench before proceeding to call a number my sister handed to me before I left."
    "Apparently \"they’ll take me to where I need to go,\" she said."
    "I take a big sigh and call the number."
    mc "Hello?"
    $ sm_name = "???"
    sm "Hello? Who is this?"
    mc "Uhm... It’s me, [player]... my sister told me you knew each other... and{w=1.0}{nw}"
    $ _history_list[-1].what = "Uhm... It’s me, [player]... my sister told me you knew each other... and—"
    "She gasps and squeals in the phone."
    sm "Oooh wow!! You're already here?! Hold on, hold on!"
    mc "I’m just at the{w=0.5}{nw}"
    $ _history_list[-1].what = "I’m just at the—"
    "She drops the call, an unexpected event that seemed to fit quite well."
    "But perhaps my sister had told her my destination beforehand. I worry not and pull out my vintage phone, opening a visual novel game I dropped eons ago to continue it."
    scene bg plaza_day
    with dissolve_scene_full
    pause 3.0
    "I begin to understand the reason of why I dropped the visual novel."
    "But around three hours had passed since I called the lady."
    "I start feeling tempted to call her out of pity, but that would be doubting her abilities of finding the likes of me in a \"crowd.\""
    "Then I spot her in the distance, panting and catching her breath just a few meters away from the bench."
    "I walk up from behind her and give her a phone call."
    show sayonika 1x zorder 3 at t11
    sm "I made it...! W... *pant* ...where are you...?"
    "I take a moment to think about how she ran all the way to the train station with the face of astonishment. The first thought is, \"True dedication and determination?\""
    mc "Right behind you, ma'am~"
    "As she turns around, I quickly pose in a gentlemanly manner."
    "And I dramatically drop the phone call like a smug protagonists in an anime."
    $ sm_name = "Sayonika"
    sm 1o "Right... I’m Sayonika... you must be—{w=1.0}{nw}"
    mc "The one who gave you a call earlier."
    sm 2b "Ah! [player], right?"
    mc "Indeed."
    "I contemplate my decisions in turning into a classy gentleman, but I decide to continue with the guise." 
    "After all, first impressions are the best impressions, eh?"
    sm 1q "Well... you do act and sound classy, that's for sure!"
    sm 3b "Anyways, you must be what your sister told me about!"
    mc "About what, hum?"
    sm "We’re gonna be roommates and classmates in summer class!"
    "If I had been drinking a cup of tea and eating a packet of crumpets, I’d have spit everything out of my mouth in seconds."
    "I hadn't been informed that I’d be tagging along to this girl’s summer classes!"
    "And roommate? God can go suck a bible!"
    "Nevertheless, if my whole summer’s gonna be spent with such a cute girl, I think that can all change."
    mc "It’ll be fun... I suppose..."
    sm 1w "Aw... why so sad all of a sudden? Am I not that likeable?"
    "N-no...! it’s not that...!"
    "Oh boy... I’m pretty sure I just offended a girl... time to pray to Hirohiko Araki hoping I won’t butcher my words with the filth of a thousand dumpyards."
    mc "I’m just not used being with a girl, let alone a whole season..."
    "She pulls out a smirk and winks."
    sm 3a "Ahaha~! Let’s make your summer more interesting, then!"
    mc "At least take me out to dinner first."
    sm 1b "Alright, you look famished already per se, let’s go grab a bite!"
    mc"Are you paying...?"
    "She fidgets a little while looking away from me."
    sm 2i "Ehehe..."
    mc "I’ll take that as a no."
    "I wonder how in the world she was able to get here without bringing any money at all." 
    "But I let that slip on my mind and let her lead me to a bakery." 
    "I’m just hoping she doesn’t mistake me for a walking wallet."
    return
