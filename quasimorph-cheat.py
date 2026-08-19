#!/usr/bin/python3
import pathlib
import subprocess
import json
import pprint

src_path = pathlib.Path('slot_0_session.dat')
dst_path = pathlib.Path('slot_1_session.dat')
subprocess.check_call(['cp', '--backup=numbered', '--force', dst_path, dst_path])
dat = json.loads(src_path.read_bytes()) # read_bytes because UTF-8 *with* BOM

if True:                        # add unlock chips to ship inventory
    unlock_chips_quicklist = {
        'tia_chip': ['tia_disc_assault_1', 'tia_shock_assault_1'],
        'sun_chip': ['sun_servo_backpack_1', 'sun_laser_powersword_1', 'sun_laser_marksman_1',],
        'low_chip': ['mre_pack_1', 'medical_kit_2', ],
        'chu_chip': ['chu_shotgun_1',],
        'medium_chip': ['rifle_basic_ammo', 'military_axe_1', 'military_minigun_1', 'military_assault_1', 'military_smg_1',],
        # NOTE: armor unlocks in sets, so only need 1 of 4 a set named x_{helmet,armor,pants,boots}_y.
        'high_chip': ['automap',
                      'heavy_armored_vest_1',
                      'military_power_armor_1', # 'military_power_helmet_1', 'military_power_pants_1', 'military_power_boots_1'
                      'army_pistol_4', 'plasma_shotgun_2', 'army_sniper_2',],
        'rwa_chip': ['rwa_military_pistol_1', 'rwa_military_smg_1',
                     'rwa_power_armor_1', # 'rwa_power_helmet_1', 'rwa_power_pants_1', 'rwa_power_boots_1', # lv10, best anti-human
                     'rwa_heavy_armor_1', # 'rwa_heavy_helmet_1', 'rwa_heavy_pants_1', 'rwa_heavy_boots_1', # lv7, best anti-ssethtzentach
                     ],
        'dil_chip': ['dil_battery_ammo', 'dil_sound_assault_1', 'dil_sound_pistol_2', 'dil_chaos_assault_1', 'dil_chaos_smg_1', 'dil_shock_sniper_1',],
        'fra_chip': ['fra_security_assault_1',],
        'sbn_chip': ['sbn_rail_assault_1', 'laser_sniper_1', 'laser_smg_1', 'sbn_rail_smg_1', 'sbn_rail_shotgun_1', 'sbn_rail_pistol_1',],
        'class_chip': {
            'angels_of_spades',
            'cobra',
            'doppelganger_pack',
            'eclipse_blades',
            'golem_group',
            'martian_mech',
            'phoenix_brigade',
            'scouts_of_hades',
            'tifton_elite',
            'tongkong',
            'tunnel_rats',
            'unit_317',
            'valkyrie_squad',
        },
        'mercenary_chip': {
            'auberon_lukas',
            'bob_denarre',
            'edward_lowrance',
            'francis_reid_daly',
            'hannah_reich',
            'Isabella_capet',
            'jacques_kennet',
            'jan_shrammert',
            'kenzie_yukio',
            'laksha_saminath',
            'marika_wulfnod',
            'maximilian_rohr',
            'mirza_aishatu',
            'niko_medich',
            'persival_fawcett',
            'priya_marlon',
            'victoria_boudicca',
        },
    }
    unlock_chips = [
        {
            "Type": "MGSC.PickupItem",
            "Content": {
                "StackCount": "1",
                "_components": [
                    {
                        "Type": "MGSC.DatadiskComponent",
                        "Content": {
                            "UnlockId": unlock_id,
                            "AllowEvacuation": "True"
                        }
                    }
                ],
                "Id": chip_id,
                "SingleWeight": "0.1",
                "InventoryWidthSize": "1",
                "ExaminedItem": "True",
                "LockCounter": "0",
                "IsUseRestricted": "False",
                "InventoryPos": "0 0"
            }
        }
        for chip_id, unlock_ids in unlock_chips_quicklist.items()
        for unlock_id in unlock_ids]
    ship_cargos = [
        e['Items']
        for d in dat['Components']
        if d['Type'] == 'MGSC.MagnumCargo'
        for e in d['Content']['ShipCargo']]
    ship_cargos[0] += unlock_chips
   
