require 'dotenv'
require 'http'

Dotenv.load("../.env")
input = HTTP.cookies(:session => ENV['AOC_SESSION']).get("https://adventofcode.com/2022/day/2/input").to_s.split("\n")

# here we go

results = {
  "A" => {
    "X" => 1 + 3,
    "Y" => 2 + 6,
    "Z" => 3 + 0
  },
  "B" => {
    "X" => 1 + 0,
    "Y" => 2 + 3,
    "Z" => 3 + 6
  },
  "C" => {
    "X" => 1 + 6,
    "Y" => 2 + 0,
    "Z" => 3 + 3
  }
}

score = 0

input.each do |line|  # line looks like "A C"
  score += results[line[0]][line[2]]
end

p score

# 2nd half

score = 0

rounds = {
  "A" => {
    "X" => 0 + 3,
    "Y" => 3 + 1,
    "Z" => 6 + 2
  },
  "B" => {
    "X" => 0 + 1,
    "Y" => 3 + 2,
    "Z" => 6 + 3
  },
  "C" => {
    "X" => 0 + 2,
    "Y" => 3 + 3,
    "Z" => 6 + 1
  }
}

input.each do |line|
  score += rounds[line[0]][line[2]]
end

p score
