require 'dotenv'
require 'http'

day = 4

Dotenv.load("../.env")
input = HTTP.cookies(:session => ENV['AOC_SESSION']).get("https://adventofcode.com/2022/day/#{day}/input").to_s.split("\n")

count = 0

input.each do |line|
  assignments = line.split ','
  first = assignments[0].split('-').map(&:to_i)
  second = assignments[1].split('-').map(&:to_i)

  # swap first & second to make sure `first` starts first
  if first[0] >= second[0] &&
      first[1] - first[0] <= second[1] - second[0]
    first, second = second, first
  end

  # uncomment for part 1
  # if first[0] <= second[0] && 
  #     first[1] >= second[1]
  #   count += 1
  #   p count
  # end
  # if first[1] >= second[0] && first[0] <= second[0]
  # if first[0] <= second[0] && first[1] ?? second[1]


  # fuck numbers we goin set theory
  first_set = (first[0]..first[1]).to_a.to_set
  second_set = (second[0]..second[1]).to_a.to_set

  p first_set, second_set
  if first_set.intersect? second_set
    count += 1
    p count
  end
  
  p '---'
end

'''
.234.....  2-4   no
.....678.  6-8

.23......  2-3   no
...45....  4-5

....567..  5-7
......789  7-9   ok (7)

.2345678.  2-8   ok (34567)
..34567..  3-7

.....6...  6-6   |
...456...  4-6   V

...456...  4-6
.....6...  6-6   ok (6)

.23456...  2-6
...45678.  4-8   ok (456)
'''
