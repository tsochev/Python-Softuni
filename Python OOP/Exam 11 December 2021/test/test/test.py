from unittest import TestCase, main

from project.team import Team


class TeamTests(TestCase):
    def setUp(self):
        self.team = Team("Team")

    def test_init__when_works_properly(self):
        self.assertEqual("Team", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_validation__expect_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "4"

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_member__when_adding(self):
        self.team.add_member(Ivan=12)
        self.team.add_member(Petar=12)
        self.team.add_member(Stoqn=12)

        self.assertEqual({"Ivan": 12, "Petar":12, "Stoqn":12}, self.team.members)

    def test_add_member__expect_string(self):
        self.assertEqual(f"Successfully added: Ivan, Petar, Stoqn", self.team.add_member(Ivan=12, Petar=12, Stoqn=12))

    def test_remove_member__when_is_removed(self):
        name = "Ivan"
        self.team.add_member(Ivan=12)

        self.assertEqual(f"Member Ivan removed", self.team.remove_member(name))

    def test_remove_member__when_name_not_exist(self):
        name = "Stoqn"
        self.team.add_member(Ivan=12)

        self.assertEqual(f"Member with name {name} does not exist", self.team.remove_member(name))

    def test_greater_than__when_true_if_len_is_bigger_else_false(self):
        t1 = Team("One")
        t2 = Team("Two")
        t1.add_member(Ivan=24, Stoqn=25)
        self.assertTrue(t1 > t2)
        self.assertEqual(True, t1 > t2)
        self.assertFalse(t2 > t1)

    def test_len_method__when_return_correct_result(self):
        self.team.add_member(Ivan=24, Stoqn=25)
        self.assertEqual(2, self.team.__len__())

    def test_add_method__when_create_new_team_name_and_add_members(self):
        t1 = Team("One")
        t2 = Team("Two")
        t1.add_member(Ivan=24, Stoqn=25)
        t2.add_member(Petar=25, Vasko=23)
        test = t1 + t2
        self.assertEqual("OneTwo", test.name)
        self.assertEqual({"Ivan": 24, "Stoqn":25, "Petar":25, "Vasko":23}, test.members)

    def test_str_method(self):
        t1 = Team("One")
        t2 = Team("Two")
        t1.add_member(Ivan=24)
        t2.add_member(Petar=25)
        test = t1 + t2
        expected = "Team name: OneTwo\nMember: Petar - 25-years old\nMember: Ivan - 24-years old"
        self.assertEqual(expected, str(test))


if __name__ == "__main__":
    main()