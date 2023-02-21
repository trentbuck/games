"Final" Loadout for Perfect Cheating Start
======================================================================
The goal is to have a character that can run around seeing everything "worry free", to learn the details of the game.
Not doing `debug backpack <https://nornagon.github.io/cdda-guide/#/search/debug>`_, tho.
Vehicles & bionics & mutations are ignored for now.
Initial focus is on getting a handle on armour, storage, and summer/winterweight layering.

• **FAVOURITE** your great gear, and turn on autonotes, so if you accidentally drop it, you can fucking find it again.

:Melee: RM42_ w/ Eskrima_ or `Krav Maga`_.

   Always want a knife regardless, for cutting_ and butchering_.
   Fits in `survivor belt`_ knife holster (20mov).
   Better dam/turn & dam/stamina than `survivor machete`_ w/ Barbarian_ (though lose strong Armor Piercing buff).

:Ranged (long): RM11B_ w/ Taekwondo_, 3-6 × 8x40mm_ 25rd mag, [match trigger, ergonomic grip, high end hand guard, gyro (or laser?)].

   Roleplaying: I like DMRs.  5x50mm_ only has pistol & smg; `laser <Laser vs. Rivtech caseless>`_ ammo is too heavy.

   Fits in `survivor harness`_ gun holster (30mov); par with `single_sling`, 4×faster than `shoulder_strap` sling gunmod.

   8x40mm_ isn't *best* at anything, but it's *good* at most things (poor availability, but we're cheating).
   The thing they're worst at is noise, and this gets it from ~200 to ~100.  Hearing damage is >150noise.  This is the main reason not to RM88.
   Only this and MP5SD_ have integrated suppressors.  All other suppressors *wear out*.  Other 8x40 can't be suppressed.

   See also `ammo comparisons`_.

   Base 10disp, repair (accurize) is -30disp, but cannot go below 0.
   So you end up with 0disp (from gun) and 75disp (from ammo).
   Therefore no point getting gun mods that improve dispersion, only recoil and aim speed.

   Carry 3–6×25rd mags (2L 1.6kg) and 1000rd loose (6L 12kg).

:Ranged (short): MP5SD_. 100rd mag.

   One of the 2 most common calibres, so just "top up" this up from corpses.
   Starts at 48noise.  You can add a *second* suppressor for 0noise.
   Range is shit, but this is intended for bumbling around in CQB without waking people, for when I get bored of knife fighting.
   Don't bother to trick this out with other mods.

   **PROBLEM!**

   This gun is
   4L/3.65kg/67cm factory-stock, or
   4.55L/5.2kg/82cm with a second suppressor and a 100rd mag.

   That does not fit into the survivor backpack, and
   I'm already using the survivor_harness_'s rifle sling for the RM11B, and
   I'm already using the survivor_belt_'s pistol holster for the RM42.

   So I don't actually have anywhere to put the gun, and I can't add a
   rifle sling or similar, because strapped-torso-front and
   strapped-torso-back are both already in use.

   On the survivor_backpack_,
   I can put up to 5L/6kg/120cm on a krab, paying a *noise & encumbrance penalty*.
   It doesn't fit *inside* the pack which is capped at 50cm.

   When I switch to knife fighting, if my backpack is full, I am *ALREADY* dropping it to avoid encumber-ment, even with maxed stats.
   Should I therefore go "fuck it" and just get a survivor_duffel_ instead?  UPDATE: that still only gets me 60cm

   Or should I switch to a takedown carbine (Kel-Tec Sub2000) or pistol?  Those aren't integrally suppressed, but I can add a can to get them from 100 to 50, instead of 50 to 0.
   Just walking around is doing 2-9 noise and smashing a wall is 20-50 noise, so I guess that's my threshold?

   Noise is purely from the cartridge, which in the stock 9mm JHP is about 100.
   A suppressor is +15cm -50noise.
   To fit in a backpack/rucksack/duffel we need to get below 50/55/60cm overall length.
   We COULD just take off the suppressor every time we want to do stuff other than shoot motherfuckers...
   Otherwise we need the length pre-suppressor to be 35/40/45cm.

   .. csv-table::
      :Header: Variant, Range, Len (unsupp), Noise (unsupp)

      Kel-Tec_SUB-2000 (folded),   32, 19, 80
      Hi-Point C-9,                14, 20, 80
      Walther_CCP,                 14, 20, 80
      Walther_PPQ_9mm,             14, 21, 80
      Glock_19,                    14, 22, 80
      Hi-Power_9mm,                14, 23, 80
      CZ_75_B,                     14, 24, 80
      Glock_17,                    14, 24, 80
      Glock_18C,                   14, 24, 88
      Luger_P08,                   14, 25, 80
      Walther_P38,                 14, 25, 80
      Mauser_C96,                  14, 32, 80
      BT_APC9K (folded),           14, 33, 80
      TEC-9,                       14, 35, 80
      MP5K,                        14, 38, 80
      Luty SMG 9x19,               14, 54, 105
      Calico,                      14, 66, 80
      MP5SD,                       13, 67, 48
      MP5A2,                       14, 69, 80
      Kel-Tec_SUB-2000 (unfolded), 32, 74, 80
      Beretta CX4,                 34, 77, 80
      Mauser_M7                    14, 32, 80
      MP18,                        14, 84, 80

   The Luty is burst-only (no semi-auto), so I guess 105 there makes sense.
   How the hell is the Glock 18C 88 noise in *both* auto and semi-auto?
   I cannot see where this is coded...

   A Kel-Tec Sub2000 is 20cm/74cm folded/unfolded & 80noise.
   A Kel-Tec Sub2000 is 34cm/89cm folded/unfolded & 30noise with a suppressor.
   A Kel-Tec Sub2000 is 13cm/68cm folded/unfolded & 82noise with a sawn-off barrel (-5 length)!
   A Kel-Tec Sub2000 is 27cm/83cm folded/unfolded & 32noise with a sawn-off barrel and a suppressor.
   Even folded, once accurized the dispersion is only 5.
   Unfolding drops recoil from 98 to 30 (UPDATE: can't fire folded at all – makes sense).

   The first play I did after setting up the MP5SD, I ran into about 50 zombies NONE of which were cops/soldiers, and
   then a bunch of razorclaws which mostly ignore the 9mm ammo.
   And until I learn zombie anatomy, it's taking 3 shots to down starting zombies.
   So maybe just say "fuck it" entirely to this idea and use knife fighting for everything except the real badasses?


:Miscellaneous:
   | smartphone_ in waterproof_case_ — calorie intake tracking, alarm clock (wake up at X), exact time
   | survivor_light_ (350cd/m²)

   | Some plastic bags (non-rigid containers up to 10L); use knife to label them "DRUGS" and "SEEDZ", then set their priority to 1 (or more) and category whitelitst.  Now you can collapse the individual boring lists easily, without wasting too much space.
   | Probably want some non-rigid liquid containers as well for water and suchlike...

:Tool Qualities (important):
   | survivor_mess_kit_    ⇒ `food cooking`_ [3] boiling_ [2] `chemical making`_ [1] containing_ [1]
   | tailors_kit_          ⇒ `curved needle`_ [1] `fabric cutting`_ [1] sewing_ [4] knitting_ [1]
   | firearm_repair_kit_   ⇒ hammering_ [3] `fine hammering`_ [1] `soft hammering`_ [1] `bolt turning`_ [1] `fine bolt turning`_  [1] `screw driving`_ [1] `fine screw driving`_ [1] `nail prying`_ [1] chiseling_ [3] `wood chiseling`_ [3]
   | `metal sawing`_       ⇐ [2] firearm_repair_kit_ — or [10] angle_grinder_
   | `fine metal sawing`_  ⇐ [1] firearm_repair_kit_ — or [2] tin_snips_
   | metal_fileset_        ⇒ filing_ [2] grinding_ [2]
   | cutting_              ⇐ [2] RM42_
   | `fine cutting`_       ⇐ [3] scalpel_ — used for `dissecting corpses to learn weaknesses <https://www.reddit.com/r/cataclysmdda/comments/u7uner/dissection_and_finding_vulnerabilities/>`_ ([4] `bionic scalpel`_)
   | `glare protection`_   ⇐ [1] welding_goggles_ — used for welding; also on survivor_firemask but *not* survivor_goggles.
   | welding_              ⇐ [2] welder_  — welding *kit* appears only interesting for vehicles
   | `wood sawing`_        ⇐ [2] bow_saw_  — skip misc_repair_kit; tailors_kit_ already handles everything else misc_repair_kit can do
   | `tree cutting`_       ⇐ [2] bow_saw_  — skip fire_axe_ & chainsaw, they're too heavy for +1/+2 points
   | digging_              ⇐ [3] entrenching_tool_ — handy for clearing rubble instead of wobbling over it?
   | lockpicking_          ⇐ [3] locksmith_kit_ ([10] bio_lockpick_)
   | clamping_             ⇐ [1] pliers_locking_
   | rope_ [1] long_rope_ [1] grappling_hook_

:Tool Qualities (meh):
   | `grass cutting`_      ⇐ [1] `survivor machete`_ [2] sickle_
   | shearing_             ⇐ [1] shears_  [3] elec_shears_
   | churn_                ⇐ [1] churn_
   | anesthesia_           ⇐ [1] anesthetic_kit_
   | fishing_              ⇐ [2] fishing_rod_professional_
   | `fish trapping`_      ⇐ [1] fish_trap_basket_
   | smoothing_            ⇐ [2] metal_smoother_          — for construction?
   | `self jacking`_                                      — a vehicle thing
   | smoking_                                             — drugs only
   | distilling_           ⇐ [2] still_ [1] chemistry_set_
   | `fine distillation`_  ⇐ [1] still_lab_
   | butchering_           ⇐ [37] butchering_kit_ [19] RM42_
   | drilling_             ⇐ [3] cordless_drill_ [2] hand_drill_
   | `rock drilling`_                                     — not interesting?
   | reaming_              ⇐ [1] pin_reamer_              — nothing uses this anymore?
   | prying_               ⇐ [3] crowbar_                 — skip halligan_bar_ as too bulky for +1 point
   | punch_                ⇐ [2] nail_punch_              — only for making buttons…
   | pencil_                                              — not used anymore?
   | lifting_                                             — vehicle stuff
   | jacking_                                             — vehicle stuff
   | siphoning_            ⇐ [1] hose_
   | `bullet pulling`_     ⇐ [2] puller_                  — for reloading bullets?  not interesting?
   | anvil_                ⇐ [3] anvil_                   — bronze_anvil_is portable (anvil isn't), but can only make bronze recipes
   | analysis_                                            — mutation stuff
   | concentration_                                       — mutation stuff
   | separation_                                          — mutation stuff
   | chromatography_                                      — obsolete?
   | `fine grinding`_      ⇐ [2] mortar_pestle_
   | pressurizing_                                        — vehicle stuff
   | extraction_                                          — kerosene (vehicle stuff) and drugs only
   | filtration_                                          — drugs only
   | suspending_                                          — rope does this automatically when butchering
   | `clean surface`_ [3] plastic_sheet_
   | `wheel fastening`_                                   — vehicle stuff
   | `oven cooking`_ [1] improvised_oven_ [2] dutch_oven_ — only need level 1 for most things - much lighter
   | `glass cutting`_                                     — only for making aquariums
   | gun_ rifle_ shotgun_ smg_ pistol_                    — only used for training pseudo-recipes



To skip all the starting bullshit
------------------------------------------------------------

1. `Create World` & `Create Custom Character`  (if you haven't already)
   Naked might be best, otherwise it'll add stating gear on top of your custom gear...

2. Find/make/cheat yourself the gear you want — make sure it is all on your person!
3. At main menu, `World > Foo > Character to template > Bar`:kbd:.
4. At main menu, `New Game > Preset Character > Bar`:kbd:.




Brainstorming
======================================================================

* WEAPONRY

  * MELEE

    | RM42_                             0.75L 0.19kg 30cm 4/22 bash/pierce -1hit  80mov  525DPSec 833DPStam  block rapidstrike KRAVMAGA/ESKRIMA/ninjutsu/silat 19butch/2cut/1finecut  survivor_belt
    | `survivor machete`_        1.00L 0.57kg 50cm 6/28 bash/cut    +1hit  90mov  431DPSec 469DPStam  parry rapidstrike BARBAR/ESKRIMA/ninjutsu/silat/mideval/niten/...  14butch/2cut/1grasscut  survivor_harness

    * melee - japanese swords

      | https://nornagon.github.io/cdda-guide/#/item/crowbar                  0.10L 0.55kg  45cm   75move +15/1bash/cut                      block
      | https://nornagon.github.io/cdda-guide/#/item/halligan                 0.55L 4.77kg  76cm  152move +42bash                block brutalstrike sweepattack
      | https://nornagon.github.io/cdda-guide/#/item/PR24-extended         8$ 1.00L 0.68kg  20cm  108move +14bash +3hit rapidstrike parry precisestrike
      | https://nornagon.github.io/cdda-guide/#/item/tonfa                 8$ 2.00L 0.56kg  50cm  106move +14bash          +2hit rapidstrike parry precisestrike
      | https://nornagon.github.io/cdda-guide/#/item/knife_combat         13$ 0.50L 0.56kg  30cm   82move +4/26bash/pierce -1hit rapidstrike
      | https://nornagon.github.io/cdda-guide/#/item/tanto                15$ 0.50L 0.56kg  35cm   82move +2/21bash/pierce       rapidstrike
      | https://nornagon.github.io/cdda-guide/#/item/qt_wakizashi         28$ 1.50L 0.90kg  70cm  104move +2/36bash/cut    +1hit rapidstrike parry
      | https://nornagon.github.io/cdda-guide/#/item/knife_rm42           40$ 0.75L 0.19kg  30cm   80move +4/22bash/pierce -1hit rapidstrike block                            <-- BEST DPSecond AND BEST DPStam ?
      | https://nornagon.github.io/cdda-guide/#/item/qt_katana            45$ 2.00L 1.29kg  90cm  118move +5/37bash/cut    +2hit rapidstrike parry
      | https://nornagon.github.io/cdda-guide/#/item/survivor_machete_qt  45$ 1.00L 0.57kg  50cm   90move +6/28bash/cut    +1hit rapidstrike parry
      | https://nornagon.github.io/cdda-guide/#/item/qt_nodachi          120$ 3.35L 2.95kg 120cm  166move +6/53bash/cut    +2hit rapidstrike block widestrike brutalstrike

  * "Accurizing" a firearm is a flat -30disp.
    For the RM11B, the default is 10disp so accurizing only does -10disp there.


  * Most expensive ammo by far is 8mm_hvp (8x40mm HVP).
    5 bullet-type damage, 20 penetration

    * "8x40mm caseless" - 12g 230mL $80  42dam (bullet) 18penetration 75dispersion 2200recoil
    * "8x40mm sporting" - 12g 230mL $64  24dam (bullet) 18penetration 90dispersion 1100recoil
    * "8x40mm FMJ"      - 12g 230mL $80  37dam (bullet) 28penetration 75dispersion 2200recoil
    * "8x40mm HVP"      - 12g 230mL $500 47dam (bullet) 38penetration 75dispersion 2200recoil
    * "8x40mm tracer"   - 12g 230mL $80  42dam (bullet) 18penetration 38dispersion 2200recoil
    * "8x40mm JHP"      - 12g 230mL $80  47dam (bullet)  8penetration 75dispersion 2200recoil


.. _RM298_HMG: https://nornagon.github.io/cdda-guide/#/item/rm298
.. _RM614_LMG: https://nornagon.github.io/cdda-guide/#/item/rm614_lmg
.. _RM88:   https://nornagon.github.io/cdda-guide/#/item/rm88_battle_rifle
.. _RM51:   https://nornagon.github.io/cdda-guide/#/item/rm51_assault_rifle
.. _RM11B:  https://nornagon.github.io/cdda-guide/#/item/rm11b_sniper_rifle
.. _RM2000: https://nornagon.github.io/cdda-guide/#/item/rm2000_smg
.. _RM103A:  https://nornagon.github.io/cdda-guide/#/item/rm103a_pistol

  * 5x50 -- not caseless -- only comes in 50 and 100 mags, and only has two guns

    | https://nornagon.github.io/cdda-guide/#/item/needlegun    SMG $80 1.25L 1.30kg 690mm 50/100mag 220disp 30sight 9dur +10dam
    | https://nornagon.github.io/cdda-guide/#/item/needlepistol HG  $80 0.62L 0.68kg 255mm 50/100mag 280disp 30sight 9dur

    | https://nornagon.github.io/cdda-guide/#/item/rm228 -- PDW shotgun, light

  * EXPENSIVENESS:

      * "RM88 battle rifle" - most expensive rifle -- other caseless are a close follow-p
      * https://nornagon.github.io/cdda-guide/#/item/hm12
        HM12 is second-most-expensive.  It doesn't do meaningful damage tho?

      * https://nornagon.github.io/cdda-guide/#/item/hk_mp5sd  3.50L 3.23kg 666mm 10/15/20/30/38/40/50/100mag 240disp 30sight 8dur +1dam
        Third-most-expensive gun is MP5SD!?

      * https://nornagon.github.io/cdda-guide/#/item/m107a1  120$  7.57L 12.95kg 145cm 10mag 130disp 30sight 8dur -5dam +100rng
        https://nornagon.github.io/cdda-guide/#/item/tac50   120$
        https://nornagon.github.io/cdda-guide/#/item/as50    120$
        50 BMG fourth most expensive

      * https://nornagon.github.io/cdda-guide/#/item/hk_g80  120$  4.96L 3.91kg 20mag 45disp 30sight 8dur +60rng UPS

  * "20x66mm buckshot"  — caseless shotgun

  * Early game, just spam 9mm or 5.56x45 NATO?

    The ONLY guns with integrated (lasts forever) suppressors are the MP5SD and the RM11B.

    You can add *ANOTHER* suppressor on the end of the MP5SD to make it doubly-suppressed, resulting in 0 noise.
    Without that, it's 50 noise.

    It can take up to 100rd mags. ::

        Marlin 39A (stock)  FIXME
        Marlin 39A (maxed)  FIXME
        MP5SD      (stock)  FIXME
        MP5SD      (maxed)  FIXME
        AUG        (stock)  FIXME
        AUG        (maxed)  FIXME
        RM88       (stock)  FIXME
        RM88       (maxed)  FIXME
        RM11B      (stock)  FIXME
        RM11B      (maxed)  FIXME

    Non-integrated suppressor is a flat -50noise.
    So not really useful for 5.56???
    They're *all* 166noise (for regular M855).
    Different guns aren't different noisy.

    Of all the 5.56 rifles, the Steyr AUG is probably the least awful.
    The FS2000 can only take 30rd mags.
    The X-95 is only availble in 300BLK.

    Of all the 7.62x54 rifles, the interesting ones are::

        M24        ( 5rd 4.0L 5.0kg 100cm  85disp)
        M14 EBR-RI (20rd 3.7L 5.0kg  90cm 110disp -1dam)
        M110A1     (20rd 4.0L 3.8kg 103cm 120disp -dam)

    So fuck that just skip straight to the 8x40 caseless.

  * The Marlin 39A can also be 0 noise.

* power armor

  * "ICE utility exoskeleton"             - 110kg 130L $400 20encum 10000gas
  * "battery powered utility exoskeleton" - 110kg 130L $400 20encum medium_storage_battery
  * "field combat exoskeleton"            -  13kg  25L $400 40encum ups
  * "heavy combat exoskeleton"            -  75kg 130L $400 60encum ups

  Only difference between field (light) and heavy is the material thickness???

  * "RM13 combat armor"                   -    5000battery
    needs a "nanofab" to repair?


* optical cloak  - most expensive cloak - invisibility when powered on


* always want "STURDY" and avoid NO_REPAIR, FRAGILE, SLOWS_MOVEMENT
  ALLOWS_NATURAL_ATTACKS probably


    So you will find lots of:

    • negligible encumbrance (< 2) clothing with almost no protection and 90% to 100% coverage
    • low encumbrance (< 5) clothing made of soft materials with just okay protection and 90% to 100% coverage
    • low - medium (< 10) encumbrance modern armor with good protection and low 80% coverage
    • high (> 15) encumbrance traditional armor with good protection and high 95%+ coverage

* BIONICS


  * Most expensive bionic:

    | "Time Dilation CBM"  150$
    | "Active Defense System CBM" 150$
    | "Uncanny Dodge CBM" 150$



* most expensive armor - armor_lc_heavy_chestplate
* most expensive melee - "qt_nodachi"


* martial arts

  | https://nornagon.github.io/cdda-guide/#/martial_art/style_barbaran   - great bonus AP, COMBAT MACHETE   <--- I LIKE THIS
  | https://nornagon.github.io/cdda-guide/#/martial_art/style_eskrima    - flat speed bonus, flat damage bonus, CLAWS, KNIVES, BATONS  <-- I LIKE THIS
  | https://nornagon.github.io/cdda-guide/#/martial_art/style_krav_maga  - bone breaker (str) (but not always firing), KNIVES, BATONS, RM88/RM51 (but NOT RM11B)  <-- I LIKE THIS
  | https://nornagon.github.io/cdda-guide/#/martial_art/style_muay_thai  - str bonuses, unarmed only
  | https://nornagon.github.io/cdda-guide/#/martial_art/style_leopard    - crit chance bonus (dex)
  | https://nornagon.github.io/cdda-guide/#/martial_art/style_ninjutsu   - great but situational - mostly useless in daytime
  | https://nornagon.github.io/cdda-guide/#/martial_art/style_zui_quan


* gunmods:

  :barrel: barrel_ported: overall worse - meh
  :barrel: barrel_small: +75 dispersion +2noise --- CANNOT SPAWN THIS, USE TOOL TO saw_barrel ACTION.  (There is also saw_stock!)
  :grip: light_grip 25% weight reduction, -2 handling, REDUCED_BASHING
  :grip: pistol_grip +2 handling
  :mechanism: match_trigger -1 dispersion
  :mechanism: waterproof (not needed for 8x40mm caseless)
  :brass_catcher: (not needed for 8x40mm caseless)
  :muzzle: muzzle_break: +15disp +14noise +4handling
  :muzzle: suppressor: +2 handling -50noise, CONSUMABLE
  :#rail: offset_sights: +25% sight_dispersion
  :rail: rail_laser_sight: 30sight 3000fov +15aimspeed
  :rail: stabilizer: -1disp +6handling

  :sling: shoulder_strap:        10$ 100g 250ml "adjust - torso_hanging_back" <-- GOOD? --- easier to just have a `survivor harness`_

  :stock: adjustable_stock: -1disp +1handling
  :stock: recoil_stock: +4handling
  :stock accessory: cheek_pad: -1disp +2handling
  :stock accessory: butt_hook +100g +100ml +4cm -15disp <-- not worth it?

  SHIT STOCKS THAT NEED BABYSITTING:

  :stock: high_end_folding_stock: -1disp +5handling (when unfolded), ??? (when folded)
  :stock: wire_stock: +2handling (when unfolded), ...
  :stocK: under_folding_stock: +8handling (when unfolded) ...
  :stock: stock_none: -10handling --- length???

  :underbarrel: bipod: +18handling BIPOD SLOW_WIELD
  :underbarrel: bipod_handguard: (foldable bipod)  +4handling (folded)   +18handling BIPOD SLOW_WIELD (unfolded)
  :underbarrel: modern_handguard: +6handling -6disp, -5%weight
  :#underbarrel: grip: 68g 119ml +6handling <-- WORSE
  :#underbarrel: inter_bayonet: 1g 92ml +22cm +10cut (melee) (unfolded); 1g 92ml (unfolded)  --- FOR SKS/Mosin only
  :underbarrel: laser_sight: 70g +15aimspeed 3000fov
  :underbarrel: theres a rivtech RM121 caseless shotgun, but MEH

  :sights: improve_sights (iron):                  30sight 360fov
  :sights: red_dot_sight:               150g 80ml  27sight 630fov +10aimspeed
  :sights: holo_sight:                  255g 290ml 23sight 720fov +10aimspeed
  :sights: acog_scope:                  280g 112ml  8sight 270fov             ZOOM
  :sights: hybrid_sight_4x:             280g 112ml  8sight 270fov             ZOOM (ACOG + spot for backup optic on top)
  :sights: holo_magnified:              320g 390ml 13sight 270fov  +5aimspeed ZOOM
  :sights: rifle_scope:                 669g 485ml  0sight 270fov  -1aimspeed ZOOM
  :sights: rifle_scope_high_end_mount:  700g 485ml  0sight 270fov  -1aimspeed ZOOM (spot for backup optic on top)

  :???: grip_mount, rail_mount, sights_mount, stock_mount --- this is for shit old guns

  :laser stuff: not considered





* armor:

  torso_armor: ignore for now
  legs_armor:  ignore for now
  arms_armor:  ignore for now




* HOLSTERS:

  | survivor_duffel_bag:       2 × tool_loop          4L 6kg 40-100cm  300mov +1encum
  | survivor_duffel_bag:           under_handles      4L 6kg 40-100cm 80mov +5encum
  | survivor_pack:                 waterbottle        0.5L 1kg 7-12cm 80mov  --- what kind of bottle?
  | survivor_pack:                 tool_loop          4L 6kg 40-100cm 300mov +1encum
  | survivor_pack:             2 × krab               5L 6kg 20-120cm 150mov +3encum
  | survivor_rucksack:
  |
  | canteen_pouch:                                    1.75L  1.8kg 13cm   40mov  20%encum      PALS_SMALL --- canteen
  | flashlight_pouch:                                 0.50L  0.5kg 37cm   40mov  30%encum      PALS_SMALL --- flashlight/heavy_flashlight
  | gas_mask_pouch:                    (1)            1.25L  2.0kg 30cm   80mov  30%encum      PALS_MEDIUM
  | gas_mask_pouch:                    (2)            0.25L  0.5kg  8cm   80mov  30%encum
  |
  | tacvest:                                          0.3-1L 2.0kg  30cm  50mov
  | tactical_holster:                                 0.3-1L 2.0kg  30cm  70mov                PALS_SMALL
  | load_bearing_vest_sling:           "rifle sling"  1.0-8L 8.2kg 120cm  30mov 160%encum
  | heavy_load_bearing_vest_sling:     "rifle sling"  1.0-8L 8.2kg 120cm  30mov 200%encum
  | heavy_load_bearing_vest_breacher:  "rifle sling"  1.0-8L 8.2kg 120cm  30mov 200%encum
  | heavy_load_bearing_vest_breacher:  "SG magnets"   1.0-4L 8.2kg  60cm  60mov 200%encum
  | ballistic_vest_light_operator:     "glowstick"    meh
  |
  | fireman_belt:                      BELT_CLIP          2L 6.0kg  90cm  50mov
  | leather_belt:                      BELT_CLIP          1L 0.8kg  70cm  60mov
  | police_belt:                       BELT_CLIP        2.3L 3.6kg  70cm  50mov
  | santa_belt:                        BELT_CLIP        1.2L 0.8kg  90cm  60mov
  | tool_belt:                      6× BELT_CLIP/KNIFE  1.5L 1.5kg  70cm  50mov
  | webbing_belt:                      BELT_CLIP        1.5L 1.0kg  70cm  60mov
  | suspender_holster:                                0.3-1L 2.0kg  30cm  50mov
  |
  | [... I GOT BORED OF THIS...]



* STATIC STORAGE::

    Type                 Volume  BlocksMove?  BlocksLOS?  EasyCraft?
    Dresser              2000L   Y            N           Y
    Bookcase             2000L   Y            Y           Y
    EntertainmentCenter  2000L   Y            Y
    Clothing_Rail        1750L   Y            N
    Display_Rack         1750L   Y            N
    Wooden_Rack          1500L   Y            N
    Utility_Shelf        1500L   Y            N
    Warehouse_Shelf      3500L   Y            Y


Survivor Gear
------------------------------------------------------------
General opinion seems to be that

• `power armor <https://nornagon.github.io/cdda-guide/#/item/power_armor_light>`_ (et al)
  `phase immersion suit <https://nornagon.github.io/cdda-guide/#/item/phase_immersion_suit>`_
  `RM13 combat armor <https://nornagon.github.io/cdda-guide/#/item/rm13_armor>`_
  are all good but have caveats/finnicky.

• The `bespoke_armor <https://github.com/CleverRaven/Cataclysm-DDA/tree/master/data/json/items/armor/bespoke_armor>`_ tree is pretty good, but
  `nomad <https://nornagon.github.io/cdda-guide/#/search/nomad>`_ is objectively worse then
  `survivor <https://nornagon.github.io/cdda-guide/#/search/survivor>`_.
  The nomad stuff also hooks into bionics, and I'm not touching bionics yet.

So let's initially start with the assumption that *all* clothing/armor should be pulled from the `survivor` part of ``bespoke_armor``.

• Light/medium/heavy is the usual dodge/block tradeoff.
  I'm less confident about the winter, flame, and wetsuit variants.
  Can we instead get away with just summerweight + some thermal undies?

  Ignore "faux-fur" as being just a crap version of fur (winter)?

• "Survivor Suit" is obsolete.
  Modular ballistic vest (MBR) is obsolete.
  Some of the new names *do not* have "survivor" in their search title!

• https://www.reddit.com/r/cataclysmdda/comments/pct2p7/looking_for_armor_guide/:

    | Survivor armor is constantly recommended ∵ few other armors combine 100% coverage & decent protection values.
    | "95% coverage" means 1 in 20 hits completely bypass your armor.
    | Roughly 12 bash + 12 cut at 100% coverage → totally immune to vast majority of attacks until late game.

    | SWAT armor (relatively easy to get) invalidates everything except heavy survivor
    | Elbow & Knee pads are cool, as they have an encumbrance value of 0%.
    | Early game, leather touring suits and leather chaps are great.
    | Arms is generally a pain early game.  Invest in good arm protection as soon as you can craft it (or find SWAT armour).

    | Early game (Day 1):-
    |   Leather jacket
    |   Leather trousers
    |   Boots
    |   Leather gloves
    |   Safety Glasses
    |   Motorcycle/Riot hemet
    |   Backpack (Or two makeshift slings if need be.)
    | Alternativley if I find a Soldier Corpse spawn
    |   ESAPI vest (Deconstruct the damaged ones, rebuild a pristine one)
    |   Kevlar helmet
    |   Kneepads / Elbow Pads
    | Midgame (Should have a base location set up near a city for raiding and wood / water. I start the process towards survivor gear here. Day 3+)
    |   SWAT armour if I run across it (Likely damaged from a Z, needs cleaning and good tailoring and materials to repair.)
    |   Firefighting / Turnout gear
    |   ANYTHING with Leather in it; shoes, gloves, high heels, belts, wallets. You name it, if it has leather, I'm snagging it.
    |   ANYTHING with KEVLAR in it that I can spare; combat boots, turnout gear, kevlar helmets, motorbike boots / touring suits etc.
    |   ALL the long strings from windows. Seriously. You can never have enough long strings, either for short strings, rope or thread. They're great.
    |   Start grinding up Tailoring and Fabrication gaining proficiencies along the way. (Leatherworking/Fabric waterproofing/Plastic Working/Garment closures are the ones to work towards.
    | Mid/Lategame (No fixed time schedule but I like to be making good progress by day 30 or so depending on supplies available)
    |   Full Light Survivor set if going for a skirmishing/raiding route. (Cheapest/Easiest to make, lightest, allows dodging at lower skill levels.)
    |   Standard survivor set for general use. (Balanced, better protection, good for general purpose use.)
    |   Heavy survivor set for heavy combat / dangerous situations. (Heavy/Encumbering, very protective but leaves little weight for loot or spare gear, best for strong characters or short raids.)
    |   Alternatively if you can find the Medieval Arms & Armor books, go for a full set of platemail and chain armor with a barbute helm and become the true apocalypse knight of your dreams.
    |   No matter the choice a survivor mask is practically mandatory by this point to nulify smokers/boomers. I prefer the light one for the least encumberance. Dont forget to craft gasmask cartridges and reload & activate your mask!


.. list-table:: Survivor gear by kind and location
   :header-rows: 1

   * * Variant
     * Bodysuit
     * Legs
     * Chest
     * Coat
     * Head
     * Hands
     * Feet

   * * **Light**
     * `light Kevlar jumpsuit <https://nornagon.github.io/cdda-guide/#/item/lsurvivor_jumpsuit>`_
     * `light survivor cargo pants <https://nornagon.github.io/cdda-guide/#/item/lsurvivor_pants>`_
     * `light survivor body armor <https://nornagon.github.io/cdda-guide/#/item/lsurvivor_armor>`_
     * [`sleeveless <https://nornagon.github.io/cdda-guide/#/item/sleeveless_trenchcoat_survivor>`_] `survivor trenchcoat <https://nornagon.github.io/cdda-guide/#/item/trenchcoat_survivor>`_
     * `light survivor hood <https://nornagon.github.io/cdda-guide/#/item/hood_lsurvivor>`_
     * [`pair of fingerless <https://nornagon.github.io/cdda-guide/#/item/gloves_lsurvivor_fingerless>`_] `light survivor gloves <https://nornagon.github.io/cdda-guide/#/item/gloves_lsurvivor>`_
     * `pair of light survivor boots <https://nornagon.github.io/cdda-guide/#/item/boots_lsurvivor>`_

   * * **Regular**
     * `Kevlar jumpsuit <https://nornagon.github.io/cdda-guide/#/item/survivor_jumpsuit>`_
     * `survivor cargo pants <https://nornagon.github.io/cdda-guide/#/item/pants_survivor>`_
     * ∅
     * [`sleeveless <https://nornagon.github.io/cdda-guide/#/item/sleeveless_duster_survivor>`_] `survivor duster <https://nornagon.github.io/cdda-guide/#/item/duster_survivor>`_
     * `survivor hood <https://nornagon.github.io/cdda-guide/#/item/hood_survivor>`_
     * [`pair of fingerless <https://nornagon.github.io/cdda-guide/#/item/gloves_survivor_fingerless>`_] `survivor gloves <https://nornagon.github.io/cdda-guide/#/item/gloves_survivor>`_
     * `pair of survivor boots <https://nornagon.github.io/cdda-guide/#/item/boots_survivor>`_

   * * **Heavy**
     * `heavy Kevlar jumpsuit <https://nornagon.github.io/cdda-guide/#/item/hsurvivor_jumpsuit>`_
     * ∅
     * ∅
     * ∅
     * ∅?
     * `pair of heavy survivor gloves <https://nornagon.github.io/cdda-guide/#/item/gloves_hsurvivor>`_
     * `pair of heavy survivor gloves <https://nornagon.github.io/cdda-guide/#/item/boots_hsurvivor>`_

   * * **Fur/Winter**
     * [`faux <https://nornagon.github.io/cdda-guide/#/item/wsurvivor_jumpsuit_nofur>`_] `fur Kevlar jumpsuit <https://nornagon.github.io/cdda-guide/#/item/wsurvivor_jumpsuit>`_
     * ∅
     * ∅
     * ∅
     * [`faux <https://nornagon.github.io/cdda-guide/#/item/hood_wsurvivor_nofur>`_] `fur survivor hood <https://nornagon.github.io/cdda-guide/#/item/hood_wsurvivor>`_
     * [`pair of faux <https://nornagon.github.io/cdda-guide/#/item/gloves_wsurvivor_nofur>`_] `fur survivor gloves <https://nornagon.github.io/cdda-guide/#/item/gloves_wsurvivor>`_
     * [`pair of faux <https://nornagon.github.io/cdda-guide/#/item/boots_wsurvivor_nofur>`_] `fur survivor boots <https://nornagon.github.io/cdda-guide/#/item/boots_wsurvivor>`_

   * * **Neoprene**
     * [`thick <https://nornagon.github.io/cdda-guide/#/item/thick_h20survivor_jumpsuit>`_] `Kevlar wetsuit <https://nornagon.github.io/cdda-guide/#/item/h20survivor_jumpsuit>`_
     * ∅?
     * ∅
     * ∅?
     * `survivor wetsuit hood <https://nornagon.github.io/cdda-guide/#/item/hood_h20survivor>`_
     * `pair of survivor wetsuit gloves <https://nornagon.github.io/cdda-guide/#/item/gloves_h20survivor>`_
     * `pair of survivor wetsuit boots <https://nornagon.github.io/cdda-guide/#/item/boots_h20survivor>`_

   * * **Nomex**
     * `Kevlar firesuit <https://nornagon.github.io/cdda-guide/#/item/fsurvivor_jumpsuit>`_
     * ∅?
     * ∅
     * ∅?
     * `survivor firehood <https://nornagon.github.io/cdda-guide/#/item/hood_fsurvivor>`_
     * `pair of survivor firegloves <https://nornagon.github.io/cdda-guide/#/item/gloves_fsurvivor>`_
     * `pair of survivor fireboots <https://nornagon.github.io/cdda-guide/#/item/boots_fsurvivor>`_

Stuff that did not fit in the table:

  Nomad stuff:
  https://nornagon.github.io/cdda-guide/#/item/nomad_bodyglove_1
  https://nornagon.github.io/cdda-guide/#/item/nomad_bodyglove_2
  https://nornagon.github.io/cdda-guide/#/item/armor_nomad
  https://nornagon.github.io/cdda-guide/#/item/armor_nomad_advanced
  https://nornagon.github.io/cdda-guide/#/item/armor_nomad_light
  https://nornagon.github.io/cdda-guide/#/item/helmet_nomad
  https://nornagon.github.io/cdda-guide/#/item/nomad_rig (nomad_rig = survivor_rig + survivor_belt_notools?)

  Merc stuff:
  https://nornagon.github.io/cdda-guide/#/item/armor_mercenary_top
  https://nornagon.github.io/cdda-guide/#/item/armor_mercenary_bottom
  https://nornagon.github.io/cdda-guide/#/item/helmet_scavenger
  (there was a scavenger_gear, but it is obsolete)

  Storage / Utility:

  .. csv-table:: Survivor storage options (* MaxLen ignores penalty-inducing strap/krab points)
     :header: Option,                 Vol,  Mass, Enc (empty),(full), MaxLen, Total capacity,(excl krabs),notes

     survivor_distributed_rigging_, 3.00L, 0.44kg, 1,  3,               30cm,  7L, 18kg, -,        strapped lower torso & thighs
     survivor_belt_,                2.25L, 1.55kg, 2,  6,        1L/2kg/70cm,  9L, 16kg, -,        strapped waist,               knife sheath
     survivor_harness_,             1.25L, 0.32kg, 1, 19,     8L/8.2kg/120cm, 13L, 24kg, -,        strapped upper front torso,   rifle sling
     survivor_runner_pack_,         4.20L, 0.44kg, 3, 12,               40cm, 20L, 16kg, -,        strapped back torso
     survivor_backpack_,            5.25L, 0.60kg, 3, 24,               50cm, 45L, 51kg, 31L/33kg, strapped back torso
     survivor_rucksack_,           10.00L, 0.80kg, 3, 28,               55cm, 58L, 70kg, 35L/40kg, strapped back torso
     survivor_duffel_,              7.88L, 1.00kg, 8, 30,               60cm, 50L, 78kg, 38L/60kg, strapped back torso


   Looking at pack capacity mass ÷ pack mass, rucksack looks best: 41/10/75/36/85/88/78.
   But if you exclude the krabs, you get this: 41/10/75/36/55/50/60.


* TOOLS

  - ALWAYS WANT THESE:

    | https://nornagon.github.io/cdda-guide/#/item/survivor_scope  - increase mapping distance
    | https://nornagon.github.io/cdda-guide/#/item/survivor_vest_light -- instead of flashlight
    | https://nornagon.github.io/cdda-guide/#/item/survivor_goggles -- sunglasses (glare)






* OLD REDDIT STUFF ABOUT FULL ARMOR LOADOUT::

    hvy survivor suit 2/30/37
    win survivor suit 2/15/22 -75w
    fur coat w80	over torso/arms
    survivor duster 0/4/9 over torso/arms/legs - storage
                                                    under				over				strapped
    mouth		survivor mask 1/9/13 (win)
                    heavy survivor helmet 3/36/45					survivor hood 2/12/18
                                                                                    (win surv hood) 2/15/22
    torso		hoodie +arms 0/4/4		Kevlar 0/9/18			leather jacket +arms 1/9/9	MBR hard 5/36/60
                    t-shirt 0/1/1			2(camo?)tank tops 0/1/1		leather vest 0/9/9		MBR steel 3/30/37
                    long sleeved +arms 0/1/1					s.trenchcoat +arms 0/4/9	MBR ceramic 1/15/37
                                                                                                                    MBR 0/12/24
                                                                                                                    chest rig 0/3/3
    arms		hoodie +torso 0/4/4		2arm warmers 0/1/1		leather jacket +torso 1/9/9	chitin guards 1/18/24
                    long sleeved +torso 0/1/1					trenchcoat +torso 0/4/9		2elbow pads 0/7/7
    hands		heavy survivor gloves 2/24/30
                    chitinous gauntlets 1/18/24
                    leather armor gauntlets 0/9/9	2glove liners 0/1/1
    legs		survivor cargo 0/3/6		2boxer shorts 0/1/1		metal leg guards 2/24/24	2knee pads 0/7/7
                                                    hard leg guards 1/6/6		leather chaps 0/9/9		drop leg pouch 0/3/3
    feet		heavy survivor boots 2/36/45	flame resistant sock 0/3/3					2ankle holster 0/3/3
                    chitinous boots 1/18/24
                    leather armor boots 0/15/15
    eyes no mouth	ballistic glasses 0/9/13

    plus 2helmet netting, 2fanny packs tactical drop pouch?
    leather pouch 0/3/3


  * MBR / "modularvest" / "modular ballistic vest" becomes
    "ballistic_vest_esapi"
    "ballistic_vest_heavy"
    "legpouch_large"

    https://github.com/CleverRaven/Cataclysm-DDA/commit/6b36c10b273e693617cb161972fb561381a1c778

    "heavy survivor suit" is obsolete, becomes....

    "Survivor suits are completely superior to nomad. STURDY means you can
    get mobbed without fearing prolonged combat will wreck your armor"
    "Nomad definitely requires a lot of patching up though"



  * NEWER ADVICE:
    https://www.reddit.com/r/cataclysmdda/comments/wk7ozt/cdda_best_armor_in_experimental/

    * OUTER https://nornagon.github.io/cdda-guide/#/item/touring_suit

    * NORMAL (early game)

      | https://nornagon.github.io/cdda-guide/#/item/lsurvivor_armor
      | https://nornagon.github.io/cdda-guide/#/item/pants_survivor
      | https://nornagon.github.io/cdda-guide/#/item/survivor_jumpsuit


    This is effectively what "veteran survivor zombie" has as its loot drops.
    This is probably a good reference for good "survivor X" gear loadouts:

        https://github.com/CleverRaven/Cataclysm-DDA/blob/master/data/json/itemgroups/Clothing_Gear/clothing.json#L3032-L3280

    RE MELEE WEAPONS

        https://www.reddit.com/r/cataclysmdda/comments/usxw73/whats_the_best_melee_build_in_experimental/


8x40 Caseless Firearms Comparisons
------------------------------------------------------------



Ammo comparisons
------------------------------------------------------------

.. csv-table:: 8x40mm caseless variants (all are 0.23L 0.01kg 6cm)
   :header: Variant,   Dam,   AP, Rng, Disp , Recoil,  Noise, Price

   8x40mm_HVP_,         47,   38,  42,   75,    2200,   1870,
   8x40mm_FMJ_,         37,   28,  42,   75,    2200,   1120,
   8x40mm_,             42,   18,  42,   75,    2200,    840, 80$
   8x40mm_tracer_,      42,   18,  42,   60,    2200,    840,
   8x40mm_bootleg_,     42,    8,  42,   82,    2200,    422,
   8x40mm_JHP_,         47,    8,  42,   75,    2200,    460,
   8x40mm_sporting_,    21,   18,  42,   90,    1100,    462,


.. _8x40mm_HVP: https://nornagon.github.io/cdda-guide/#/item/8mm_hvp
.. _8x40mm_FMJ: https://nornagon.github.io/cdda-guide/#/item/8mm_fmj
.. _8x40mm: https://nornagon.github.io/cdda-guide/#/item/8mm_caseless
.. _8x40mm_tracer: https://nornagon.github.io/cdda-guide/#/item/8mm_inc
.. _8x40mm_bootleg: https://nornagon.github.io/cdda-guide/#/item/8mm_bootleg
.. _8x40mm_JHP: https://nornagon.github.io/cdda-guide/#/item/8mm_jhp
.. _8x40mm_sporting: https://nornagon.github.io/cdda-guide/#/item/8mm_civilian


.. csv-table:: Some default cartridges for comparison
   :header: VARIANT,    Vol,   Mass, Len,   Dam,   AP,  Rng, Disp,  Recoil,  Noise,    Comments

   .22 LR,            0.07L, 0.00kg, 4cm,    12,    0,   13,   60,     150,     26,
   9x18mm Makarov,    0.10L, 0.01kg, 5cm,    16,    2,   13,   60,     300,     58,
   9x19mm Mauser,     0.12L, 0.01kg, 5cm,    26,    0,   14,   60,     500,     28,
   5.7×28mm SS190,    0.12L, 0.01kg, 5cm,    20,   18,   14,   40,      90,    388,    CQB
   4.6×30mm,          0.16L, 0.01kg, 5cm,    18,   20,   14,   40,      90,    388,    CQB
   5.56×45mm M855,    0.19L, 0.01kg, 6cm,    41,    6,   36,  170,    1650,    318,
   8×40mm caseless,   0.23L, 0.01kg, 6cm,    42,   18,   42,   75,    2200,    840,    noisy!
   7.62x39mm AK,      0.11L, 0.02kg, 5cm,    45,    8,   30,   35,    2036,    420,
   7.62×51mm M80,     0.16L, 0.02kg, 5cm,    58,    6,   65,    5,    3300,    478,    disp crazy low?!
   7.62x54mmR M-N,    0.18L, 0.02kg, 6cm,    54,   10,   75,   15,    2650,    690,
   .50BMG M33,        0.45L, 0.11kg, 8cm,   131,   28,  110,  150,   25250,   3888,


.. csv-table:: Looking at actual storage spawning stuff on the floor...
   :header: MAG, Vol,   Mass, Len,  COMPAT,         per shot,     ,      ,  COMMENT

    010,       0.25L, 0.06kg,  6cm, PISTOL SMG DMR, 25.0ml,   6.0g, 6.0mm,
    025,       0.50L, 0.09kg,  8cm, PISTOL SMG DMR, 20.0ml,   3.5g, 3.2mm,  easily best for DMR
    050,       0.50L, 0.11kg,  8cm, AR BR         , 10.0ml,   2.2g, 1.6mm,
    100,       0.75L, 0.15kg,  9cm, AR BR         ,  7.5ml,   1.5g, 0.9mm,  sweet spot for rifles
    250,       2.00L, 0.34kg, 13cm,   BR LMG HMG  ,  8.0ml,   1.3g, 0.5mm,
    500,       4.00L, 1.40kg, 16cm,      LMG HMG  ,  8.0ml,   2.8g, 0.3mm,
    loose,          ,       ,     ,               ,  5.8ml,  1.2g?, 2cmm?,

::

    1000rd loose       5.75L  12.00kg
    10 × 100rd mags    7.50L  13.50kg
    40 ×  25rd mags   20.00L  15.60kg   <--- overkill; keep most loose



Laser vs. Rivtech caseless
------------------------------------------------------------

.. csv-table:: 8x40mm caseless variants (all are 0.23L 0.01kg 6cm)
   :header: Variant,   Price, Vol, Mass, Len, mags, disp, sight disp, dur, bonuses

   RM298_HMG_,    $150, 10.50L, 24.50kg, 126cm,    250/500rd,  90disp, 30sight, 9dur, +10dam -6rng
   RM614_LMG_,    $150,  2.75L,  4.60kg,  94cm,    250/500rd,  70disp, 30sight, 9dur,  +5dam
   RM88_ BR,      $175,  2.50L,  3.20kg, 100cm, 50/100/250rd,  30disp, 30sight, 9dur, +10dam
   RM51_ AR,      $120,  2.15L,  2.85kg,  91cm,     50/100rd,  50disp, 30sight, 9dur,  +5dam
   RM11B_ DMR,    $100,  2.85L,  3.10kg,  91cm,      10/25rd,  10disp, 30sight, 9dur, +10dam +20rng suppressed scoped
   RM2000_ SMG,   $100,  1.75L,  1.90kg,  66cm,      10/25rd, 120disp, 30sight, 9dur,
   RM103A_ HG,     $60,  0.75L,  1.45kg,  30cm,      10/25rd, 175disp, 30sight, 9dur,

A7 laser doing 25dam/4pen per shot, taking 1000kJ for 25 shots, so assume DOUBLE SHOTS and ignore pen ::

      rifle itself  3.00L   3.0kg
      10×UPS        40.0L  19.3kg      250 × 25dam shots
      80×hvy batt   98.4L  80.0kg     2000 × 25dam shots (loose)

RM11B doing 52dam/18pen per shot::

      rifle itself  3.35L  3.49kg
      5 × 25rd mag  2.50L  1.95kg      125 × 52dam shots
      1000 rd       5.85L 12.00kg     1000 × 52dam shots (loose)

So if you consider the weight/volume cost, the 8x40 is *crazily* more good.

On that basis I think lasers can get fucked right now.

If you could charge the laser from a rando light battery that might
be different, because you can scavenge those.

Oh maybe you can like drain all the smartphones into the UPS and then use those to shoot?

Focusing lens improves from 25dam/4pen/30rng to 30dam/4pen/45rng but still sucks compared to DMR.
Efficient emitter reduces battery cost from 40/shot to 36/shot but meh.


Light sources
------------------------------------------------------------
Considering only LIGHT_100 (100 cd/m2) and above:

|   LIGHT_500 15W USES_BIONIC_POWER nomad_harness_
|   LIGHT_500 15W CHARGEDIM heavy_flashlight_ — brightest, belt-able
|   LIGHT_450 15W CHARGEDIM shocktonfa
|   LIGHT_450 15W CHARGEDIM miner_hat_
|   LIGHT_350 10W CHARGEDIM survivor_light_  — pretty good balance?
|   LIGHT_350 10W CHARGEDIM helmet_eod
|   LIGHT_300 10W CHARGEDIM wizard_cane
|   LIGHT_300 10W CHARGEDIM wearable_camera_pro
|   LIGHT_300 10W CHARGEDIM flashlight_
|   LIGHT_300  5W           l-stick — too long unless it's your primary weapon
|   LIGHT_240 10W CHARGEDIM smart_lamp
|   LIGHT_240     CHARGEDIM handflare
|   LIGHT_200     LEAK_DAM  wearable_atomic_light

|   LIGHT_008 0.5W  cellphone flashlight
|   LIGHT_020 1.5W  smartphone flashlight

CANT_WEAR stuff
------------------------------------------------------------
* Hub 01 (Robot Faction)

  * Gear comes in 3 tiers: Prototype, Ballistic/Kinetic/Turnout, and Soldier (best).
  * Modular Defense System (or worse, Anchor) takes 1 Skirt and 1 Mantle.
  * Modular Recon Gear takes 1 Helmet.
  * Everything else (Jumpsuit, Environment Suit, Greaves, Vambraces) equips normally.

* US Army `MTV <https://en.wikipedia.org/wiki/Modular_Tactical_Vest>`_:

  Vests either take 2 ESAPI (front/back), or 2 ESAPI + 2 ESBI (front/back/sides).

  .. csv-table:: Vests (others are obsolete) -- numbers *with* full ESAPI/ESBI load
     :header: Variant,               Slots,  Encum,   Coverage,                 Warmth,  Bash,   Cut, Bullet, Other

     heavy_ballistic_vest_,         14.0kg, 2+2,   12/5/2, torso / 15% legs / 50% arms,    15,  8.03, 10.71,  21.42,
     ballistic_vest_,                9.9kg, 2+2,       12, torso,                          15,  7.77, 10.36,  20.72,
     hard_armor_vest_,               7.7kg, 2+0,        8, 92% torso,                      15,  7.77, 10.36,  20.72,
     merc_coat_,                    12.5kg, 2+2,     12/9, torso & arms,                   40,  6.94,  9.25,  18.51, 1.4acid 0.5fire 2env
     light_ballistic_vest_mag_,      5.9kg, 2+0,        5, 54% torso,                       0,  5.40,  5.40,  16.20,
     light_ballistic_vest_pouch_,    5.9kg, 2+0,        5, 54% torso,                       0,  5.40,  5.40,  16.20,
     light_ballistic_vest_shoulder_, 5.9kg, 2+0,        5, 54% torso,                       0,  5.40,  5.40,  16.20,

  .. csv-table:: Inserts (others exist but aren't interesting)
     :header: Variant, Vol,  Mass,  Len,  Encum,  Cov, Protection, Location

     ESBI,             0.8L, 1.0kg, 20cm, 1encum, 14%, 100%/25/50/50, ABLATIVE_MEDIUM – sides (under arms)
     ESAPI,            1.9L, 2.5kg, 32cm, 2encum, 27%, 100%/25/50/50, ABLATIVE_LARGE  – front/rear
     stab panel,       0.3L, 0.5kg, 16cm, 0encum, 27%,   100%/3/8/14, ABLATIVE_LARGE  – front/rear

* PALS webbing.

  To actually use this, you need to (a)ctivate the PALS receiver, then choose to "Attach pockets"

  https://www.reddit.com/r/cataclysmdda/comments/xarad5/psa_molle_webbing_belt_excellent_lowencumbrance/

  * If an item has it, it has ``attach_molle`` with a size: 4/8/14.
    PALS_SMALL consumes 1 unit;
    PALS_MEDIUM consumes 2 units;
    PALS_LARGE consumes 3 units.
    So e.g. a light_load_bearing_vest (size=4) can take LARGE/SMALL, or MEDIUM/MEDIUM, or MEDIUM/SMALL/SMALL.
    FIXME: double-check those numbers.

  .. csv-table:: PALS receiver
     :header: Slots, Variant,

     4, https://nornagon.github.io/cdda-guide/#/item/light_load_bearing_vest
     4, https://nornagon.github.io/cdda-guide/#/item/webbing_belt
     6, https://nornagon.github.io/cdda-guide/#/item/armor_riot
     6, https://nornagon.github.io/cdda-guide/#/item/armor_riot_torso
     6, https://nornagon.github.io/cdda-guide/#/item/ballistic_vest_light
     6, https://nornagon.github.io/cdda-guide/#/item/molle_pack
     8, https://nornagon.github.io/cdda-guide/#/item/heavy_load_bearing_vest_breacher
     8, https://nornagon.github.io/cdda-guide/#/item/load_bearing_vest
     8, https://nornagon.github.io/cdda-guide/#/item/load_bearing_vest_sling
     8, https://nornagon.github.io/cdda-guide/#/item/molle_medium_rucksack
     10, https://nornagon.github.io/cdda-guide/#/item/armor_mercenary_top
     10, https://nornagon.github.io/cdda-guide/#/item/ballistic_vest_esapi
     10, https://nornagon.github.io/cdda-guide/#/item/ballistic_vest_heavy
     10, https://nornagon.github.io/cdda-guide/#/item/dragonskin
     10, https://nornagon.github.io/cdda-guide/#/item/molle_large_rucksack
     14, https://nornagon.github.io/cdda-guide/#/item/heavy_load_bearing_vest
     14, https://nornagon.github.io/cdda-guide/#/item/heavy_load_bearing_vest_sling

  PALS attachment:

  | https://nornagon.github.io/cdda-guide/#/json_flag/PALS_SMALL
  | https://nornagon.github.io/cdda-guide/#/json_flag/PALS_MEDIUM
  | https://nornagon.github.io/cdda-guide/#/json_flag/PALS_LARGE



.. _smartphone:                   https://nornagon.github.io/cdda-guide/#/item/smart_phone
.. _waterproof_case:              https://nornagon.github.io/cdda-guide/#/item/waterproof_smart_phone_case
.. _firearm_repair_kit:           https://nornagon.github.io/cdda-guide/#/item/small_repairkit
.. _welder:                       https://nornagon.github.io/cdda-guide/#/item/welder
.. _bow_saw:                      https://nornagon.github.io/cdda-guide/#/item/bow_saw
.. _tin_snips:                    https://nornagon.github.io/cdda-guide/#/item/tin_snips
.. _angle_grinder:                https://nornagon.github.io/cdda-guide/#/item/angle_grinder
.. _survivor_mess_kit:            https://nornagon.github.io/cdda-guide/#/item/survivor_mess_kit
.. _tailors_kit:                  https://nornagon.github.io/cdda-guide/#/item/tailors_kit
.. _welding_goggles:              https://nornagon.github.io/cdda-guide/#/item/goggles_welding
.. _`bionic scalpel`:             https://nornagon.github.io/cdda-guide/#/item/bio_surgical_razor
.. _scalpel:                      https://nornagon.github.io/cdda-guide/#/item/scalpel
.. _sickle:                       https://nornagon.github.io/cdda-guide/#/item/sickle
.. _`survivor harness`:           https://nornagon.github.io/cdda-guide/#/item/survivor_vst
.. _`survivor belt`:              https://nornagon.github.io/cdda-guide/#/item/survivor_belt_notools
.. _RM11B:                        https://nornagon.github.io/cdda-guide/#/item/rm11b_sniper_rifle
.. _RM42:                         https://nornagon.github.io/cdda-guide/#/item/knife_rm42
.. _RM88:                         https://nornagon.github.io/cdda-guide/#/item/rm88_battle_rifle
.. _MP5SD:                        https://nornagon.github.io/cdda-guide/#/item/hk_mp5sd
.. _Eskrima:                      https://nornagon.github.io/cdda-guide/#/martial_art/style_eskrima
.. _`Krav Maga`:                  https://nornagon.github.io/cdda-guide/#/martial_art/style_krav_maga
.. _Taekwondo:                    https://nornagon.github.io/cdda-guide/#/martial_art/style_taekwondo
.. _`survivor machete`:           https://nornagon.github.io/cdda-guide/#/item/survivor_machete_qt
.. _barbarian:                    https://nornagon.github.io/cdda-guide/#/martial_art/style_barbaran
.. _shears:                       https://nornagon.github.io/cdda-guide/#/item/shears
.. _elec_shears:                  https://nornagon.github.io/cdda-guide/#/item/elec_shears
.. _`cutting`:                    https://nornagon.github.io/cdda-guide/#/tool_quality/CUT
.. _`grass cutting`:              https://nornagon.github.io/cdda-guide/#/tool_quality/GRASS_CUT
.. _`fine cutting`:               https://nornagon.github.io/cdda-guide/#/tool_quality/CUT_FINE
.. _`glare protection`:           https://nornagon.github.io/cdda-guide/#/tool_quality/GLARE
.. _`shearing`:                   https://nornagon.github.io/cdda-guide/#/tool_quality/SHEAR
.. _`churn`:                      https://nornagon.github.io/cdda-guide/#/tool_quality/CHURN
.. _`awl`:                        https://nornagon.github.io/cdda-guide/#/tool_quality/LEATHER_AWL
.. _`curved needle`:              https://nornagon.github.io/cdda-guide/#/tool_quality/SEW_CURVED
.. _`anesthesia`:                 https://nornagon.github.io/cdda-guide/#/tool_quality/ANESTHESIA
.. _`fishing`:                    https://nornagon.github.io/cdda-guide/#/tool_quality/FISHING
.. _`fish trapping`:              https://nornagon.github.io/cdda-guide/#/tool_quality/FISH_TRAP
.. _`smoothing`:                  https://nornagon.github.io/cdda-guide/#/tool_quality/SMOOTH
.. _`welding`:                    https://nornagon.github.io/cdda-guide/#/tool_quality/WELD
.. _`hammering`:                  https://nornagon.github.io/cdda-guide/#/tool_quality/HAMMER
.. _`fine hammering`:             https://nornagon.github.io/cdda-guide/#/tool_quality/HAMMER_FINE
.. _`soft hammering`:             https://nornagon.github.io/cdda-guide/#/tool_quality/HAMMER_SOFT
.. _`wood sawing`:                https://nornagon.github.io/cdda-guide/#/tool_quality/SAW_W
.. _`metal sawing`:               https://nornagon.github.io/cdda-guide/#/tool_quality/SAW_M
.. _`fine metal sawing`:          https://nornagon.github.io/cdda-guide/#/tool_quality/SAW_M_FINE
.. _`food cooking`:               https://nornagon.github.io/cdda-guide/#/tool_quality/COOK
.. _`boiling`:                    https://nornagon.github.io/cdda-guide/#/tool_quality/BOIL
.. _`containing`:                 https://nornagon.github.io/cdda-guide/#/tool_quality/CONTAIN
.. _`chemical making`:            https://nornagon.github.io/cdda-guide/#/tool_quality/CHEM
.. _`smoking`:                    https://nornagon.github.io/cdda-guide/#/tool_quality/SMOKE_PIPE
.. _`distilling`:                 https://nornagon.github.io/cdda-guide/#/tool_quality/DISTILL
.. _`tree cutting`:               https://nornagon.github.io/cdda-guide/#/tool_quality/AXE
.. _`digging`:                    https://nornagon.github.io/cdda-guide/#/tool_quality/DIG
.. _`bolt turning`:               https://nornagon.github.io/cdda-guide/#/tool_quality/WRENCH
.. _`fine bolt turning`:          https://nornagon.github.io/cdda-guide/#/tool_quality/WRENCH_FINE
.. _`screw driving`:              https://nornagon.github.io/cdda-guide/#/tool_quality/SCREW
.. _`fine screw driving`:         https://nornagon.github.io/cdda-guide/#/tool_quality/SCREW_FINE
.. _`butchering`:                 https://nornagon.github.io/cdda-guide/#/tool_quality/BUTCHER
.. _`drilling`:                   https://nornagon.github.io/cdda-guide/#/tool_quality/DRILL
.. _`rock drilling`:              https://nornagon.github.io/cdda-guide/#/tool_quality/DRILL_ROCK
.. _`prying`:                     https://nornagon.github.io/cdda-guide/#/tool_quality/PRY
.. _`nail prying`:                https://nornagon.github.io/cdda-guide/#/tool_quality/PRYING_NAIL
.. _`punch`:                      https://nornagon.github.io/cdda-guide/#/tool_quality/PUNCH
.. _`pencil`:                     https://nornagon.github.io/cdda-guide/#/tool_quality/WRITE
.. _`lifting`:                    https://nornagon.github.io/cdda-guide/#/tool_quality/LIFT
.. _`jacking`:                    https://nornagon.github.io/cdda-guide/#/tool_quality/JACK
.. _`self jacking`:               https://nornagon.github.io/cdda-guide/#/tool_quality/SELF_JACK
.. _`siphoning`:                  https://nornagon.github.io/cdda-guide/#/tool_quality/HOSE
.. _`chiseling`:                  https://nornagon.github.io/cdda-guide/#/tool_quality/CHISEL
.. _`wood chiseling`:             https://nornagon.github.io/cdda-guide/#/tool_quality/CHISEL_WOOD
.. _`sewing`:                     https://nornagon.github.io/cdda-guide/#/tool_quality/SEW
.. _`knitting`:                   https://nornagon.github.io/cdda-guide/#/tool_quality/KNIT
.. _`bullet pulling`:             https://nornagon.github.io/cdda-guide/#/tool_quality/PULL
.. _`anvil`:                      https://nornagon.github.io/cdda-guide/#/tool_quality/ANVIL
.. _`analysis`:                   https://nornagon.github.io/cdda-guide/#/tool_quality/ANALYSIS
.. _`concentration`:              https://nornagon.github.io/cdda-guide/#/tool_quality/CONCENTRATE
.. _`separation`:                 https://nornagon.github.io/cdda-guide/#/tool_quality/SEPARATE
.. _`fine distillation`:          https://nornagon.github.io/cdda-guide/#/tool_quality/FINE_DISTILL
.. _`chromatography`:             https://nornagon.github.io/cdda-guide/#/tool_quality/CHROMATOGRAPHY
.. _`grinding`:                   https://nornagon.github.io/cdda-guide/#/tool_quality/GRIND
.. _`fine grinding`:              https://nornagon.github.io/cdda-guide/#/tool_quality/FINE_GRIND
.. _`reaming`:                    https://nornagon.github.io/cdda-guide/#/tool_quality/REAM
.. _`filing`:                     https://nornagon.github.io/cdda-guide/#/tool_quality/FILE
.. _`clamping`:                   https://nornagon.github.io/cdda-guide/#/tool_quality/VISE
.. _`pressurizing`:               https://nornagon.github.io/cdda-guide/#/tool_quality/PRESSURIZATION
.. _`lockpicking`:                https://nornagon.github.io/cdda-guide/#/tool_quality/LOCKPICK
.. _`extraction`:                 https://nornagon.github.io/cdda-guide/#/tool_quality/EXTRACT
.. _`filtration`:                 https://nornagon.github.io/cdda-guide/#/tool_quality/FILTER
.. _`suspending`:                 https://nornagon.github.io/cdda-guide/#/tool_quality/SUSPENDING
.. _`rope`:                       https://nornagon.github.io/cdda-guide/#/tool_quality/ROPE
.. _`clean surface`:              https://nornagon.github.io/cdda-guide/#/tool_quality/SURFACE
.. _`wheel fastening`:            https://nornagon.github.io/cdda-guide/#/tool_quality/WHEEL_FAST
.. _`fabric cutting`:             https://nornagon.github.io/cdda-guide/#/tool_quality/FABRIC_CUT
.. _`oven cooking`:               https://nornagon.github.io/cdda-guide/#/tool_quality/OVEN
.. _`gun`:                        https://nornagon.github.io/cdda-guide/#/tool_quality/GUN
.. _`rifle`:                      https://nornagon.github.io/cdda-guide/#/tool_quality/RIFLE
.. _`shotgun`:                    https://nornagon.github.io/cdda-guide/#/tool_quality/SHOTGUN
.. _`smg`:                        https://nornagon.github.io/cdda-guide/#/tool_quality/SMG
.. _`pistol`:                     https://nornagon.github.io/cdda-guide/#/tool_quality/PISTOL
.. _`glass cutting`:              https://nornagon.github.io/cdda-guide/#/tool_quality/CUT_GLASS
.. _survivor_duffel:              https://nornagon.github.io/cdda-guide/#/item/survivor_duffel_bag
.. _survivor_backpack:            https://nornagon.github.io/cdda-guide/#/item/survivor_pack
.. _survivor_rucksack:            https://nornagon.github.io/cdda-guide/#/item/survivor_rucksack
.. _survivor_runner_pack:         https://nornagon.github.io/cdda-guide/#/item/survivor_runner_pack
.. _survivor_distributed_rigging: https://nornagon.github.io/cdda-guide/#/item/survivor_rig
.. _survivor_belt:                https://nornagon.github.io/cdda-guide/#/item/survivor_belt_notools
.. _survivor_harness:             https://nornagon.github.io/cdda-guide/#/item/survivor_vest
.. _survivor_goggles:             https://nornagon.github.io/cdda-guide/#/item/survivor_goggles
.. _hard_armor_vest:               https://nornagon.github.io/cdda-guide/#/item/level_3_vest
.. _light_ballistic_vest_mag:      https://nornagon.github.io/cdda-guide/#/item/ballistic_vest_light
.. _light_ballistic_vest_pouch:    https://nornagon.github.io/cdda-guide/#/item/ballistic_vest_light_pouches
.. _light_ballistic_vest_shoulder: https://nornagon.github.io/cdda-guide/#/item/ballistic_vest_light_operator
.. _ballistic_vest:                https://nornagon.github.io/cdda-guide/#/item/ballistic_vest_esapi
.. _heavy_ballistic_vest:          https://nornagon.github.io/cdda-guide/#/item/ballistic_vest_heavy
.. _merc_coat:                     https://nornagon.github.io/cdda-guide/#/item/armor_mercenary_top
.. _entrenching_tool:              https://nornagon.github.io/cdda-guide/#/item/e_tool
.. _locksmith_kit: https://nornagon.github.io/cdda-guide/#/item/picklocks
.. _bio_lockpick: https://nornagon.github.io/cdda-guide/#/item/bio_lockpick
.. _churn: https://nornagon.github.io/cdda-guide/#/item/churn
.. _anesthetic_kit: https://nornagon.github.io/cdda-guide/#/item/anesthetic_kit
.. _fishing_rod_professional: https://nornagon.github.io/cdda-guide/#/item/fishing_rod_professional
.. _fish_trap_basket: https://nornagon.github.io/cdda-guide/#/item/fish_trap_basket
.. _metal_smoother: https://nornagon.github.io/cdda-guide/#/item/metal_smoother
.. _long_rope: https://nornagon.github.io/cdda-guide/#/item/rope_30
.. _grappling_hook: https://nornagon.github.io/cdda-guide/#/item/grapnel
.. _still_lab: https://nornagon.github.io/cdda-guide/#/item/still_lab
.. _still: https://nornagon.github.io/cdda-guide/#/item/still
.. _chemistry_set: https://nornagon.github.io/cdda-guide/#/item/chemistry_set
.. _cordless_drill: https://nornagon.github.io/cdda-guide/#/item/cordless_drill
.. _hand_drill: https://nornagon.github.io/cdda-guide/#/item/hand_drill
.. _butchering_kit: https://nornagon.github.io/cdda-guide/#/item/butchering_kit
.. _anvil: https://nornagon.github.io/cdda-guide/#/item/anvil
.. _bronze_anvil: https://nornagon.github.io/cdda-guide/#/item/anvil_bronze
.. _puller: https://nornagon.github.io/cdda-guide/#/item/pulle
.. _nail_punch: https://nornagon.github.io/cdda-guide/#/item/punch_nail
.. _hose: https://nornagon.github.io/cdda-guide/#/item/hose
.. _analytical_set_basic: https://nornagon.github.io/cdda-guide/#/item/analytical_set_basic
.. _metal_fileset: https://nornagon.github.io/cdda-guide/#/item/metal_file
.. _mortar_pestle: https://nornagon.github.io/cdda-guide/#/item/mortar_pestle
.. _pliers_locking: https://nornagon.github.io/cdda-guide/#/item/pliers_locking
.. _plastic_sheet: https://nornagon.github.io/cdda-guide/#/item/plastic_sheet
.. _pin_reamer: https://nornagon.github.io/cdda-guide/#/item/pin_reamer
.. _dutch_oven: https://nornagon.github.io/cdda-guide/#/item/dutch_oven
.. _improvised_oven: https://nornagon.github.io/cdda-guide/#/item/improvised_oven
