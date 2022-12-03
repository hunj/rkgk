require 'dotenv'
require 'http'

day = 3

Dotenv.load("../.env")
input = HTTP.cookies(:session => ENV['AOC_SESSION']).get("https://adventofcode.com/2022/day/#{day}/input").to_s.split("\n")

# here we go

# im not hardcoding an array containing a-zA-Z
# am too lazy for that shit

priority = "a".upto("z").to_a.concat("A".upto("Z").to_a)

sum = 0
input.each do |line|
  first = line[0, line.length/2].chars
  second = line[line.length/2, line.length].chars
  common = first.intersection second
  common_char = common.join ''
  sum += priority.index(common_char) + 1
end

p sum

# second part

sum = 0

input.each_slice 3 do |slice|
  common = slice[0].chars.intersection(slice[1].chars.intersection(slice[2].chars))
  common_char = common.join ''
  sum += priority.index(common_char) + 1
end

p sum