if True:                        # add 20 backpacks & vests to inventory
    pack_and_vest = [
        { # archangel backpack (best overall balance, plus cheatiest settings already gives me X4 slots)
            "Type": "MGSC.PickupItem",
            "Content": {
                "StackCount": "1",
                "_components": [
                    {
                        "Type": "MGSC.BreakableItemComponent",
                        "Content": {
                            "CurrentPercent": "1",
                            "MaxPenaltyPercent": "0",
                            "MaxDurability": "220",
                            "MinDurabilityAfterRepair": "0",
                            "Unbreakable": "False"
                        }
                    },
                    {
                        "Type": "MGSC.ExtendedHeightComp",
                        "Content": {
                            # NOTE: 12->64 doesn't show up in the hover tooltip, but
                            #       it DOES actually work when equipped.
                            #       I'm a little paranoid about whether this will "eat" items in lower slots though...
                    "ExtendedHeight": "64" # 12
                        }
                    }
                ],
                "Id": "sun_servo_backpack_1",
                "SingleWeight": "0.1",  # 1.3
                "InventoryWidthSize": "1",
                "ExaminedItem": "False",
                "LockCounter": "0",
                "IsUseRestricted": "False",
                "ExaminedItem": "True",
                "InventoryPos": "0 0"
            }
        }, 
        {   # veteran vest (I picked this over panzer for the quick slots)
            "Type": "MGSC.PickupItem",
            "Content": {
                "StackCount": "1",
                "_components": [
                    {
                        "Type": "MGSC.BreakableItemComponent",
                        "Content": {
                            "CurrentPercent": "1",
                            "MaxPenaltyPercent": "0",
                            "MaxDurability": "100",
                            "MinDurabilityAfterRepair": "0",
                            "Unbreakable": "False"
                        }
                    }
                ],
                "Id": "military_armored_vest_1",
                "SingleWeight": "0.1",  # 2.4
                "InventoryWidthSize": "1",
                "ExaminedItem": "True",
                "LockCounter": "0",
                "IsUseRestricted": "False",
                "InventoryPos": "0 0"
            }
        }]
    ship_cargos = [
        e['Items']
        for d in dat['Components']
        if d['Type'] == 'MGSC.MagnumCargo'
        for e in d['Content']['ShipCargo']]
    ship_cargos[0] += [
        item
        for item in pack_and_vest
        for _ in range(20)]          # 17 clones + Big Boss + some spares


if True:                        # non-customized armor
    armor_ids = {
        # As at 1.x, rwa_heavy is STRICTLY WORSE than rwa_power.
        # 'rwa_heavy_armor_1', 'rwa_heavy_helmet_1', 'rwa_heavy_pants_1', 'rwa_heavy_boots_1', # lv7, best anti-ssethtzentach
        # 'military_power_armor_1', 'military_power_helmet_1', 'military_power_pants_1', 'military_power_boots_1', # lv8 frame armor
        'rwa_power_armor_1', 'rwa_power_helmet_1', 'rwa_power_pants_1', 'rwa_power_boots_1', # lv10, best anti-human
        }
    armor_loadout = [*[
        {"Type": "MGSC.PickupItem",
         "Content": {
             "Id": armor_id,
             "StackCount": "1",
             "_components": [
                 {"Type": "MGSC.BreakableItemComponent",
                  "Content": {
                      "CurrentPercent": "1",
                      "MaxPenaltyPercent": "0",
                      "MaxDurability": '1000', # cheat
                      "MinDurabilityAfterRepair": "0",
                      "Unbreakable": "False"}}],
               "SingleWeight": "0.1", # cheat
               "InventoryWidthSize": "1",
               "ExaminedItem": "True",
               "LockCounter": "0",
               "IsUseRestricted": "False",
               "InventoryPos": "0 0"}}
        for armor_id in armor_ids]]
    ship_cargos = [
        e['Items']
        for d in dat['Components']
        if d['Type'] == 'MGSC.MagnumCargo'
        for e in d['Content']['ShipCargo']]
    ship_cargos[0] += [
        x
        for x in armor_loadout
        for _ in range(20)]          # 17 clones + Big Boss + some spares

