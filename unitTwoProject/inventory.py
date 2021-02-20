class Inventory:

    '''
        Types of items:

        1. Specialized weapons: Items that can only be accessed when playing against certain enemies
        [Work for 5 enemy turns and can be purchased 2 times]
            Spiked armour: Makes the Warrior take 10 damage when they throw a physical attack
                - You won't receive damage from the hits; only the Warrior will
            Ninja mist: Hides your movement from the Trickster
                - They'll perceive your movement as a retreat so they'll attack (w/ less damage than you)
            Cursed sabotage: Makes it so that the Wizard takes 10 damage for using magic
                - This includes; magic attacks (potions & spells), magic defense (shield), normal defense,
                  and strong attacks (everything but normal 7 damage attacks)
                - They can still use magic, but it'll be detrimental for them

        2. General weapons: Items that can be accessed during any battle
        [Work for 2 turns and can be purchased 3 times]
            ADD ITEMS

        3. Defensive tools: Items that can be used to replenish health/energy, add shield, or increase damage
        [One-time purchase & occurrence OR lasts for the rest of the battle (for damage)]
            ADD ITEMS

    '''

    def __init__(self):
        print()