#!/usr/bin/python3
import pathlib
import subprocess
import json
import pprint

# from jsonpath_ng import jsonpath, parse
# print(parse('Components[Type="MGSC.Difficulty"]').find(dat))

src_path = pathlib.Path('slot_0_session.dat')
dst_path = pathlib.Path('slot_1_session.dat')
subprocess.check_call(['cp', '--backup=numbered', '--force', dst_path, dst_path])
dat = json.loads(src_path.read_bytes()) # read_bytes because UTF-8 *with* BOM
#help(json.dumps)

# mercenaries, = [d['Content']
#                 for d in dat['Components']
#                 if d['Type'] == 'MGSC.Mercenaries']

# all_classes = {'scouts_of_hades', 'eclipse_blades', 'tifton_elite',
#     'phoenix_brigade', 'doppelganger_pack', 'golem_group', 'unit_317',
#     'tunnel_rats', 'valkyrie_squad', 'cobra', 'tongkong',
#     'angels_of_spades', 'martian_mech',
# }
# mercenaries['UnlockedClasses'] = sorted(all_classes | set(mercenaries['UnlockedClasses'])) # mainly for early tunnel_rats
# if False:
#     # This isn't working AFAICT
#     # I think instead we need to add mercenary_chip items to the inventory...
#     all_mercs = {
#         'auberon_lukas',
#         'bob_denarre',
#         'edward_lowrance',
#         'francis_reid_daly',
#         'hannah_reich',
#         'Isabella_capet',
#         'jacques_kennet',
#         'jan_shrammert',
#         'kenzie_yukio',
#         'laksha_saminath',
#         'marika_wulfnod',
#         'maximilian_rohr',
#         'niko_medich',
#         'persival_fawcett',
#         'priya_marlon',
#         'victoria_boudicca',
#     }
#     mercenaries['UnlockedMercenaries'] = sorted(all_mercs | set(mercenaries['UnlockedMercenaries']))
#     # Don't add any mercenaries, but give already-bred mercenaries best stats of all mercenaries.


