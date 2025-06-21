============================================================
 Impressions and support notes for Macbook Air M2 2022
============================================================


What I want & need
==================

Since about 2003 I wanted a "convergence desktop", i.e.
I carry around a (trusted & trustworthy) smartphone.
When working normally at a desk, it uses an external keyboard/monitor/mouse (completely replacing a laptop/desktop).

Ideally *all* of these goals are met:

• runs Debian GNU/Linux painlessly without hacks
• ≤1kg weight
• ≤DIN A5 overall size (~10.1 US inches)
• ≥1d battery life (when running but idle)
• ≤500USD (in 2025 CE USD)

• Storage & compute power are irrelevant.

  Store things & compile things on communal servers.
  Communal server costs & resources are *shared between users* so overall cheaper.
  Communal server can be hotter, bigger, heavier, & louder than a laptop.

  This is the same reason why mass transit is fundamentally better private motorcars (for most jobs).

  • UPDATE 2021: I now need a full-feature GUI browser every day, sigh, so
    like ≥4GB RAM + ≥16GB NVRAM + ≥1080p + touchpad/touchscreen.

These were goals before ChromeOS was a thing — even before "the cloud" was a thing, so
I was advocating this by analogy with a 1970s-style minicomputer + serial terminals, or
1990s-style server + X terminals (or VNC thin clients).

Things I tried:

• Asus EeePC 701 & 901 & 1001 (the original netbook - "what if small+light, but for poors instead of Veblens?")
• Asus Transformer TF101 (tegra2 arm tablet + clamshell keyboard/battery dock) (**fuck Nvidia**)
• Acer C720 & C730 (ChromeOS replaces the netbook market)
• Thinkpad T490s (Amazon EC2 web UI was OOMing chrome on my chromebook, so I gave up and bought a "maximally normie" laptop)
• Pinephone (running pmOS + phosh
• iPhone SE 2022 (my dumb phone died one day, so I tried a "maximally normie" smartphone, and it mostly worked out)

Things I didn't try

• Purism Librem 5, ∵ too expensive
• arm64 pitop, ∵ **fuck Broadcom**
• arm64 thinkpad X13s, ∵ too expensive
• arm64 macbook air/pro, ∵ too expensive, and "what I can buy right now" vs "what Asahi supports right now" are 2-3y apart

  • I was thinking about this again recently and second-hand M2 Air on
    gumtree was ~600AUD and a new M4 Air was ~2000AUD.  I complained
    there wasn't a middle ground (old enough to work in Asahi, but
    passing Apple QA and not classified ads dicerolls).  e1f pointed
    out that apple has "refurbished" which was M2 Air for 1200AUD.

    Also *literally everyone* I talked to said "I have an arm macbook and I love it".
    It was almost "pod people"-level suspicious that they all said exactly "I love it".

    So I figured factoring in:

    • current mostly-complete Asahi support
    • everyone I trust says "I love it"
    • ≪2000AUD

    This seems a good time to try "can't you just be normal?" again.

My last "daily driver" macs were:

• Centris 610 (ca. 1993) running System 7.
• Mac Mini (ca. 2005) running OS X 10.2.
• When they switched from PowerPC to x86 I was like "fuck you, you're basically as bad as all the other hardware vendors now".


Initial Setup
=============

• Holy shit this metal case is cold!!
• Holy shit is this *heavier* than my T-series thinkpad, I thought airs were light? (1.08kg → 1.5kg)
  My 14" thinkpad is 1309g, the 13" M2 Air is 1224g.

• No LED case lights to indicate off/on/suspended or discharging/charging/charged.
  There's one on the "magsafe" power cable, but I was planning to exclusively use USBC.

• The usbc-to-magsafe cable is surprising long compared to all my other power/usbc cables, even the iphone one.

• On initial login, I *can't* say "my iphone is right there, get my account from that".  It only supports that from macOS and Windows (not iOS)!

