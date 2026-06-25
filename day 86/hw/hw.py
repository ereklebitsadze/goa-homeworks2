# დავალება 5: დამხმარე ფუნქციების შექმნა utils მოდულში
def show_message(message):
    print(f"[GAME LOG]: {message}")

def show_combat_log(attacker, target, damage):
    print(f"⚔️ {attacker} თავს დაესხა პერსონაჟს {target} და მიაყენა {damage} ზიანი!")






# დავალება 7: Player კლასი გადატანილია models/player.py-ში

class Player:
    def __init__(self, name, damage=20):
        self.name = name
        self.health = 100  # დავალება 1: health ატრიბუტის დამატება (საწყისი 100)
        self.damage = damage  # დავალება 3: damage ატრიბუტის დამატება

    # დავალება 3: attack მეთოდი, რომელიც აკლებს სიცოცხლეს მოწინააღმდეგეს
    def attack(self, enemy):
        enemy.health -= self.damage

    # დავალება 4: walk მეთოდის ბაზისური ვერსია
    def walk(self):
        print("Player is walking")




# დავალება 7: Enemy კლასი გადატანილია models/enemy.py-ში
from models.player import Player

# დავალება 2: Enemy კლასი მემკვიდრეობს Player კლასს
class Enemy(Player):
    def __init__(self, name, damage=15):
        # super() ავტომატურად გადასცემს მშობლის ატრიბუტებს (მათ შორის health=100-ს)
        super().__init__(name, damage) 

    # დავალება 4: პოლიმორფიზმი (Method Overriding)
    # შენიშვნა: ჭეშმარიტი პოლიმორფიზმისთვის მეთოდს უნდა ერქვას ზუსტად იგივე 'walk'
    def walk(self):
        print("Enemy is walking stealthily")
        
    # თუ ტასკის პირობას ზუსტად მივყვებით მეთოდის სახელზე:
    def EnemyWalk(self):
        print("Enemy is walking stealthily")


# დავალება 8: მოთამაშის სტატუსის დამბეჭდავი ფუნქცია
def display_player(player):
    print("\n=== 📊 პერსონაჟის სტატუსი ===")
    print(f"სახელი: {player.name}")
    print(f"სიცოცხლე (Health): {player.health}")
    print(f"ძალა (Damage): {player.damage}")
    print("============================\n")






# დავალება 9: ბაზისური კონტროლერი (იგულისხმება, რომ არსებობდა)
class MainController:
    def __init__(self):
        self.is_active = False

# GameController, რომელიც მემკვიდრეობს MainController-ს
class GameController(MainController):
    def __init__(self):
        super().__init__()

    # თამაშის დაწყების ახალი მეთოდი
    def start_game(self):
        self.is_active = True
        print("🎮 თამაში წარმატებით დაიწყო GameController-ის მიერ!")







# დავალება 10: ყველა საჭირო ახალი მოდულის იმპორტი
from models.player import Player
from models.enemy import Enemy
from views.views import display_player
from utils.utils import show_message, show_combat_log
from controller import GameController

def main():
    # დავალება 10: თამაშის ინიციალიზაცია და დაწყება GameController-ით
    game = GameController()
    game.start_game()

    # დავალება 6: utils.py-დან იმპორტირებული ფუნქციის გამოყენება
    show_message("სისტემა ამზადებს პერსონაჟებს...")

    # ობიექტების (Instances) შექმნა
    hero = Player("KingArthur", damage=25)
    villain = Enemy("DarkKnight", damage=10)

    # დავალება 8: საწყისი სტატუსის ჩვენება views-ს გამოყენებით
    display_player(hero)
    display_player(villain)

    # დავალება 4: პოლიმორფიზმის დემონსტრირება (ორივე ერთსა და იმავე ქცევას სხვადასხვანაირად აკეთებს)
    hero.walk()
    villain.walk()  # გამოიძახებს გადაწერილ ვერსიას

    # დავალება 3: ბრძოლის იმიტაცია (Attack მეთოდი)
    hero.attack(villain)
    
    # დავალება 6-ის ფარგლებში ლოგირების utils-ის გამოყენება
    show_combat_log(hero.name, villain.name, hero.damage)
    
    # განახლებული სტატუსის ჩვენება
    display_player(villain)

if __name__ == "__main__":
    main()