# # Note this excludes perks provided by class!
# # Note this excludes the "rank_N" perks that implement levelling up!
# all_perks = [
#     # {'Parameters': [], 'AIParameters': [], 'PerkId': 'rank_0', 'NextPerkId': 'rank_1', 'LevelUpActionType': 'AnyKill', 'CurrentExp': '0', 'ExpPerAction': '1', 'MaxExp': '7', 'PerkType': 'Rank'},
#     {'Parameters': [{'PerkId': 'assault_reflex_basic', 'NextPerkId': 'assault_reflex_advanced', 'Name': 'IDuration', 'ValType': 'Int', 'IntVal': '2'}, {'Name': 'ICooldown', 'ValType': 'Int', 'IntVal': '12'}, {'Name': 'IActivation', 'ValType': 'Int', 'IntVal': '80'}, {'Name': 'IAddedAP', 'ValType': 'Int', 'IntVal': '1'}], 'AIParameters': [], 'LevelUpActionType': 'EnemyAttackMissed', 'CurrentExp': '10', 'ExpPerAction': '5', 'MaxExp': '20', 'PerkType': 'Trigger'},
#     {'Parameters': [{'PerkId': 'athletics_basic', 'NextPerkId': 'athletics_advanced', 'Name': 'FSprintAccDebuff', 'ValType': 'Float', 'FloatVal': '-0.35'}], 'AIParameters': [], 'LevelUpActionType': 'Run', 'CurrentExp': '0', 'ExpPerAction': '1', 'MaxExp': '30', 'PerkType': 'Passive'},
#     {'Parameters': [{'PerkId': 'battle_physicist_basic', 'NextPerkId': 'battle_physicist_advanced', 'Name': 'FEnergySaving', 'ValType': 'Float', 'FloatVal': '0.2'}], 'AIParameters': [], 'LevelUpActionType': 'DisassembleBatteryGuns', 'CurrentExp': '0', 'ExpPerAction': '5', 'MaxExp': '20', 'PerkType': 'Passive'},
#     {'Parameters': [{'PerkId': 'berserk_gang_basic', 'NextPerkId': 'berserk_gang_advanced', 'Name': 'IDuration', 'ValType': 'Int', 'IntVal': '6'}, {'Name': 'ICooldown', 'ValType': 'Int', 'IntVal': '14'}, {'Name': 'IActivation', 'ValType': 'Int', 'IntVal': '80'}, {'Name': 'IHealthRegen', 'ValType': 'Int', 'IntVal': '4'}, {'Name': 'IPainRegen', 'ValType': 'Int', 'IntVal': '3'}], 'AIParameters': [], 'LevelUpActionType': 'ReceiveDamagingWound', 'CurrentExp': '0', 'ExpPerAction': '10', 'MaxExp': '20', 'PerkType': 'Trigger'},
#     {'Parameters': [{'PerkId': 'blind_fury_basic', 'NextPerkId': 'blind_fury_advanced', 'Name': 'IDuration', 'ValType': 'Int', 'IntVal': '3'}, {'Name': 'ICooldown', 'ValType': 'Int', 'IntVal': '9'}, {'Name': 'IActivation', 'ValType': 'Int', 'IntVal': '80'}, {'Name': 'FDamage', 'ValType': 'Float', 'FloatVal': '0.55'}], 'AIParameters': [], 'LevelUpActionType': 'PlayerHitted', 'CurrentExp': '10', 'ExpPerAction': '10', 'MaxExp': '20', 'PerkType': 'Trigger'},
#     {'Parameters': [{'PerkId': 'cannibalism_basic', 'NextPerkId': 'cannibalism_advanced', 'Name': 'IDuration', 'ValType': 'Int', 'IntVal': '3'}, {'Name': 'ICooldown', 'ValType': 'Int', 'IntVal': '15'}, {'Name': 'IActivation', 'ValType': 'Int', 'IntVal': '80'}, {'Name': 'FDamage', 'ValType': 'Float', 'FloatVal': '0.45'}], 'AIParameters': [], 'LevelUpActionType': 'EatRawHumanMeat', 'CurrentExp': '0', 'ExpPerAction': '10', 'MaxExp': '20', 'PerkType': 'Trigger'},
#     {'Parameters': [{'PerkId': 'carnage_basic', 'NextPerkId': 'carnage_advanced', 'Name': 'IDuration', 'ValType': 'Int', 'IntVal': '2'}, {'Name': 'ICooldown', 'ValType': 'Int', 'IntVal': '20'}, {'Name': 'IActivation', 'ValType': 'Int', 'IntVal': '120'}, {'Name': 'FRestoreAP', 'ValType': 'Float', 'FloatVal': '0.7'}], 'AIParameters': [], 'LevelUpActionType': 'OnMeleeWoundInflict', 'CurrentExp': '0', 'ExpPerAction': '10', 'MaxExp': '20', 'PerkType': 'Trigger'},
#     {'Parameters': [{'PerkId': 'cauterize_basic', 'NextPerkId': 'cauterize_advanced', 'Name': 'IDuration', 'ValType': 'Int', 'IntVal': '3'}, {'Name': 'ICooldown', 'ValType': 'Int', 'IntVal': '7'}, {'Name': 'IActivation', 'ValType': 'Int', 'IntVal': '40'}, {'Name': 'BBurnImmune', 'ValType': 'Boolean', 'BoolVal': 'True'}, {'Name': 'IHealthRegen', 'ValType': 'Int', 'IntVal': '6'}], 'AIParameters': [], 'LevelUpActionType': 'OnTakingBurn', 'CurrentExp': '0', 'ExpPerAction': '10', 'MaxExp': '20', 'PerkType': 'Trigger'},
#     {'Parameters': [{'PerkId': 'cautious_basic', 'NextPerkId': 'cautious_advanced', 'Name': 'IDuration', 'ValType': 'Int', 'IntVal': '5'}, {'Name': 'ICooldown', 'ValType': 'Int', 'IntVal': '22'}, {'Name': 'IActivation', 'ValType': 'Int', 'IntVal': '120'}, {'Name': 'FCritChance', 'ValType': 'Float', 'FloatVal': '0.3'}, {'Name': 'FCritDamage', 'ValType': 'Float', 'FloatVal': '0.5'}], 'AIParameters': [], 'LevelUpActionType': 'NoticeHiddenEnemy', 'CurrentExp': '0', 'ExpPerAction': '10', 'MaxExp': '20', 'PerkType': 'Trigger'},
#     {'Parameters': [{'PerkId': 'cold_weapon_wielding_basic', 'NextPerkId': 'cold_weapon_wielding_advanced', 'Name': 'FMeleeAccuracy', 'ValType': 'Float', 'FloatVal': '0.15'}], 'AIParameters': [], 'LevelUpActionType': 'MeleeHitOnEnemy', 'CurrentExp': '0', 'ExpPerAction': '5', 'MaxExp': '20', 'PerkType': 'Passive'},
#     {'Parameters': [{'PerkId': 'covermaster_basic', 'NextPerkId': 'covermaster_advanced', 'Name': 'ICoverOverallBonus', 'ValType': 'Int', 'IntVal': '15'}], 'AIParameters': [], 'LevelUpActionType': 'EnemyAttackMissed', 'CurrentExp': '0', 'ExpPerAction': '2', 'MaxExp': '20', 'PerkType': 'Passive'},
#     {'Parameters': [{'PerkId': 'cqc_specialist_master', 'NextPerkId': 'cqc_specialist_legend', 'Name': 'FScatter', 'ValType': 'Float', 'FloatVal': '-0.35'}, {'Name': 'FRangeAccuracy', 'ValType': 'Float', 'FloatVal': '0.2'}], 'AIParameters': [], 'LevelUpActionType': 'ShotRangedWeapon', 'CurrentExp': '22', 'ExpPerAction': '2', 'MaxExp': '80', 'PerkType': 'Passive'},
#     {'Parameters': [{'PerkId': 'dirty_shot_basic', 'NextPerkId': 'dirty_shot_advanced', 'Name': 'IDuration', 'ValType': 'Int', 'IntVal': '1'}, {'Name': 'ICooldown', 'ValType': 'Int', 'IntVal': '6'}, {'Name': 'IActivation', 'ValType': 'Int', 'IntVal': '40'}, {'Name': 'IEnemyStunDuration', 'ValType': 'Int', 'IntVal': '1'}, {'Name': 'IEnemyCount', 'ValType': 'Int', 'IntVal': '1'}], 'AIParameters': [], 'LevelUpActionType': 'OnCrit', 'CurrentExp': '0', 'ExpPerAction': '10', 'MaxExp': '20', 'PerkType': 'Trigger'},
#     {'Parameters': [{'PerkId': 'fire_transfer_advanced', 'NextPerkId': 'fire_transfer_master', 'Name': 'IDuration', 'ValType': 'Int', 'IntVal': '2'}, {'Name': 'ICooldown', 'ValType': 'Int', 'IntVal': '4'}, {'Name': 'IActivation', 'ValType': 'Int', 'IntVal': '10'}, {'Name': 'FCritChance', 'ValType': 'Float', 'FloatVal': '0.55'}, {'Name': 'BActionPointDuration', 'ValType': 'Boolean', 'BoolVal': 'True'}], 'AIParameters': [], 'LevelUpActionType': 'AnyKill', 'CurrentExp': '8', 'ExpPerAction': '2', 'MaxExp': '50', 'PerkType': 'Trigger'},
#     {'Parameters': [{'PerkId': 'gear_maintenance_basic', 'NextPerkId': 'gear_maintenance_advanced', 'Name': 'FPhysicalResists', 'ValType': 'Float', 'FloatVal': '0.15'}, {'Name': 'FArmorDurability', 'ValType': 'Float', 'FloatVal': '0.15'}], 'AIParameters': [], 'LevelUpActionType': 'PhysicalDmgAbsorbedByResist', 'CurrentExp': '4', 'ExpPerAction': '2', 'MaxExp': '20', 'PerkType': 'Passive'},
#     {'Parameters': [{'PerkId': 'handmade_shotgun_ammo_basic', 'NextPerkId': 'handmade_shotgun_ammo_advanced', 'Name': 'FShellAmmoDamage', 'ValType': 'Float', 'FloatVal': '0.2'}], 'AIParameters': [], 'LevelUpActionType': 'ShotShellsAmmo', 'CurrentExp': '0', 'ExpPerAction': '2', 'MaxExp': '20', 'PerkType': 'Passive'},
#     {'Parameters': [{'PerkId': 'marauder_basic', 'NextPerkId': 'marauder_advanced', 'Name': 'FLootCorpseItem', 'ValType': 'Float', 'FloatVal': '0.3'}, {'Name': 'FLootStorageItem', 'ValType': 'Float', 'FloatVal': '0.3'}], 'AIParameters': [], 'LevelUpActionType': 'LootUniqCorpse', 'CurrentExp': '0', 'ExpPerAction': '1', 'MaxExp': '20', 'PerkType': 'Passive'},
#     {'Parameters': [{'PerkId': 'military_training_legend', 'NextPerkId': {}, 'Name': 'IStarvStanceBonus', 'ValType': 'Int', 'IntVal': '-5'}], 'AIParameters': [], 'LevelUpActionType': 'WeightMove', 'CurrentExp': '0', 'ExpPerAction': '0', 'MaxExp': '0', 'PerkType': 'Passive'},
#     {'Parameters': [{'PerkId': 'reaction_training_basic', 'NextPerkId': 'reaction_training_advanced', 'Name': 'FDodge', 'ValType': 'Float', 'FloatVal': '0.1'}], 'AIParameters': [], 'LevelUpActionType': 'EnemyAttackMissed', 'CurrentExp': '0', 'ExpPerAction': '4', 'MaxExp': '20', 'PerkType': 'Passive'},
#     {'Parameters': [{'PerkId': 'reinforced_battery_basic', 'NextPerkId': 'reinforced_battery_advanced', 'Name': 'FBatteryAmmoDamage', 'ValType': 'Float', 'FloatVal': '0.15'}], 'AIParameters': [], 'LevelUpActionType': 'OnAttackWithBatteryAmmo', 'CurrentExp': '0', 'ExpPerAction': '2', 'MaxExp': '20', 'PerkType': 'Passive'},
#     {'Parameters': [{'PerkId': 'revealing_flame_basic', 'NextPerkId': 'revealing_flame_advanced', 'Name': 'IDuration', 'ValType': 'Int', 'IntVal': '8'}, {'Name': 'ICooldown', 'ValType': 'Int', 'IntVal': '12'}, {'Name': 'IActivation', 'ValType': 'Int', 'IntVal': '80'}, {'Name': 'IRevealRange', 'ValType': 'Int', 'IntVal': '4'}, {'Name': 'BRevealingSignal', 'ValType': 'Boolean', 'BoolVal': 'True'}], 'AIParameters': [], 'LevelUpActionType': 'PutFireOnEnemy', 'CurrentExp': '0', 'ExpPerAction': '10', 'MaxExp': '20', 'PerkType': 'Trigger'},
#     {'Parameters': [{'PerkId': 'scholar_basic', 'NextPerkId': 'scholar_advanced', 'Name': 'IScholarCraft', 'ValType': 'Int', 'IntVal': '1'}], 'AIParameters': [], 'LevelUpActionType': 'OnProductionCraft', 'CurrentExp': '0', 'ExpPerAction': '1', 'MaxExp': '20', 'PerkType': 'Passive'},
#     {'Parameters': [{'PerkId': 'shielding_basic', 'NextPerkId': 'shielding_advanced', 'Name': 'FElementalResists', 'ValType': 'Float', 'FloatVal': '0.25'}], 'AIParameters': [], 'LevelUpActionType': 'ElementalDmgAbsorbedByResist', 'CurrentExp': '0', 'ExpPerAction': '4', 'MaxExp': '20', 'PerkType': 'Passive'},
#     {'Parameters': [{'PerkId': 'talent_beneficial_mutation', 'NextPerkId': {}, 'Name': 'BIgnoreInfection', 'ValType': 'Boolean', 'BoolVal': 'True'}, {'Name': 'FMissingHealthDamageIncrease', 'ValType': 'Float', 'FloatVal': '0.05'}], 'AIParameters': [], 'LevelUpActionType': 'None', 'CurrentExp': '0', 'ExpPerAction': '0', 'MaxExp': '0', 'PerkType': 'Talent'},
#     {'Parameters': [{'PerkId': 'talent_dog_of_war', 'NextPerkId': '', 'Name': 'IHealthRegen', 'ValType': 'Int', 'IntVal': '2'}, {'Name': 'IPerkCooldownBonus', 'ValType': 'Int', 'IntVal': '-3'}], 'AIParameters': [], 'LevelUpActionType': 'None', 'CurrentExp': '0', 'ExpPerAction': '0', 'MaxExp': '0', 'PerkType': 'Talent'},
#     {'Parameters': [{'PerkId': 'talent_dreamer', 'NextPerkId': '', 'Name': 'IQMorphGain', 'ValType': 'Int', 'IntVal': '-1'}, {'Name': 'IAILosBonus', 'ValType': 'Int', 'IntVal': '-1'}], 'AIParameters': [], 'LevelUpActionType': 'None', 'CurrentExp': '0', 'ExpPerAction': '0', 'MaxExp': '0', 'PerkType': 'Talent'},
#     {'Parameters': [{'PerkId': 'talent_feel_no_pain', 'NextPerkId': {}, 'Name': 'BIgnorePain', 'ValType': 'Boolean', 'BoolVal': 'True'}, {'Name': 'FIncomeCritMult', 'ValType': 'Float', 'FloatVal': '-0.5'}], 'AIParameters': [], 'LevelUpActionType': 'None', 'CurrentExp': '0', 'ExpPerAction': '0', 'MaxExp': '0', 'PerkType': 'Talent'},
#     {'Parameters': [{'PerkId': 'talent_field_medic', 'NextPerkId': '', 'Name': 'IFixationHeal', 'ValType': 'Int', 'IntVal': '3'}, {'Name': 'FImplantDropChance', 'ValType': 'Float', 'FloatVal': '0.25'}], 'AIParameters': [], 'LevelUpActionType': 'None', 'CurrentExp': '0', 'ExpPerAction': '0', 'MaxExp': '0', 'PerkType': 'Talent'},
#     {'Parameters': [{'PerkId': 'talent_gunsmith', 'NextPerkId': {}, 'Name': 'FWeaponDurability', 'ValType': 'Float', 'FloatVal': '1.2'}, {'Name': 'FEquipWeaponWeight', 'ValType': 'Float', 'FloatVal': '-0.5'}], 'AIParameters': [], 'LevelUpActionType': 'None', 'CurrentExp': '0', 'ExpPerAction': '0', 'MaxExp': '0', 'PerkType': 'Talent'},
#     {'Parameters': [{'PerkId': 'talent_invincible', 'NextPerkId': {}, 'Name': 'IResists', 'ValType': 'Int', 'IntVal': '12'}, {'Name': 'FWeightMeleeDmgIncrease', 'ValType': 'Float', 'FloatVal': '0.12'}, {'Name': 'IKiloDmgThreshold', 'ValType': 'Int', 'IntVal': '10'}], 'AIParameters': [], 'LevelUpActionType': 'None', 'CurrentExp': '0', 'ExpPerAction': '0', 'MaxExp': '0', 'PerkType': 'Talent'},
#     {'Parameters': [{'PerkId': 'talent_ninjutsu', 'NextPerkId': '', 'Name': 'FWeightAffectDodge', 'ValType': 'Float', 'FloatVal': '0.6'}, {'Name': 'IThrowRangeBonus', 'ValType': 'Int', 'IntVal': '2'}], 'AIParameters': [], 'LevelUpActionType': 'None', 'CurrentExp': '0', 'ExpPerAction': '0', 'MaxExp': '0', 'PerkType': 'Talent'},
#     {'Parameters': [{'PerkId': 'talent_one_man_army', 'NextPerkId': '', 'Name': 'BThirdWeaponSlot', 'ValType': 'Boolean', 'BoolVal': 'True'}, {'Name': 'FExplosionIncomeDamageMult', 'ValType': 'Float', 'FloatVal': '-0.5'}], 'AIParameters': [], 'LevelUpActionType': 'None', 'CurrentExp': '0', 'ExpPerAction': '0', 'MaxExp': '0', 'PerkType': 'Talent'},
#     {'Parameters': [{'PerkId': 'talent_preparation', 'NextPerkId': '', 'Name': 'BBackstabResistIgnore', 'ValType': 'Boolean', 'BoolVal': 'True'}, {'Name': 'IRevealRange', 'ValType': 'Int', 'IntVal': '4'}], 'AIParameters': [], 'LevelUpActionType': 'None', 'CurrentExp': '0', 'ExpPerAction': '0', 'MaxExp': '0', 'PerkType': 'Talent'},
#     {'Parameters': [{'PerkId': 'talent_sniper', 'NextPerkId': {}, 'Name': 'IWeaponDistance', 'ValType': 'Int', 'IntVal': '2'}, {'Name': 'IEnemyHuntBonus', 'ValType': 'Int', 'IntVal': '-2'}], 'AIParameters': [], 'LevelUpActionType': 'None', 'CurrentExp': '0', 'ExpPerAction': '0', 'MaxExp': '0', 'PerkType': 'Talent'},
#     {'Parameters': [{'PerkId': 'talent_strafe', 'NextPerkId': '', 'Name': 'BRunActions', 'ValType': 'Boolean', 'BoolVal': 'True'}, {'Name': 'FUsedApDodgeBonus', 'ValType': 'Float', 'FloatVal': '0.1'}], 'AIParameters': [], 'LevelUpActionType': 'None', 'CurrentExp': '0', 'ExpPerAction': '0', 'MaxExp': '0', 'PerkType': 'Talent'},
#     {'Parameters': [{'PerkId': 'talent_tactical_reload', 'NextPerkId': '', 'Name': 'IAddedProj', 'ValType': 'Int', 'IntVal': '1'}, {'Name': 'IConstReload', 'ValType': 'Int', 'IntVal': '1'}], 'AIParameters': [], 'LevelUpActionType': 'None', 'CurrentExp': '0', 'ExpPerAction': '0', 'MaxExp': '0', 'PerkType': 'Talent'},
#     {'Parameters': [{'PerkId': 'talent_thrift', 'NextPerkId': {}, 'Name': 'IAllConsumablesStack', 'ValType': 'Int', 'IntVal': '4'}, {'Name': 'FPhysicalResistsWeightModifier', 'ValType': 'Float', 'FloatVal': '0.4'}], 'AIParameters': [], 'LevelUpActionType': 'None', 'CurrentExp': '0', 'ExpPerAction': '0', 'MaxExp': '0', 'PerkType': 'Talent'},
# ]