• So I can't do *anything* until I connect by yubikey for 2FA, but the yubikey 5C is USB A or NFC, and this *doesn't* have an NFC reader (unlike the iphone)!  I didn't have a male C to *female* A cable, so I had to go get the pinephone's converge dock (which is just a generic USB C dock, really).

• When tabbing to UI elements, pressing button is SPC, not RET!
• By default tap-to-click is off.

• I've been using thinkpad laptop & (basically identical) wired & bluetooth keyboards for years, which all have identical dimensions & travel.  The different keyboard feels weird.  In particular there is less travel.

• No "show password" button while I type it into the "Sign In to Your Apple Account" UI, and my password doesn't fit onscreen either, so took me about 6 attempts to type it all correctly on the not-used-to-it keyboard.

• no prtscr button – how do you take a screenshot?  ⌘+option+3 didn't work, at least during the account creation UI...

• why is my default account thumbnail a golf ball instead of a generic placeholder?

• gee, tough to decide if I want to tick "[X] Allow my Apple Account to reset this password" for the machine-local password.
  Given the apple account is behind 2FA with hardware tokens and *no* "mother's first dog's maiden name" fallback, I *think* yes?

• *during* account creation on the macbook, the iphone popped up a warning saying something like "another device on your account doesn't use lockdown mode – that is suboptimal!" but clicking on the alert made it disappear without telling me any more!

  • UPDATE: **after** enrolling a credit card, it said "Lockdown Mode is enabled on another device associated with your Apple acconut.  Would you like to turn it on for this Mac? [Set Up Later] [Back] [Turn On & Restart]".

• location services on (FIXME: set it to be off for apps by default later?)
• analytics off
• FIXME: turn siri off
• "not now" / "set up later" for siri
• opt-out of "share audio recordings"
• leave enabled "Turn on FileVault disk encryption" and "Allow my Apple Account to unlock my disk" (see 2fa comment above)

  • NOTE: alternative is to create a "recvery key" and write it down somewhere safe – this is what I did for the iphone.

  • | 22:04 <twb> When setting up a new mac, re FileVault Disk Encryption, "Allow my Apple Acconut to unlock my disk" vs. "create a recovery key and store it in a safe place"
    | 22:04 <twb> Can I choose "Allow my account to unlock" now, but then opt-out later and switch to a recovery key?
    | 22:04 <twb> Last time, I opted-out up front, so I don't know

• FIXME: register additional fingers with fingerprint database, in case my index finger is amputated

• Interesting, VISA card has to be enrolled with "Apple Pay" separately per-device (rather than per-account).  Good!

• FIXME: two-finger scroll is "upside down" compared to linux

• FIXME: "privacy tape" for the camera, because there is not a built-in hardware barrier like on my old thinkpad