# Weapons are more complicated because they have inline stats.
# It might be better to craft them...
if False:
    example_weapon = {
        'Type': 'MGSC.PickupItem',
        'Content': {'Id': 'sbn_rail_pistol_1',
                    'ExaminedItem': 'True',
                    'InventoryPos': '0 21',
                    'InventoryWidthSize': '2',
                    'IsUseRestricted': 'False',
                    'LockCounter': '0',
                    'SingleWeight': '1.52',
                    'StackCount': '1',
                    '_components': [
                        {'Type': 'MGSC.BreakableItemComponent',
                         'Content': {'CurrentPercent': '1',
                                     'MaxDurability': '220',
                                     'MaxPenaltyPercent': '0',
                                     'MinDurabilityAfterRepair': '0',
                                     'Unbreakable': 'False'}},
                        {'Type': 'MGSC.WeaponComponent',
                         'Content': {'CurrentAmmo': '21',
                                     'InstanceId': '32f327b5-636d-4691-a73e-f257bda5f2a4',
                                     'LastReloadAmount': '0',
                                     'Traits': [{'ItemTraitType': 'WeaponTrait',
                                                 'TraitId': 'suppressor',
                                                 'TraitContext': 'Passive',
                                                 'Parameters': [{'BoolVal': 'True',
                                                                 'Name': 'BSuppressor',
                                                                 'ValType': 'Boolean'}]},
                                                {'TraitId': 'piercing',
                                                 'TraitContext': 'Passive',
                                                 'ItemTraitType': 'WeaponTrait',
                                                 'Parameters': [{'FloatVal': '0.7',
                                                                 'Name': 'FPierce',
                                                                 'ValType': 'Float'}]}],
                                     '_currentAmmoId': 'implicted_em_ammo',
                                     '_currentFireModeId': 'rifle_1',
                                     '_weaponId': 'sbn_rail_pistol_1'}}]}}


if True: # Add to cargo hold all the items necessary to fully upgrade all ship tech trees? (except quest item)
    ship_cargos = [
        e['Items']
        for d in dat['Components']
        if d['Type'] == 'MGSC.MagnumCargo'
        for e in d['Content']['ShipCargo']]
    ship_cargos[0] += [
        {
            "Type": "MGSC.PickupItem",
            "Content": {
                "StackCount": "100",
                "_components": [
                    # {
                    #     "Type": "MGSC.ExpireComponent",
                    #     "Content": {
                    #         "ExpireDate": "694172861938860000", # ????
                    #         "IsStarted": "False",
                    #         "IsFrozen": "False",
                    #         "LastFreezeTickTime": "0"
                    #     }
                    # },
                    {
                        "Type": "MGSC.StackableItemComponent",
                        "Content": {
                            "Count": "100", # fuck it I cannot be arsed counting these
                            "Max": "100"
                        }
                    }
                ],
                "Id": item_id,
                "SingleWeight": "0.2",
                "InventoryWidthSize": "1",
                "ExaminedItem": "True",
                "LockCounter": "0",
                "IsUseRestricted": "False",
                "InventoryPos": "0 0"
            }
        }
        for item_id in {
                'communication_relay',
                'military_unit',
                'darknet_unit',
                'expert_disk',
                'electrical_parts_container',
                'management_unit',
                'luxury_food_container',
                'alcohol_container',
                'water_container',
                'quasi_sensor_device',
                "precious_metals", # 'mining_gold', # load of gold bars? -- WRONG, but I'm not sure what this should be.
                'automap',
                'ai_module',
                'geoscanner_device',
                'entertainment_software',
                'personal_key',
                'drug_cargo',
                'security_clothing_container',
                'armor_container',
                "defibrillator_device",
                'prototype_schematics',
                'ledger_book',
                'military_parts_container',
                'ore_cargo',
                'worker_clothing_container',
                'tool_container',
                'construction_equipment',
                'welding_machine_device',
                'robot_parts_container',
                "engineering_parts_container",
                'scientific_equipment',
                'research_disk',
                'weapon_container',
                'gunbang_magazine',
                'medical_equipment',
                'mining_equipment',
                "quasisamples",
                'quasiresearch_disk',
                'hydraulic_pump',
                'regular_clothing_container',
                'miner_clothing_container',
                'robot_resurrect_device',
                'chemical_analyzer',
                'memory_software',
                'electrical_parts_container',
                'biomass_tank',
                'organs_box',
                "pills_steroids",
                # Too questy to unlock from the start...
                # 'anulator',
                # parts for upgrading armor pieces and stuff
                # For 1 piece of warlord armor: 10 high_chip, 39 capacitor_parts, 72 ceramite_plates?, 30 rwa_chip, 15 military_parts_container
                # There is no cap on levelling up clones though, it just costs more parts and time.
                # For 1 clone with 99 upgrades: 94 biomass_tank, 47 organs_box, 35 drug_cargo, 35 medical_components, 215 mercenary_chip
                "medical_components",
                # Too buggy.
                # *unlock_chips_quicklist.keys(),
                # What about components for making weapons in the shop (since I am not gonna spawn them here)...
                "capacitor_parts",
                "transformer",
                "rubber",
                "circuit_board",
                "plastic",
                "blunt_parts",
                "armor_plates",
                "coarse_parts",
                "bulb",
                "lens",
                "pierce_parts",
                "rags",
                "spring",
                "ceramite_plates",
                # WRONG # "microelectronic_parts",
                "rod_parts",
                "rusty_plates",
                "broken_weapon",
                "wire",
                "metal_tread",
        }]


