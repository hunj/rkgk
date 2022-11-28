
class TicTacToe
  def initialize()
    @board = [
      [nil, nil, nil],
      [nil, nil, nil],
      [nil, nil, nil]
    ]
  end

  def print_board
    puts "┌-┬-┬-┐"
    @board.each_with_index do |row, row_idx| 
      print "|"
      row.each_with_index do |col, col_idx| 
        self.print_block col
        print "|"
      end

      print "\n"
      puts "├-┼-┼-┤" if row_idx < 2
    end
    puts "└-┴-┴-┘"
  end

  def print_block i
    if i.nil?
      print " "
    else
      print i
    end
  end

  def turn player
  end

  def mark player, x, y
  end
  
  def win_condition? player
  end
end

t = TicTacToe.new()

t.print_board
