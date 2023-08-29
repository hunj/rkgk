require 'dotenv'
require 'http'
require 'set'

day = 6

Dotenv.load("../.env")
input = HTTP.cookies(:session => ENV['AOC_SESSION']).get("https://adventofcode.com/2022/day/#{day}/input").to_s.split("\n").first

(0..input.length-3).each { |idx|
  past_four_letters = input[idx..idx+13].chars.to_set
  # if past_four_letters.length == 4
  if past_four_letters.length == 14
    p idx+14
    break
  end
}