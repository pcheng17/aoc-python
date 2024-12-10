# 2024

## Thoughts

### Day 1

Wow, I'm rusty, but the problem was very straightforward. Reading comprehension already messed me up
today - I missed the fact that part a needed to be sorted. Part b was just a lot of tripping over
off-by-one errors. Regardless, easy day! A nice way to get back into the AoC mindset.

### Day 2

Yep, really rusty. I struggled a lot on syntax in this problem, like trying to figure out the
Pythonic way of finding the delta between pairs of adjacent elements. Then in part b, I completely
messed up the logic. I was trying to use some of the work done in part a, but very incorrectly. At
the end of the day, I just chose to create a new list for every removed element to see if the row is
safe upon removing one element. I also forgot the correct Python notation here, so I ended up with a
really brute-force way of popping elements.

### Day 3

The problem itself was fine. I just got completely screwed over because I always immediately split
my input at the newlines, thinking that each row of the input file is a new piece of data to
process. Woops, not the case this time...

Knowing a tiny bit of regex saved me this time, too. I remember I really struggled with regex last
year.

### Day 4

Grids! I got to `[*zip(*grid)]` today! I choked a little bit on the diagonals logic. I feel like
there should be an easier way of going about it, but I was in too deep. I wasn't going to back out
of my approach anymore. It worked though. Part b was much easier because the pattern was much easier
to reason about.

Remember:
- `[*zip(*grid)]` transposes the grid
- `[*zip(*grid[::-1])]` rotates the grid clockwise by 90 degrees

### Day 5

This problem was kind of just annoying. Part a wasn't difficult, and part b just required me to
remember how to use `cmp_to_key` as a custom comparison function in `sort`. Otherwise, a pretty
straightforward problem.

`cmp_to_key` needs to do the following:

- return `-1` if `a < b`
- return `1` if `a > b`
- return `0` if `a == b`

Edit: I came back and implemented bubble sort to not use any built-in tools.

### Day 6

We're getting into the territory of typical AoC problems now. This one was pretty straight forward.
My mistake for part b was assuming that the loop that we enter must use the newly placed obstacle.
It turns out that's not the case, i.e., after hitting the newly placed obstacle once, there was at
least one case where we entered a loop without ever revisiting the newly placed obstacle. I got
around this by just storing the state at every position along the path that I've traveled so far. If
we see a previous state, then we're in a loop. That should've been my first approach...

### Day 7

Not bad today. It took me a little bit to figure out how I wanted to check all possible operations.
I was getting stuck on doing it recursively because I was trying to be clever. I ended up just
evaluating one of the operations on the first two integers, creating a new array of that new integer
along with the rest, and then recursively called myself with that new array. This turned out to be
totally fine.

### Day 8

I think this one was pretty easy. The problem statement itself was a little hard to parse but in the
end, it was pretty straight forward. I don't think there were any traps.

### Day 9

Wow, this one took quite a bit of time to understand what was going on. It felt like there was a lot
of moving pieces in this problem, and using only words and a few pictures didn't do explaining the
problem justice. However, once the problem started making sense, I think this was actually a very
interesting problem. It touches on some important algorithms and data structures, such as the idea
of matching two indices toward each other, or the idea of a heap (which I did not actually use, oh
well). All in all, despite being a hard problem to understand, I liked it.

### Day 10

Not bad! A little rusty thinking about BFS/DFS and memoization, but this was a nice warm up into
these types of problems. I'm happy I caught on pretty quickly that part a is much better done in
"reverse", i.e., start from the 9's and move backward toward the 0s... or at least I think it's much
better done in reverse. Part b took me a second to figure out how I wanted to setup the DFS, but all
in all, pretty straightforward.

I learned an interesting trick today. If I want to pass a variable by reference, just stick it in a
(one-element) list.

