from color_code_test import test_number_to_pair, test_pair_to_number
from print_color_code import print_color_coding_manual
if __name__ == '__main__':
  test_number_to_pair(4, 'White', 'Brown')
  test_number_to_pair(5, 'White', 'Slate')
  test_pair_to_number('Black', 'Orange', 12)
  test_pair_to_number('Violet', 'Slate', 25)
  test_pair_to_number('Red', 'Orange', 7)
  print('Done :)')

print_color_coding_manual()
