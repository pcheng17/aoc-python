# 2023

## Thoughts

### Day 1

Part A was fine, but part B caught me off guard. The solution I came up with in the moment was
extremely brute-force; I essentially duplicated the logic for finding the first and last digits from part A and applied it to the English representations. Then, I compared to see which one came
first/last: digit or English representation. After solving it and discussing with a friend, we
realized that the trick was to first do a clever string replacement to essentially replace each
English representation with the digit itself; it needs to be clever to account for potential cases
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

What a change of pace compared to Day 5. Brute force for this problem was good enough.

### Day 7

The problem itself was pretty straightfoward, just a bit of busy work to implement the comparisons
properly. I realized that I could uniquely encode each type of hand into a tuple: 
`(max card count, number of unique cards)`, and these tuples were well-ordered with respect to the
rankings of the hands. I thought this was a neat observation.

I completely tripped up on Part B though. In order to implement the "upgrade" mechanic to figure out
the best possible hand given that J is wild, I brute forced each of the different cases: if there
are 5 Js, 4 Js, 3 Js, etc. This worked out well except for one case. If there is only 1 J, then the
rest of the cards in your hand can look like this, for example: AAQQ, or AAAQ. If it's the former,
then, J can either be Q or A to produce a full house, but in the latter, J should be A to produce a
four-of-a-kind. I missed this subtlety, even though this case (the case with 1 J) was the hardest
for me to pin down. That should've been a hint to me to slow down and be careful.

I eventually discovered this bug by scanning the sorting of the hands of my input one by one until I
noticed something wrong. I also cooked up an example for my friend and me to run for me to compare.
Had to really roll up my sleeves for this one...

I learned a few things by looking at other peoples' solutions:

- `translate` and `str.maketrans` are pretty neat. `translate` allows you to do
  replacements of multiple different letters at once (instead of having to call `replace` multiple
  times), and `str.maketrans` is responsible for creating the translation table. For example, the
  following snippet translates `He bob` to `Hi mom`.

  ```python
  text = 'He bob'
  text = test.translate(str.maketrans('eb', 'im'))
  print(text) # 'Hi mom'
  ```
- The characters of this string, `23456789ABCDE`, are ordered. Thus, at least for part A, one
  could've translated `TQJKA` to `ABCDE`, and each hand would've been trivially comparable as
  strings when trying to break ties between hands of the same type.
 
### Day 8

Not bad! Part A was super straightforward: create a dictionary of the network, and then
walk it until we get to the destination. I was able to use some tricks I've recently learned, which
was cool. For example, I used `translate` and `str.maketrans` from yesterday to turn my string of
directions, `LRLRLLL..`, into 0s and 1s so I could directly index into my data structure for what
node to move to next. I also realized that counting the number of iterations can be done with an
`enumerate` that starts at 1, i.e., `enumerate(_, 1)`.

I was initially being really dumb for Part B. It was a few quick modifications from Part A to run
Part B, but it barely crossed my mind that the long run time for Part B meant that another approach
was necessary; I just sat there and waited... After my friend gave me a subtle hint, I realized that
maybe we should examine the periods of each path to see how often each path revisits a node that
ends with Z. Luckily, the distance from `**A` to `**Z` was exactly the same as the distance from
`**Z` back to `**Z` for all starting nodes `**A`, so the problem boiled down to finding the LCM of
each of the periods. What I was worried about was if the distance from `**A` to `**Z` happened to be
different from the distance from `**Z` back to `**Z`, i.e., the cycle length is different from the
length it takes to enter the cycle. If this had been the case, then the problem would've required
the Chinese Remainder Theorem, which would've been cool, but I'm also happy it didn't end up being
that involved.

### Day 9

I was expecting today's to be difficult since it's an odd-numbered day and a Friday night, but it
wasn't bad - in fact, kind of fun. I spent too long during Part A trying to come up with some clever
mathematical way of solving the problem instead of just implementing the naive solution. It wasn't
me some time, but oh well. The naive implementation was pretty straightforward after all.

For Part B, I forgot that extending to the left means that we needed to worry about the subtraction
sign, so I spent some time trying to debug a negative sign issue... silly mistake.

After chatting with a friend of mine, we realized that Part B is just Part A but with the initial
sequences reversed, and so this is the version that I'm making available in my repo. In my opinion,
it makes the solution for this problem way cleaner, and it looks quite nice.

### Day 10

Wow, this was a difficult day. I initially struggled way too much on writing a recursive solution,
constantly into the recursion limit in Python. I eventually decided to just cut my losses and
rewrite the traversal logic as a while loop, and it pretty much worked on the first try. I think my
lesson learned here is to not always just reach for recursion immediately, especially when the
problem setup is not super complicated. 

Part B was quite interesting, and I really liked the problem because of Part B. I worked with a
friend of mine (Bonsoon) to figure out how we might want to go about it, and I must admit that I
really like the solution we came up with. Basically, the idea is to shoot rays at the path and count
how many times the ray intersects the pipes. If it has intersected an even number of times when it
reaches an empty spot in the grid, then the empty spot must be outside of the loop, and if it has
intersect an odd number of times when it reaches an empty spot in the grid, then the empty spot must
be inside of the loop. To perform this computation, we realized that we can drop all `-`
characters because they aren't important in this computation. We can also drop all `F7` and `LJ`
pairs because they would add 2 to the intersection count, which doesn't change the parity of the
number. Finally, every instance of `FJ`, `L7`, and `|` all count as 1 intersection, and done!

What a fun problem!

### Day 11

Nice simple day. I got screwed over by placing my `return` statement in the wrong level of
`for`-loops... thanks Python.

But, I thought it was neat that I got to use my `manhattan_dist` function that I wrote last year!
