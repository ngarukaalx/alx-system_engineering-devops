#!/usr/bin/env ruby
#  match a 10 digit phone number
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flag:(.*?)\]\/).join(",")
