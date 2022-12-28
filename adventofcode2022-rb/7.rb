require 'dotenv'
require 'http'

day = 7

Dotenv.load("../.env")
input = HTTP.cookies(:session => ENV['AOC_SESSION']).get("https://adventofcode.com/2022/day/#{day}/input").to_s.split("\n")

# input = ["$ cd /",
# "$ ls",
# "dir a",
# "14848514 b.txt",
# "8504156 c.dat",
# "dir d",
# "$ cd a",
# "$ ls",
# "dir e",
# "29116 f",
# "2557 g",
# "62596 h.lst",
# "$ cd e",
# "$ ls",
# "584 i",
# "$ cd ..",
# "$ cd ..",
# "$ cd d",
# "$ ls",
# "4060174 j",
# "8033020 d.log",
# "5626152 d.ext",
# "7214296 k"]

stack = []
directory = {
  # path => size
  # "path/to/filename" => 12345
  # "path/to/directory" => nil???
}


input.each do |line|
  args = line.split ' '
  if args[0] == "$"

    if args[1] == "cd"
      if args[2] == ".."
        stack.pop
      else
        stack.push args[2]
      end
    end

  else
    if args[0] != 'dir'
      size, filename = args[0], args[1]
      (0...stack.length).each do |idx|
        path = stack[0..idx].join('/')
        if !directory.has_key? path
          directory[path] = 0
        end
        directory[path] += size.to_i
      end
    end
  end
end
puts directory

cap = 100000
sum = 0

directory.each do |path, size|
  if size < cap
    sum += size
  end
end

p sum

# part 2
required_free_space = 30000000
total_disk_space = 70000000
current_free_space = total_disk_space - directory["/"]
need_to_reclaim = required_free_space - current_free_space
puts "#{need_to_reclaim} = #{required_free_space} - #{current_free_space}"

candidates = directory.filter {|path, size| size > need_to_reclaim }
candidate_size = candidates.values.sort.first
p candidate_size