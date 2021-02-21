class Inventory:

    '''
        Types of items:

        1. Specialized weapons: Items that can only be accessed when playing against certain enemies
        [Work for 5 enemy turns and can be purchased 2 times]
            Spiked armour: Makes the Warrior take 10 damage when they throw a physical attack
                - You won't receive damage from the hits; only the Warrior will
            Ninja mist: Hides your movement from the Trickster
                - They'll perceive your movement as a retreat so they'll attack (w/ less damage than you)
            Cursed sabotage: Makes it so that the Wizard takes 20 damage for using magic
                - This includes; magic attacks (potions & spells), magic defense (shield), normal defense,
                  and strong attacks (everything but normal 7 damage attacks)
                - They can still use magic, but it'll be detrimental for them

        2. General tools: Items that can be accessed during any battle
            Protein drink: Increases energy to 100%
                - One-time occurrence; 2 available
            Enchanted sword: Increases damage to x2 (+ has a unique attack description!)
                - Applicable for 3 turns; 2 available
            Force field: Increases shield by 50
                - One-time occurrence; 2 available
            Bandages: Increases health by 20
                - One-time occurrence; 2 available

    '''

    def __init__(self):
        print()