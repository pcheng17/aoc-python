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

But, I thought it was neat that I got to use my `manhattan` function that I wrote last year!

I also learned that `itertools` has a `combinations` function, which produces all combinations of
items in the input iterable.

### Day 12

Oof, this one was hard. I initially started going down the route of brute-forcing it, which would've
worked for Part A (thanks, Bonsoon, for being faster than me at it so you could confirm for me), but
per his warning, I did not end up spending time doing brute force because of Part B. We then spent
a hours brainstorming how to properly solve this problem, and eventually landed on the idea of
dynamic programming/memoization, the latter of which is what we ended up implementing. Sure enough,
after a lot of debugging, it all worked out.

In retrospect, this problem definitely requires something like memoization, which takes care of
exploring the tail end of the branch of this pattern. It has the same flavor as some of the problems from last year's Advent of Code that also required memoization. I should've noticed the pattern sooner.

I finally learned how to use `@cache` from `functools` to memoize a function. I've seen it used
before but never really understood how it worked. It's pretty neat - basically, a wrapper around
your function to automagically memoize calls to it as long as the arguments are immutable, e.g.,
`tuple` instead of `list`. I swapped out my own memoization implementation for this one, and it
worked like a charm.

### Day 13

Pretty straightforward! I think I really lucked out with using Python for this problem because of
the nice properties of `zip` in that it stops when the shortest iterable is exhausted. Thus, I
didn't need to worry about the different lengths of the mirrored halves.

I think I kind of lucked out on Part B. I started going down the route of trying to figure out how
to detect the smudge while checking for where the grid is mirrored, but then somehow realized that I
can just search for an "almost-mirror" where the two sides have a Levenshtein distance of 1.

Interesting observation: I tried to use my own `Grid2D` class for this, but immediately scrapped
that idea because I was worried that working with the data from behind an interface would make logic
too messy... Maybe designing classes for these types of problems isn't the best idea.

Also, I got my best ranking so far on Part A - Rank 387!

Edit: I just learned something new! `*zip(*grid)` is a mind-blowing way to transpose a 2D array... I
need to keep this in my back pocket.

### Day 14

For Part A, I think I was being a little too clever in my first pass at the problem. Instead of just
brute-forcing the movement of each stone and checking for collisions, I tried to take a sweep-like
approach where, for all the rocks in one row, I send them down as far as they'll go in one step.
It worked, but it required a lot of index bookeeping to keep track of how far in each column a rock
could travel as it slid.

In Part B, I was definitely being way too clever for my own good. Because I had just learned about
how to tranpose a grid by using `*zip(*grid)`, I thought that I could literally rotate the grid and
then use the same logic from Part A of sliding north to be able to slide in every direction. This
actually did work, and it was pretty cool to not have to write any extra code for the other
directions, but I ultimately wasted a ton of time debugging my scoring logic. I forgot that the grid
should be oriented in the original orientation for scoring, which meant that I needed to rotate the
grid one more time (after sliding to the East) before scoring. This bug took me way too long to
discover...

In any case, my rewrite of the solution uses very similar ideas. However, I've replaced the sliding
logic with a very clever string-only solution. Basically, sliding to the left means to replace `.O`
with `O.`, and sliding to the right means to replace `O.` with `.O`. So cool! And then to slide
North or South, you can tranpose the grid and then slide left or right, respectively. In this
version, I do remember to flip the grid back to its original orientation before scoring.

My friend also developed a nice way of determining period lengths of the scoring. There is basically
no way of running the simulation out to one billion cycles, so the idea is to figure out at what
point the scores became periodic, and then to extrapolate this out to one billion to determine the
answer. Essentially, it boils down to storing a map for the history, where the keys are the `grid`
itself, and the keys are `(cycle index, score)`. The moment a grid is repeated is when we've
discovered one period of the sequence, and we can determine our answer from there.

### Day 15

Easy day! Part B was basically all reading comprehension.

I thought it was funny how the problem is about hashmaps, and yet, I didn't end up using a `dict` at
all. Since the boxes were contiguously indexed, I opted for a list to store the boxes.

### Day 16

Not bad. At first, I was a little worried that brute forcing the rules would be a pain, but it
turned out just fine. I opted for a BFS approach, where my set of visited nodes also contained
information about the direction in which each node was visited. Without it, then you might end up
loosing paths because nodes can be visited from different directions.

Brute forcing Part B was also fine, nothing special.

### Day 17

### Day 18

### Day 19

### Day 20

This problem was fun! Part A was pretty straightforward, despite taking awhile to fully
understand the problem. I had to spend like 15 minutes chatting with Bonsoon about it until we were
totally convinced we knew what was happening.

Part B was great. Upon reading the problem, I immediately thought "oh man, how do I even do
this...??" Usually, problems that require us to solve the problem out to some very large number must
have some kind of periodic behavior. However, the twist with this one was that we needed to find
the first time at which a certain condition would happen, which could be arbitrarily large, so
finding a period... is basically just solving the problem entirely.