# creature_datas = [
#     e['CreatureData']
#     for d in dat['Components']
#     if d['Type'] == 'MGSC.Mercenaries'
#     for e in d['Content']['Values']]
# # for creature_data in creature_datas:
# #     for key, value in creature_data.items():
# #         print(key, value, sep='\t')
# # FIXME: I AM NOT CONVINCED THIS IS ACTUALLY WORKING!
# for creature_data in creature_datas:
#     creature_data.update({
#         'BaseHealth': '200',        # health, higher is better
#         'MeleeDamage': {
#             'damage': 'blunt',  # normally always blunt
#             'minDmg': '9',      # normally 2-9
#             'maxDmg': '21',     # normally 10-21
#             'critChance': '0.08', # normally 0.04-0.08
#             'critDmg': '0.5'},    # normally 0.3-0.5
#         # crit chance
#         'BaseMeleeAccuracy': '0.5', # melee accuracy
#         'BaseRangeAccuracy': '0.5', # ranged accuracy
#         'BaseDodge': '0.36',        # dodge chance
#         'StarvationLimit': '3000',  # normally 1800-2400
#         'BaseLosLevel':	'12',            # Sight Range (normal range 10-10)
#         'PainThresholdBase': '16',  # normally 8-16
#         'PainThresholdLimit': '16', # normally 8-16
#         # 'PainThresholdRegen': '1',        # normally always 1
#         'AttackWoundChanceMult': '1.25', # inflict wound chance modifier
#         'ReceiveWoundChanceMult': '0.6', # receive wound chance modifier -- LOWER is better - normal range 0.6-1
#         'BaseActionPoints': '3',         # normal range 0-0
#         # 'BaseOverallDmgMult': '1',       # normal range 1-1
#         # 'BaseOverallDodgeMult': '1',     # normal range 1-1
#         # 'GrenadeDamageMult': '1',      # normal range 1-1
#         'CoverBlockChanceBonus': '15', # normal range 0-15
#         'CoverHitChanceBonus': '15',  # normal range 0-15
#         'IgnoreInfection': True,      # True is better
#         'IgnorePain': True,           # True is better
#         # 'IgnoreStarvation': True,     # normally always False
#         # 'LookAngle': '100',     # normally always 100 (increase this to 180 or 270???)
#         'WeaponDistanceBonus': '2', # normally 0-2, only vicky has this
        
