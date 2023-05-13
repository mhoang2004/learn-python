class User:
    active_users = 0

    @classmethod
    def display_active_user(cls):
        return f"There are currently {cls.active_users} active users"

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1


class Moderator(User):
    total_mods = 0

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1

    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.total_mods} active users"


u1 = User("Hoa", "Long", 12)
u1 = User("Hoa", "Long", 12)
u1 = User("Hoa", "Long", 12)
m1 = Moderator("Ki", "Hao", 33, "football")
m1 = Moderator("Ki", "Hao", 33, "football")

print(User.display_active_user())
print(Moderator.display_active_mods())
