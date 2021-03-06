"""
* aoc2021 - Day 1
* https://adventofcode.com/2021/day/1
"""

DAY = 'day1'

def get_puzzle_input(day, input_directory="../input"):
  """
  Return an array containing all the lines of ../input/${day}.txt
  """
  with open(f"{input_directory}/{day}.txt", "r", encoding="UTF-8") as input_file:
    return input_file.read().splitlines()


def part1(puzzle_input):
  """
  Day 01, Part 1
  """

  measurements = [int(line) for line in puzzle_input]
  nb_measurements = len(puzzle_input)

  def depth_increase(index):
    """
    Is the depth of the next measurement higher than the depth of the current measurement ?
    """
    try:
      return measurements[index + 1] > measurements[index]
    except IndexError:
      return False

  return sum(1 if depth_increase(index) else 0 for index in range(nb_measurements))

def part2(puzzle_input):
  """
  Day 01, Part 2
  """

  measurements = [int(line) for line in puzzle_input]
  nb_measurements = len(puzzle_input)

  def depth_increase(index):
    """
    With window size: 3:
    Is the depth of the next window higher than the depth of the current window ?
    """
    try:
      current_window_depth = measurements[index] + measurements[index + 1] + measurements[index + 2]
      next_window_depth = measurements[index + 1] + measurements[index + 2] + measurements[index + 3]
      return next_window_depth > current_window_depth
    except IndexError:
      return False

  return sum(1 if depth_increase(index) else 0 for index in range(nb_measurements))


print(part1(get_puzzle_input(DAY)))
print(part2(get_puzzle_input(DAY)))
