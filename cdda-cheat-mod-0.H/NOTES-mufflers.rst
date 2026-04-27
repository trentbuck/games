| 12:51 <twb> Is the "loud enough to cause temporary deafness" level a fixed number?
| 12:51 <twb> In basic testing, a .223 with suppressor doesn't cause hearing loss, but a .308 with suppressor does, but only after a couple of sohts
| 12:52 <REDACTED> whats the message that you get when you go deaf again?
| 12:53 <twb> "Your ears ring!"
| 12:57 <REDACTED> sounds.cpp:573
| 12:58 <REDACTED> looks like about 150
| 12:58 [twb looks]
| 12:59 <twb> Seems reasonable
| 13:02 <REDACTED> as you can see if you wear hearing protection the value that is being compared with 150 is cut in half
| 13:05 <twb> So it looks like e.g. an MP5 is effectively hearing-safe already, in the game world
| 13:06 <twb> Picking that mainly because it has a pre-built MP5SD version
| 13:07 <REDACTED> i havent looked deeply into the logic but it looks like it stacks
| 13:07 <REDACTED> so i'd be careful, it might still hurt
| 13:07 <twb> As in like firing 10 rounds in 10 seconds is worse than 10 rounds in an hour?
| 13:08 <REDACTED> possibly but i have not tested that
| 13:08 <REDACTED> i saw that the deaf effect has different severities
| 13:09 <twb> The code looked to me more like you need a single loud noise to trigger deaf level 1 for <random duration to wear off> and then if you have another single loud noise it moves you to deaf level 2
| 13:10 <REDACTED> yes but i have been looking at a single function. i grepped for deaf in src/ - theres more.
| 13:10 <twb> If it is modelling uh... industrial hearing damage, like working in a server room or as a roadie, I don't think it is there
| 13:10 <twb> oh ok
| 13:10 <REDACTED> possibly, as i said i have not tested that so unsure
| 13:10 <REDACTED> i am 50/50 on that matter whether its implemented or not
| 13:16 <twb> OK as a test I set an MP5 w/ 100-rd mag on full auto and dumped it downrange without aiming, and my ears seem OK
| 13:16 [twb double-checks doesn't have earplugs in]
