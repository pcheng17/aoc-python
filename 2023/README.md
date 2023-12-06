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
the caveat that not every element in the grid is the same size. Sure, digits and symbols are all one
character long, but adjacent digits needed to be understood as a larger number that took up multiple
adjacent spots in the grid. 

This was probably the first time I've ever reached for regex to solve a problem, ever. I was pretty
relieved that the regex itself wasn't difficult, but even then, I needed to pull up a regex checker
online to figure out the correct regex.

The solution I came up with on the spot was extremely janky. For some reason, I was convinced that I
needed to do adjacency checks case by case, i.e., above, below, corners, left, right. This ended up
bloating my code up to approximately 150 lines just for visiting neighbors in the grid...

My cleaned up version, though probably not the most clean, is much nicer in comparison. The biggest
change was doing the adjacency checks with a single nested for loop over the window (bounding box)
of the region around each number.

Thanks to people online, I was reminded of `defaultdict` from `collections`. It's a dictionary that
allows you to specify the default value for a key that doesn't exist.

### Day 4

This was much easier than Day 3, which was a relief. I made a silly mistake that I accidentally
fixed with an extra cast to `int`. My formula for computing the number of points from a card was 
`2 ** (len(matches) - 1)`, which is only correct if the number of matches is nonzero! Coincidentally, using the formula `int(2 ** (len(matches) - 1))` saved me because this new formula returns 0 if there are no matches. Dumb, but I admit I overlooked this edge case.

Part B was pretty straightforward, but only after stopping to read the instructions more carefully.
I don't know, something about the problem setup made it difficult for me to figure out how the game
was changed.

I got to use `defaultdict` for this one, which was an opportunity to practice something I learned about yesterday. Turns out, one way of specifying that you want a dict where the default value is 0 is `defaultdict(lambda: 0)`.

### Day 5

Part A was pretty straightforward. However, it did take me a bit to figure out how I wanted to parse
and organize the data. I ended up going down a few rabbit holes where I overcomplicated my solution,
and had to backtrack. I find that this is more likely to happen when I try to define multiple
functions to solve my problem as opposed to just throwing everything into one main function; the
latter is definitely better (for me) for the purpose of solving these types of problems quickly.

Part B was difficult for me. I naively decided to just duplicate the logic of Part A to run it per
seed in all of the ranges, which was definitely not the right thing to do because I had
approximately 2.3 billion seeds. After chatting with a friend for probably 30 minutes, I was
more and more convinced that we had to operate on ranges as opposed on seed values, but coming up
with the logic to evaluate on ranges was not easy for me. The trick was to draw pictures. I should
know this by now... draw pictures sooner rather than later because they're really helpful!

A few hours later: although I got the right answer, my solution was not correct! I completely
overlooked the case where a map doesn't contain the range for an input, in which case the input is
left unchanged, i.e., the identity map. This means that the answer to my particular input doesn't
require that part of the definition of the mappings. After discovering this, I was unsatisfied with
my solution, so I tried to include the identity map case in my implementation. However, this seemed like a lot of extra nuanced logic which I wasn't sure how to write without first introducing some extra tooling, so I ultimately went with a different approach which I learned about after browsing Reddit.

Instead of evaluating the maps in a forward direction to figure out the minimum output, evaluate the inverse of the maps to determine what is the smallest output that has an inverse that
falls within a seed range. The code for this is pretty straightforward, and it produces the same
answer that is accepted by AoC for my input. On my M1 Mac, it takes a little over 6 min to evaluate
this version; not bad considering it's written in Python. Anyway, I'm now very curious what the
intended solution is.

### Day 6

What a change in pace compared to Day 5. Brute force for this problem is good enough.