if True:   # pre-complete slow/expensive item & clone upgrade projects
    # WARNING: I tried bumping the stats of armor up, but they then didn't take?
    #          Therefore I did the upgrade in-game and then copied the ModificationsCount and stats over.
    new_projects = [
        # Clones
        {'ProjectType': 'Mercenary',
         'DevelopId': 'persival_fawcett',
         'StartTime': '694339524866210000', # FIXME: is this appropriate?
         'FinishTime': '694341979580480000', # FIXME: is this appropriate?
         'ModificationsCount': '49',
         'AppliedModifications': [
             {'Key': 'mercenary_health', 'Value': '230'},
             {'Key': 'mercenary_pain_threshold', 'Value': '30'},
             {'Key': 'mercenary_dodge', 'Value': '0.5'},
             {'Key': 'mercenary_starvation', 'Value': '3000'},
             {'Key': 'mercenary_range_accuracy', 'Value': '0.45'}],
         'CachedItems': [],
         'IsInDevelopmentb': 'False',
         'ModifyStartPrice': '0',
         'UpcomingModifications': [],
         'UpcomingModificationsCount': '0'},
        # Classes
        {'ProjectType': 'MercenaryClass',
         'DevelopId': 'scouts_of_hades',
         'StartTime': '694339524866210000', # FIXME: is this appropriate?
         'FinishTime': '694341979580480000', # FIXME: is this appropriate?
         'ModificationsCount': '4',
         'AppliedModifications': [
             {'Key': 'mercenaryclass_perk0', 'Value': 'cyber_compatibility_basic'},
             {'Key': 'mercenaryclass_perk2', 'Value': 'steel_without_basic'},
             {'Key': 'mercenaryclass_perk3', 'Value': 'battle_concentration_basic'},
             {'Key': 'mercenaryclass_perk4', 'Value': 'reaction_training_basic'}],
         'CachedItems': [],
         'IsInDevelopment': 'False',
         'ModifyStartPrice': '30',
         'UpcomingModifications': [],
         'UpcomingModificationsCount': '0'},
        # Weapons
        {'ProjectType': 'RangeWeapon',
         'DevelopId': 'sbn_rail_assault_1',
         'StartTime': '694339524866210000', # FIXME: is this appropriate?
         'FinishTime': '694341979580480000', # FIXME: is this appropriate?
         'AppliedModifications': [
             {'Key': 'rangeweapon_max_durability', 'Value': '215'},
             {'Key': 'rangeweapon_damage', 'Value': '150'},
             {'Key': 'rangeweapon_crit_damage', 'Value': '2.5'},
             {'Key': 'rangeweapon_accuracy', 'Value': '0.65'},
             {'Key': 'rangeweapon_scatter_angle', 'Value': '0.9'}],
         'CachedItems': [],
         'IsInDevelopment': 'False',
         'ModificationsCount': '40',
         'ModifyStartPrice': '11',
         'UpcomingModifications': [],
         'UpcomingModificationsCount': '0'},
        {'ProjectType': 'RangeWeapon',
         'DevelopId': 'dil_chaos_assault_1',
         'StartTime': '694339524866210000', # FIXME: is this appropriate?
         'FinishTime': '694341979580480000', # FIXME: is this appropriate?
         'ModificationsCount': '40',
         'AppliedModifications': [
             {'Key': 'rangeweapon_max_durability', 'Value': '145'},
             {'Key': 'rangeweapon_weight', 'Value': '4.74'},
             {'Key': 'rangeweapon_damage', 'Value': '136'},
             {'Key': 'rangeweapon_crit_damage', 'Value': '2.05'},
             {'Key': 'rangeweapon_accuracy', 'Value': '0.52'},
             {'Key': 'rangeweapon_scatter_angle', 'Value': '3'},
             {'Key': 'rangeweapon_reload_duration', 'Value': '5'},
             {'Key': 'rangeweapon_magazine_capacity', 'Value': '35'}],
         'CachedItems': [],
         'IsInDevelopment': 'False',
         'ModifyStartPrice': '11',
         'UpcomingModifications': [],
         'UpcomingModificationsCount': '0'},
        {'ProjectType': 'MeleeWeapon',
         'DevelopId': 'military_axe_1',
         'StartTime': '694339524866210000', # FIXME: is this appropriate?
         'FinishTime': '694341979580480000', # FIXME: is this appropriate?
         'ModificationsCount': '11',
         'AppliedModifications': [
             {'Key': 'meleeweapon_max_durability', 'Value': '135'},
             {'Key': 'meleeweapon_damage', 'Value': '71'},
             {'Key': 'meleeweapon_crit_damage', 'Value': '1.95'},
             {'Key': 'meleeweapon_accuracy', 'Value': '0.4'}],
         'CachedItems': [],
         'IsInDevelopment': 'False',
         'ModifyStartPrice': '11',
         'UpcomingModifications': [],
         'UpcomingModificationsCount': '0'},

        # Armor
        {"ProjectType": "Armor",
         "DevelopId": "rwa_power_armor_1",
         'StartTime': '694339524866210000', # FIXME: is this appropriate?
         'FinishTime': '694341979580480000', # FIXME: is this appropriate?
         "IsInDevelopment": "False",
         "ModificationsCount": "40",
         "UpcomingModificationsCount": "0",
      "ModifyStartPrice": "33",
         "AppliedModifications": [
             {"Key": "armor_resist_blunt", "Value": "40"},
             {"Key": "armor_resist_fire", "Value": "40"},
             {"Key": "armor_resist_pierce", "Value": "40"},
             {"Key": "armor_resist_cold", "Value": "36"},
             {"Key": "armor_resist_lacer", "Value": "38"},
             {"Key": "armor_resist_shock", "Value": "36"},
             {"Key": "armor_resist_beam", "Value": "36"},
             {"Key": "armor_resist_poison", "Value": "36"}],
         "UpcomingModifications": [],
         "CachedItems": []},
        {'ProjectType': 'Helmet',
         'DevelopId': 'rwa_power_helmet_1',
         'StartTime': '694339524866210000', # FIXME: is this appropriate?
         'FinishTime': '694341979580480000', # FIXME: is this appropriate?
         'ModificationsCount': '40',
         'AppliedModifications': [
             {'Key': 'helmet_resist_blunt', 'Value': '21'},
             {'Key': 'helmet_resist_fire', 'Value': '19'},
             {'Key': 'helmet_resist_pierce', 'Value': '21'},
             {'Key': 'helmet_resist_cold', 'Value': '20'},
             {'Key': 'helmet_resist_lacer', 'Value': '21'},
             {'Key': 'helmet_resist_shock', 'Value': '19'},
             {'Key': 'helmet_resist_beam', 'Value': '19'},
             {'Key': 'helmet_resist_poison', 'Value': '18'}],
         'CachedItems': [],
         'IsInDevelopment': 'False',
         'ModifyStartPrice': '13',
         'UpcomingModifications': [],
         'UpcomingModificationsCount': '0'},
        {'ProjectType': 'Leggings',
         'DevelopId': 'rwa_power_pants_1',
         'StartTime': '694339524866210000', # FIXME: is this appropriate?
         'FinishTime': '694341979580480000', # FIXME: is this appropriate?
         'ModificationsCount': '40',
         'AppliedModifications': [
             {'Key': 'leggings_resist_blunt', 'Value': '30'},
             {'Key': 'leggings_resist_fire', 'Value': '30'},
             {'Key': 'leggings_resist_pierce', 'Value': '27'},
             {'Key': 'leggings_resist_cold', 'Value': '27'},
             {'Key': 'leggings_resist_lacer', 'Value': '29'},
             {'Key': 'leggings_resist_shock', 'Value': '27'},
             {'Key': 'leggings_resist_beam', 'Value': '27'},
             {'Key': 'leggings_resist_poison', 'Value': '30'}],
         'CachedItems': [],
         'IsInDevelopment': 'False',
         'ModifyStartPrice': '23',
         'UpcomingModifications': [],
         'UpcomingModificationsCount': '0'},
        {'ProjectType': 'Boots',
         'DevelopId': 'rwa_power_boots_1',
         'StartTime': '694339524866210000', # FIXME: is this appropriate?
         'FinishTime': '694341979580480000', # FIXME: is this appropriate?
         'ModificationsCount': '40',
         'AppliedModifications': [
             {'Key': 'boots_resist_blunt', 'Value': '19'},
             {'Key': 'boots_resist_fire', 'Value': '17'},
             {'Key': 'boots_resist_pierce', 'Value': '19'},
             {'Key': 'boots_resist_cold', 'Value': '16'},
             {'Key': 'boots_resist_lacer', 'Value': '20'},
             {'Key': 'boots_resist_shock', 'Value': '17'},
             {'Key': 'boots_resist_beam', 'Value': '17'},
             {'Key': 'boots_resist_poison', 'Value': '20'}],
         'CachedItems': [],
         'IsInDevelopment': 'False',
         'ModifyStartPrice': '13',
         'UpcomingModifications': [],
         'UpcomingModificationsCount': '0'},
    ]
    projects, = [
        d['Content']['Values']
        for d in dat['Components']
        if d['Type'] == 'MGSC.MagnumProjects']
    for new_project in new_projects:
        if not any(new_project['DevelopId'] == p['DevelopId'] for p in projects):
            projects.append(new_project)
    # UPDATE: upgraded clones don't get the attribute benefits unless you reboot them.
    #         You can do this from the clone upgrade scheme, AFTER the upgrade completes.
    # UPDATE: upgraded classes don't affect already-assigned classes.
    #         You can fix this by going to a clone's assigned class, changing it, then changing it back.
    # UPDATE: when you modify an item, newly-made items change from
    #         "rwa_power_helmet_1" to
    #         "rwa_power_helmet_1_custom".
    #         Any items you already had DON'T get upgraded.
    #         You MUST unlock the ship's upgrade station, THEN
    #         upgrade the item, THEN
    #         make the armour/weapon item in the ship's factory station.
    #         Then for the actual stat changes you have something like this in MGSC.MagnumProjects:
    # See if we can fix that...
    # UPDATE: too annoying, needs to go into .Traits._weaponId and stuff as well...
    if False:
        item_dicts = [
            item['Content']
            for d in dat['Components']
            if d['Type'] == 'MGSC.MagnumCargo'
            for e in d['Content']['ShipCargo']
            for item in e['Items']]
        develop_ids = {p['DevelopId'] for p in projects}
        for i in item_dicts:
            if i['Id'] in develop_ids:
                i['Id'] = i['Id'] + '_custom'
    else:
        item_dicts = [
            item['Content']
            for d in dat['Components']
            if d['Type'] == 'MGSC.MagnumCargo'
            for e in d['Content']['ShipCargo']
            for item in e['Items']]
        for i in item_dicts:
            if i['Id'] in {'rwa_power_armor_1', 'rwa_power_helmet_1', 'rwa_power_pants_1', 'rwa_power_boots_1'}:
                i['Id'] = i['Id'] + '_custom'
        
    

# Go through ALL the existing weapons/armor in the cargo hold and set their weight to 0.1kg?
# And mark them as "seen".
if True:
    item_dicts = [
        item['Content']
        for d in dat['Components']
        if d['Type'] == 'MGSC.MagnumCargo'
        for e in d['Content']['ShipCargo']
        for item in e['Items']]
    for i in item_dicts:
        if 'ExaminedItem' in i:
            i['ExaminedItem'] = 'True'
        if 'SingleWeight' in i:
            if float(i['SingleWeight']) > 0.1: # don't INCREASE ammo weight!
                i['SingleWeight'] = '0.1'

dst_path.write_text(json.dumps(dat, indent=2))