Once Bonsoon got to Part B, we spent quite a long time discussing how to solve this. We started to
realize that there is some periodic behavior happening within the problem, but for the longest
time, much of the behavior we observed was not helpful. Finally, we realized that we were looking
way too "deep" into the problem, and the periodicity that we needed was actually in the penultimate
state of the logic gates of the problem: the four penultimate logic gates that fed into the final
one needed to all be `HIGH` in order for the condition of the problem to be satisified, which meant
that, if we could determine the period of each of these four logic gates, we could use an LCM to
determine the period of the entire system.

Luckily, much like an earlier problem this year, the periodicity was "simple" enough in that, an LCM
was sufficient for solving the problem, and we didn't have to reach for the Chinese Remainder Theorem.

### Day 21

Part A was vanilla BFS.

Part B, however, was weird. To be honest, I'm not sure if I'm really a fan of this problem, mostly
because I'm not sure I thorougly understand what's going on. Basically, it turns out that the number
of reachable spots in the grid every 131 steps, where 131 is the size of the grid, follows a
quadratic curve. Bonsoon, who helped me with this problem, was only able to figure this out after a
ton tinkering around with the problem. Once the right family of values was found, interpolating the
data with a quadratic function and then evaluating it at the appropriate x-value produced the right
answer.

I can kind of believe that this works? Maybe? ::shrug::

### Day 22

Last year, we had Tetris. This year, it was Jenga. Despite having to use quite a lot of brain power,
I thought this one was quite interesting. It was freshing after the few puzzle-like ones that we've
had recently, where this one was more of a programming challenge. Part A took me about 3 hours to
complete because of a silly little bug that only showed itself on very specific types on inputs.
Instead of simulating the stacking of the bricks one "time step" at a time, I decided to just
directly compute how far each brick could travel before it would hit either the ground or another
block. However, in updating the heightfield of the resulting pile, I forgot to account for the fact
that the newly settled block could have height greater than one... so dumb.

The logic to determine if one block could support another was reminiscent of a typical interview
problem that I've both given and received, which is, how do you determine when two axis-aligned
boxes overlap? If one block were to support another, that means that if you were to look at the
configuration from the top down, the two blocks would have to overlap.

The logic to determine whether or not a block could be removed without causing others to topple was
also quite interesting. I used a graph-based approach, where a (child) block can only be removed if
it is not the only child of a parent block.

For Part B, I started by trying to build a graph for the dependency tree of the entire stack. Then,
to compute how many blocks would tumble when a particular block disintegrated, I would've had to
walk up the tree to compute how many blocks would be affected by the removal of children blocks. I
was not able to get this right on the first try, so I decided to just take the brute force approach:
for each block to disintegrate, re-run my "simulation" from Part A to see how many blocks would end
up resettling.

### Day 23

Man, this one was hard. I used BFS in Part A, but got stuck on how to properly implement a visited
set to prevent myself from walking over the same route. After quite a bit of time, I realized that
every ghost that gets spawned to explore a new route needs to know its history of visited nodes, so,
so every element in the queue (a ghost that needs to be processed) must also store a set. Then, the
trick was that, when adding a new item to the queue, the new item's history of visited nodes
**must** be a new copy of the history of visited nodes of the item that spawned it. This way, the
history of visited nodes of the parent ghost is not modified when the child ghost explores a new
path.

Part B was brutal. I tried to improve my code for Part A, but I think the problem was just too large
to be done in a naive BFS way. Bonsoon was the real MVP behind my solution. He observed that the map
was actually a maze with where all the channels were only one tile wide, so in most of the map,
there was only one way to walk. Where there were multiple ways to walk, the maze had a branch point
where a decision of direction had to be made. Bonsoon's idea was to first extract all the branch
points of the map, including the start and end, to form a coarse approximation of the maze; this
forms a graph. Then, find all pair-wise max distances between nodes of this graph by using the maze
under the restriction that we never cross over our own path, and we never walk through another
branch point; this produces a weighted graph. Finally, use BFS on this weighted graph to find the
largest distance from start to end.

After much debugging, I was able to produce a solution. Surprisingly, it wasn't fast, but it worked.
Thanks Bonsoon!

### Day 24

This one was fun, mostly because it was much more mathy type of puzzle. I solved Part A by just
solving for the closed form of the intersection points - pretty straightforward.

For Part B, I really wanted to write down the system of equations to solve it, but ended up getting
too lazy, so I figured out how to use `sympy` to set up and solve the equations for me. The catch is
that you only need data from 3 hailstones to setup the sufficient number of equations.

### Day 25

This was was great, mostly because Bonsoon and I came up with our cursed approach. I plotted the
graph using Graphviz, and then realized that I could easily spot the two connected components once
the three appropriate edges were removed (thanks to how Graphviz plotted the graph). Me being
big-brained, I decided to just count up the number of nodes in one of the connected components by
hand. This took me two tries though because I miscounted the first time... I ended up being off by
two. The second time, I pulled up an online tally app so I could just hit my space bar to count for
me. EZ

I've included the svg file for the graph I generated for safe-keeping.

I realized that I can count things really quickly when it comes in groups of 2 or 3. The moment
there are 4 items in a group, I found that I would often wonder if I had hit the space bar 4 times...
