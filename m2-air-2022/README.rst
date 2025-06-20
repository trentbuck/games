============================================================
 Impressions and support notes for Macbook Air M2 2022
============================================================


What I want & need
==================

Since about 2003 I wanted a "convergence desktop", i.e.
I carry around a (trusted & trustworthy) smartphone.
When working normally at a desk, it uses an external keyboard/monitor/mouse.

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
