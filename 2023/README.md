# 2023

## Thoughts

### Day 1

Part A was fine, but part B caught me off guard. The solution I came up with in the moment was
extrmeley brute-force; I essentially duplicated the logic for finding the first and last digits from
part A and applied it to the English representations. Then, I compared to see which one came
first/last: digit or English representation. After solving it and discussing with a friend, we
realized that the trick was to first do a clever string replacement to essentially replace each
English represntation with the digit itself; it needs to be clever to account for potential cases
where two English representations share a letter, e.g. `eightwo`. Once the replacement was done,
the problem boiled down to solving part A again.

### Day 2

Pretty straightforward! The only hiccup I experienced was the parsing step. Ultimately it wasn't
difficult, but I'm a bit rusty with AoC-input parsing, so this problem was a good warmup.

### Day 3

I thought this was quite a difficult problem for Day 3. A grid-based problem on Day 3, along with
caveat that not every element in the grid is the same size. Sure, digits and symbols are all one
character long, but adjacent digits needed to be understood as a larger number that took up multiple
adjacent spots in the grid. 

This was probably the first time I've ever reached for regex to solve a problem, ever. I'm pretty
happy that the regex itself wasn't difficult, but even then, I needed to pull up a regex checker
online to figure out the correct regex.

The solution I came up with on the spot was extremely janky. For some reason, I was convinced that I
needed to do adjacency checks case by case, i.e., above, below, corners, left, right. This ended up
bloating my code up to approximately 150 lines just for visiting neighbors in the grid...

My cleaned up version, though probably not the most clean, is much nicer in comparison. The biggest
change was doing the adjacency checks with a single nested for loop over the window (bounding box)
of the region around each number.
