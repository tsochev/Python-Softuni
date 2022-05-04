from unittest import TestCase, main

from worker import Worker


class WorkerTests(TestCase):
    valid_name = "Worker"
    valid_salary = 1000
    valid_energy = 5

    def test_init__when_valid_name_salary_energy__expect_correct_init(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)

        self.assertEqual(self.valid_name, worker.name)
        self.assertEqual(self.valid_salary, worker.salary)
        self.assertEqual(self.valid_energy, worker.energy)

    def test__rest__when_valid__expect_energy_to_be_incremented(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.rest()

        self.assertEqual(self.valid_energy + 1, worker.energy)

    def test_work__when_energy_is_0__expect_raise(self):
        worker = Worker(self.valid_name, self.valid_salary, 0)
        with self.assertRaises(Exception) as context:
            worker.work()

        self.assertEqual('Not enough energy.', str(context.exception))

    def test_work__when_energy_is_negative__expect_raise(self):
        worker = Worker(self.valid_name, self.valid_salary, -1)
        with self.assertRaises(Exception) as context:
            worker.work()

        self.assertEqual('Not enough energy.', str(context.exception))

    def test_work__when_energy_is_positive__expect_increase_money_and_decrease_energy(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.work()

        self.assertEqual(self.valid_salary, worker.money)
        self.assertEqual(self.valid_energy - 1, worker.energy)

    def test_get_info__when_valid_name_salary_energy__expect_correct_result(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)

        expected = f'{self.valid_name} has saved 0 money.'
        actual = worker.get_info()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