• During initial boot, the FDE requires typing a passphrase (can't use biometrics to unlock the FDE).

• Immediately apply OS security update before doing anything else

• After applying security updates, next reboot asked about iCloud *before* giving me a desktop again.
  It asked '[X] Store files from Documents and Desktop in iCloud Drive".
  I'm not sure I want **everything** in iCloud by default – definitely not before I turn on "encrypt everything so you can't decrypt it on your end", so I **unticked** that.

  • BUG: can't navigate to [Continue] button from keyboard in this dialogue box – have to use mouse.

• Oh wow, macos still puts files on the desktop by default?  Including screenshots?  Ewww.

  • FIXME: make screenshots (⌘+shift+3) save to something like ~/Photos/Screenshots/.

• Wade through every setting in the settings app

  • turn off Apple Intelligence (generative AI)
  • in Siri, set TTS voice to Indian English Voice 1 (default is Australian English Voice 2).

    This is used for TTS even though Siri will be off; on iOS we have to set this *before* turning Siri off, because it greys out the setting.

    • UPDATE: turning off Siri changed it back to "Australian (Voice 2)" :-(

  • turn off Siri

• FIXME: During initial account creation, it asked for a verification SMS to enroll my credit card into Apple Pay – but it never asked for the one-time key the SMS had sent me!  If I look in `Settings` it says the card has expired.  It says I can't change that in `Settings`, I have to go into `App Store`.

  • OK I *think* what happened was I had a card-not-present credit card enrolled the apple account from when I first got my iphone (in 2023), and *even though the phone* had enrolled a new credit card in *apple wallet*, only the old expired card was enrolled in the *apple account*.  And when setting up the new Air, it was trying to enroll that expired card-not-present card, *not* the current (valid) card.


• FIXME: what's the equivalent of iOS's Settings > iPhone Storage > FooApp > Offload App, to uninstall it (but not un-buy it)?  I clearly have Kiwix showing a cloud-and-down-arrow icon on macOS, so it must be possible to put other unwanted apps (like Garage Band and iMovie) into that state...

  • UPDATE: OK Settings > Storage > then **double click** on the `Applications` line, to get the option to remove apps.

  • Ew.  When macOS pops up a "password or fingerprint prompt" it doesn't acquire exclusive focus, so tapping the fingerprint scanner does nothing (because it sends fingerprint info the Settings window instead of to "enter your password" window)

• Turn on "Empty Bin automatically" (equivalent of Debian's ``OnCalendar=daily ExecStart=trash-empty 31``).

• Set the desktop background to be flat black (not a fucking movie!!!)

• FIXME: when opening image(s) in Preview, how do you move them to trash?  DEL key didn't work, nor did ⌘+DEL.  Right click on the thumbnail works, at least...

• | twb> Is there a default shortcut for <something> + <number> to launch/focus the <number>'th app in the dock?
  | twb> on windows and gnome it's ⌘+n
  | REDACTED> No.
  | twb> fair enough
  | REDACTED> You'd need a third-party Dock-alike (eg. Witch)
  | twb> yeah definitely not worth it
  | twb> like 90% of the time it's just between terminal and gui browser so ⌘+Tab is sufficient
  | REDACTED> macOS does not lend itself to full keyboard control.
  | twb> And yet weirdly the macbooks don't have touchscreens
  | REDACTED> Modern Apple is stupid Apple. It died when Steve did.


Browsing
====================

* FIXME: how do I make https://en.wikipedia.org/wiki/Special:Search/%s the default search engine?
  In other browsers, the modern advice is to just browse to wikipedia and then go to the address bar, and it'll offer to add the wikipedia as a search engine.
  It seems this doesn't exist on Safari?

  https://en.wikipedia.org/wiki/Help:Searching_from_a_web_browser

  That says "type 'wiki foo' to search wikipedia for foo", but that does not work for me as at 2025Q2.  They talk about Safari 8 which I think is very old?

  https://en.wikipedia.org/wiki/OpenSearch_(specification)#Support → "This will not affect the ability to manually add an OpenSearch engine from a website[9]"

  I found this but I do not fucking like having to hack this in AT ALL.  Also given the age, it probably predates "V3 Manifest" and "all safari extensions must be compiled into native macos apps" stuff.
  https://github.com/MentalGear/OpenSearchSafari

* FIXME: fuck me, there are ads.  Like... at all.

  Hrm, so on macOS, Safari does not support any of: Privacy Badger, uBlock Origin, Firefox Focus -- the last one is what works on iOS outside of Europe.
  And firefox-esr isn't in the first-party app store -- the one that security updates apply automatically from.

  | 00:54 <twb> also ew, safari isn't blocking ads by default
  | 00:54 <REDACTED1> Never has.
  | 00:55 <twb> yeah I forgot I had to do something to make ads blocked on iOS too
  | 00:56 <REDACTED1> twb: Use another browser & add your choice of blocker, or use AdGuard if you want to keep using Safari.
  | 00:56 <twb> right
  | 00:56 <REDACTED1> AdGuard is a 'network filter' that plugs in at the OS level (an adjunct to the network stack).
  | 00:57 <REDACTED2> Or pihole that works on the network level and blocks ads in all your devices.
  | 00:57 <REDACTED1> I use Orion (the *other* WebKit browser) these days. Very good blocking.
  | 07:28 <twb> Weird.  I was looking at AdGuard which was mentioned earlier -- its homepage says "free and open source", but doesn't link to a git repo anywhere AFAICT
  | 07:30 <twb> Just guessing it was github worked
  | 07:30 <REDACTED2> Only some products from Adguard are open source...
  | 07:31 <twb> Well, that one said "free and open source" and didn't link to the source
  | 07:32 <REDACTED2> https://adguard.com/en/blog/adguard-open-source-policy.html
  | 07:32 <REDACTED2> https://adguard.com/en/adguard-browser-extension/overview.html
  | 07:32 <twb> It looks like safari already has basically the equivalent of chromium's "v3 manifest to kill ad blockers" thing
  | 07:32 <REDACTED2> It does link them here..
  | 07:32 <twb> REDACTED2: thanks
  | 07:33 <twb> I somehow ended up on uh... https://adguard.com/en/adguard-safari/overview.html
  | 07:34 <twb> Does macOS have an equivalent of /etc/hosts, so you can just dump a bunch of deliberately-wrong DNS resolution in there?
  | 07:34 <twb> Looks like yes
  | 07:35 <twb> Although possibly HTTP clients bypass it and do DOT by now
  | 07:36 <REDACTED2> The v3 manifest "killing" ad blockers is a years old exageration, reality is most casual users won't notice any diff...
  | 07:36 <REDACTED2> https://old.reddit.com/r/uBlockOrigin/comments/1j37112/ublock_origin_lite_is_like_95_percent_as_good_as/

  :EFF Privacy Badger: https://github.com/EFForg/privacybadger/issues/549#issuecomment-2945008056 → we are blocked by Safari bugs
  :Firefox Focus: https://support.mozilla.org/en-US/questions/1279485 → Firefox Focus is iOS/Android-only
  :uBlock Origin: https://github.com/uBlockOrigin/uBlock-issues/issues/1123#issuecomment-926733561 → necessary WebExtensions APIs aren't supported (as at 2021)
  :uBlock Origin Lite: https://github.com/uBlockOrigin/uBOL-home/issues/52 → https://github.com/uBlockOrigin/uBOL-home#ubo-lite → https://testflight.apple.com/join/JjTcThrV → looks like this is in open beta!

  See also citation from Wikipedia https://www.zdnet.com/article/apple-neutered-ad-blockers-in-safari-but-unlike-chrome-users-didnt-say-a-thing/

  See also how Apple *wants* you to create Safari ad blockers as native macOS apps: https://developer.apple.com/documentation/SafariServices/creating-a-content-blocker

  See also how UBOL is different from UBO: https://github.com/uBlockOrigin/uBOL-home/wiki/Frequently-asked-questions-(FAQ)#filtering-capabilities-which-cant-be-ported-to-mv3


Doing My Actual Job
====================

* Debian is in the Microsoft Store, but not in the Apple App Store :-/
* Also missing:
  * alpinelinux
  * firefox esr
  * emacs
  * libvirt / virt-manager / virt-viewer

* FIXME: are there options that are less completely shit than homebrew yet?  What are they?


ZFS & backups
====================
https://arstechnica.com/gadgets/2016/06/a-zfs-developers-analysis-of-the-good-and-bad-in-apples-new-apfs-file-system/

The ZFS guy complained that they hadn't implemented transparent compression, even though it's fucking easy to do.

Later I found https://en.wikipedia.org/wiki/Apple_File_System#Compression and went "oh OK I guess it was implemented since I last checked" – but #macos says this is not the case.