#         })


if True:
    unlock_chips_quicklist = {
        'tia_chip': ['tia_disc_assault_1', 
                     'tia_shock_assault_1', # guess?
                     ],
        'sun_chip': ['sun_servo_backpack_1', 'sun_laser_powersword_1', 'sun_laser_marksman_1',],
        'low_chip': ['mre_pack_1', 'medical_kit_2', ],
        'chu_chip': ['chu_shotgun_1',],
        # 'she_chip': ['she_plasma_assault',],
        'medium_chip': ['rifle_basic_ammo', 'military_axe_1', 'military_minigun_1', 'military_assault_1', 'military_smg_1',],
        # armor unlocks in sets, so only need 1 of 4 a set named x_{helmet,armor,pants,boots}_y.
        'high_chip': ['automap',
                      'heavy_armored_vest_1',
                      'military_power_armor_1', # 'military_power_helmet_1', 'military_power_pants_1', 'military_power_boots_1'
                      'army_pistol_4', 'plasma_shotgun_2', 'army_sniper_2',],
        'rwa_chip': ['rwa_military_pistol_1', 'rwa_military_smg_1',
                     'rwa_power_armor_1', # 'rwa_power_helmet_1', 'rwa_power_pants_1', 'rwa_power_boots_1', # lv10, best anti-human
                     'rwa_heavy_armor_1', # 'rwa_heavy_helmet_1', 'rwa_heavy_pants_1', 'rwa_heavy_boots_1', # lv7, best anti-ssethtzentach
                     ],
        'dil_chip': ['dil_battery_ammo', 'dil_sound_assault_1', 'dil_sound_pistol_2', 'dil_chaos_smg_1', 'dil_shock_sniper_1',],
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
            'mirza_aishatu',
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
else:
    # Just edit the list of unlocked recipes directly.
    desirable_recipes = {
        "army_pistol_4",
        "automap",              # dataminer
        "dil_battery_ammo",
        "dil_chaos_smg_1",
        "dil_chaos_assault_1",
        "dil_sound_pistol_2",
        "dil_sound_assault_1",
        "dil_sound_shotgun_1",
        "fra_security_assault_1",
        "medical_kit_2",
        'heavy_armored_vest_1',   # panzer vest
        'military_axe_1',
        "military_armored_vest_1", # veteran vest
        "military_power_armor_1", # frame armor lv8
        "military_power_boots_1",
        "military_power_helmet_1",
        "military_power_pants_1",
        "mre_pack_1",           # best food?
        "plasma_shotgun_2",
        "rwa_heavy_armor_1",    # carnage armor lv7
        "rwa_heavy_boots_1",
        "rwa_heavy_helmet_1",
        "rwa_heavy_pants_1",
        "rwa_military_pistol_1",
        "rwa_military_smg_1",   # best smg?
        "rwa_power_armor_1",    # warlord armor lv10
        "rwa_power_boots_1",
        "rwa_power_helmet_1",
        "rwa_power_pants_1",
        "sbn_rail_assault_1",   # suppressed ammoless ~low-dam weapons
        "sbn_rail_pistol_1",
        "sbn_rail_shotgun_1",
        "sbn_rail_smg_1",
        'laser_sniper_1',
        'laser_smg_1',
        'chu_shotgun_1',          # best sg?
        "sun_laser_powersword_1", # best sword w/ammo
        "sun_servo_backpack_1", # best backpack
        "tia_disc_assault_1",
        "tia_shock_smg_1",      # guess
      }
    cargodict, = [
        d['Content']
        for d in dat['Components']
        if d['Type'] == 'MGSC.MagnumCargo']
    cargodict['UnlockedProductionItems'] = sorted(set(cargodict['UnlockedProductionItems']) | desirable_recipes)
    


armor_loadout = [
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
    },
*[{
              "Type": "MGSC.PickupItem",
              "Content": {
                "StackCount": "1",
                "_components": [
                  {
                    "Type": "MGSC.BreakableItemComponent",
                    "Content": {
                      "CurrentPercent": "1",
                      "MaxPenaltyPercent": "0",
                      "MaxDurability": '1000', # cheat
                      "MinDurabilityAfterRepair": "0",
                      "Unbreakable": "False"
                    }
                  }
                ],
                "Id": armor_id,
                "SingleWeight": "0.1", # cheat
                "InventoryWidthSize": "1",
                "ExaminedItem": "True",
                "LockCounter": "0",
                "IsUseRestricted": "False",
                "InventoryPos": "0 0"
              }
            }
  for armor_id in [
          # As at 1.x, rwa_heavy is STRICTLY WORSE than rwa_power.
          # 'rwa_heavy_armor_1', 'rwa_heavy_helmet_1', 'rwa_heavy_pants_1', 'rwa_heavy_boots_1', # lv7, best anti-ssethtzentach
          'military_power_armor_1', 'military_power_helmet_1', 'military_power_pants_1', 'military_power_boots_1', # lv8 frame armor
          'rwa_power_armor_1', 'rwa_power_helmet_1', 'rwa_power_pants_1', 'rwa_power_boots_1', # lv10, best anti-human
  ]],
]

