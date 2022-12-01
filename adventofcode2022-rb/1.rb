require 'dotenv'
require 'http'

Dotenv.load("../.env")
input = HTTP.cookies(:session => ENV['AOC_SESSION']).get("https://adventofcode.com/2022/day/1/input").to_s

# here we go

calories = []

count = 0
input.each_line do |line|
  if line == "\n"  # god damnit
    calories << count
    count = 0
  else
    count += line.to_i
  end
end

max_cal = 0
calories.each_with_index do |cal|
  if cal > max_cal
    max_cal = cal
  end
end

puts max_cal

calories.sort!.reverse!  # i ain't reinventing the wheel

puts calories[0, 3].reduce(:+)
