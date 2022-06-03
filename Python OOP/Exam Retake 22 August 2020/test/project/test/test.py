from unittest import TestCase, main

from project.student_report_card import StudentReportCard


class StudentReportCardTests(TestCase):
    def setUp(self):
        self.src = StudentReportCard("Ivan", 12)

    def test_initialization__when_is_correct(self):
        self.assertEqual("Ivan", self.src.student_name)
        self.assertEqual(12, self.src.school_year)
        self.assertEqual({}, self.src.grades_by_subject)

    def test_init_student_name__when_is_invalid__expect_raise(self):
        with self.assertRaises(ValueError) as ct:
            self.src.student_name = ""

        self.assertEqual("Student Name cannot be an empty string!", str(ct.exception))

    def test_init_student_name__when_is_valid(self):
        self.src.student_name = "Gosho"

        self.assertEqual("Gosho", self.src.student_name)

    def test_init_school_year__when_below_1__expect_raise(self):
        with self.assertRaises(ValueError) as ct:
            self.src.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(ct.exception))

    def test_init_school_year__when_is_1__expect_correct_result(self):
        self.src.school_year = 1
        self.assertEqual(1, self.src.school_year)

    def test_init_school_year__when_is_12__expect_correct_result(self):
        self.src.school_year = 12
        self.assertEqual(12, self.src.school_year)

    def test_init_school_year__when_over_12__expect_raise(self):
        with self.assertRaises(ValueError) as ct:
            self.src.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(ct.exception))

    def test_init_school_year__expect_correct_result(self):
        self.src.school_year = 5
        self.assertEqual(5, self.src.school_year)

    def test_add_grade__when_subject_does_not_exist(self):
        self.src.add_grade("Math", 4)
        self.src.add_grade("Physic", 5)
        self.assertEqual([4], self.src.grades_by_subject["Math"])
        self.assertEqual([5], self.src.grades_by_subject["Physic"])

    def test_add_grade__when_subject_add_grades(self):
        self.src.add_grade("Math", 4)
        self.src.add_grade("Math", 5)
        self.assertEqual([4, 5], self.src.grades_by_subject["Math"])

    def test_average_grade_by_subject__expect_correct_result(self):
        self.assertEqual("", self.src.average_grade_by_subject())
        self.src.add_grade("Math", 4)
        self.src.add_grade("Math", 5)
        self.assertEqual("Math: 4.50", self.src.average_grade_by_subject())

    def test_average_grade_for_all_subjects__expect_correct_result(self):
        self.src.add_grade("Math", 4)
        self.src.add_grade("Math", 5)
        self.src.add_grade("Test", 3)
        self.src.add_grade("Test", 4)
        self.assertEqual("Average Grade: 4.00", self.src.average_grade_for_all_subjects())

    def test_repr__expect_correct_result(self):
        self.src.add_grade("Math", 4)
        self.src.add_grade("Math", 5)
        self.src.add_grade("Test", 3)
        self.src.add_grade("Test", 4)
        self.assertEqual("""Name: Ivan
Year: 12
----------
Math: 4.50
Test: 3.50
----------
Average Grade: 4.00""", repr(self.src))


if __name__ == "__main__":
    main()
