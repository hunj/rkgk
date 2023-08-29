require 'dotenv'
require 'http'

day = 5

Dotenv.load("../.env")
input = HTTP.cookies(:session => ENV['AOC_SESSION']).get("https://adventofcode.com/2022/day/#{day}/input").to_s.split("\n")

"""
[T]     [D]         [L]            
[R]     [S] [G]     [P]         [H]
[G]     [H] [W]     [R] [L]     [P]
[W]     [G] [F] [H] [S] [M]     [L]
[Q]     [V] [B] [J] [H] [N] [R] [N]
[M] [R] [R] [P] [M] [T] [H] [Q] [C]
[F] [F] [Z] [H] [S] [Z] [T] [D] [S]
[P] [H] [P] [Q] [P] [M] [P] [F] [D]
 1   2   3   4   5   6   7   8   9 
"""

stacks = {
  1 => %w(P F M Q W G R T),
  2 => %w(H F R),
  3 => %w(P Z R V G H S D),
  4 => %w(Q H P B F W G),
  5 => %w(P S M J H),
  6 => %w(M Z T H S R P L),
  7 => %w(P T H N M L),
  8 => %w(F D Q R),
  9 => %w(D S C N L P H)
}

instruction_regex = /^move (\d+) from (\d+) to (\d+)$/

input.each do |line|
  instruction = instruction_regex.match line
  if instruction
    count = instruction[1].to_i
    from = instruction[2].to_i
    to = instruction[3].to_i

    # uncomment for part 1
    # count.times do |c|
    #   if stacks[from].empty?
    #     break
    #   else
    #     temp = stacks[from].pop
    #     stacks[to].push temp
    #   end
    # end

    temp = stacks[from].pop count
    stacks[to].push temp
    stacks[to].flatten!

  end
end

stacks.each do |idx, stack|
  puts "#{idx} #{stack}"
end