# Add top-tier gear to the Ship Cargo list.
# We'll put everything in grid position 0 0.
# This makes it not directly accessible, but you
# can just hit the sort button to get it all repositioned neatly afterwards.
# /Components/*[@Type="MGSC.MagnumCargo"]/ShipCargo[0]/Items
# THIS IS WORKING, yay.
ship_cargos = [
    e['Items']
    for d in dat['Components']
    if d['Type'] == 'MGSC.MagnumCargo'
    for e in d['Content']['ShipCargo']]
ship_cargos[0] += [
    x
    for x in armor_loadout
    for _ in range(17)          # 17 clones (excl. Big Boss)
]

# Weapons are more complicated because they have inline stats.
# It might be better to craft them...
example_weapons = [
    {
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
                    "Type": "MGSC.WeaponComponent",
                    "Content": {
                        "InstanceId": "32f327b5-636d-4691-a73e-f257bda5f2a4",
                        "CurrentAmmo": "21",
                        "LastReloadAmount": "0",
                        "Traits": [
                            {
                                "Parameters": [
                                    {
                                        "Name": "BSuppressor",
                                        "ValType": "Boolean",
                                        "BoolVal": "True"
                                    }
                                ],
                                "TraitId": "suppressor",
                                "ItemTraitType": "WeaponTrait",
                                "TraitContext": "Passive"
                            },
                            {
                                "Parameters": [
                                    {
                                        "Name": "FPierce",
                                        "ValType": "Float",
                                        "FloatVal": "0.7"
                                    }
                                ],
                                "TraitId": "piercing",
                                "ItemTraitType": "WeaponTrait",
                                "TraitContext": "Passive"
                            }
                        ],
                        "_weaponId": "sbn_rail_pistol_1",
                        "_currentAmmoId": "implicted_em_ammo",
                        "_currentFireModeId": "rifle_1"
                    }
                }
            ],
            "Id": "sbn_rail_pistol_1",
            "SingleWeight": "1.52",
            "InventoryWidthSize": "2",
            "ExaminedItem": "True",
            "LockCounter": "0",
            "IsUseRestricted": "False",
            "InventoryPos": "0 21"
        }
    },
]

# Go through ALL the existing weapons/armor in the cargo hold and set their weight to 0.1kg?

# Add to cargo hold all the items necessary to fully upgrade all ship tech trees?
if True:
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
                
        }
    ]


# import pprint
# pprint.pprint(mercenaries)

# pprint.pprint(dat)


# UPDATE: when you modify an item it changes from
#         "rwa_power_helmet_1" to
#         "rwa_power_helmet_1_custom".
#         Any items you already had DON'T get upgraded.
#         You MUST unlock the ship's upgrade station, THEN
#         upgrade the item, THEN
#         make the armour/weapon item in the ship's factory station.
#         Then for the actual stat changes you have something like this in MGSC.MagnumProjects:
#         

{
    "ProjectType": "Helmet",
    "DevelopId": "rwa_power_helmet_1",
    "StartTime": "694339524866210000",
    "FinishTime": "694342084866210000",
    "IsInDevelopment": "False",
    "ModificationsCount": "40",
    "UpcomingModificationsCount": "0",
    "ModifyStartPrice": "13",
    "AppliedModifications": [
        {
            "Key": "helmet_resist_blunt",
            "Value": "80"
        },
        {
            "Key": "helmet_resist_fire",
            "Value": "80"
        },
        {
            "Key": "helmet_resist_pierce",
            "Value": "80"
        },
        {
            "Key": "helmet_resist_cold",
            "Value": "80"
        },
        {
            "Key": "helmet_resist_lacer",
            "Value": "80"
        },
        {
            "Key": "helmet_resist_shock",
            "Value": "80"
        },
        {
            "Key": "helmet_resist_beam",
            "Value": "80"
        },
        {
            "Key": "helmet_resist_poison",
            "Value": "80"
        }
    ],
    "UpcomingModifications": [],
    "CachedItems": [
        # The things you spent on the upgrades end up here.
        # This is only so you get them back if you cancel it while it's in progress.
    ]
}

dst_path.write_text(json.dumps(dat, indent=2))
