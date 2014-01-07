
================================================================================
Fog Creek Software
================================================================================

:Headquarters: New York City, New York
:Industry: Project management tools
:Founders: Joel Spolsky; Michael Pryor
:CEO: Michael Pryor
:Founded: September 2000
:Ownership: Private
:Size: ~45 [1]_

.. contents::
   :depth: 2

Products & Services
================================================================================

.. _fogbugz:
.. _kiln:

FogBugz & Kiln
--------------------------------------------------------------------------------
:Launch: November 2000
:Status: Active

FogBugz manages projects, track bugs, and even tell you when you're going to
ship. Kiln is a complete version control system for Mercurial and Git. Kiln
requires FogBugz.

.. _trello:

Trello
--------------------------------------------------------------------------------
:Launch: September 13, 2011
:Status: Active

Trello is a web-based project management application.


.. _copilot:

Copilot
--------------------------------------------------------------------------------
:Launch: August 8, 2005
:Status: Available for purchase, but discontinued.

Copilot is a remote assistance service.

.. _citydesk:

CityDesk
--------------------------------------------------------------------------------
:StableRelease: August 25, 2003
:Status: Available for purchase, but discontinued.

CityDesk is a client-side Windows content management system.

.. _webputty:

WebPutty
--------------------------------------------------------------------------------
:status: Discontinued

WebPutty is a simple CSS editing and hosting service.

History
================================================================================

Finance
================================================================================

Originally FogCreek did consulting to make money.

As of December 2013: [1]_

- `FogBugz`_ is the main source of revenue, together with `Kiln`_.

- `Trello`_ is not making a ton of money (maybe 10% of revenue) but paid options
  were introduced only recently, and Trello is expected to be a large part of
  future revenue. FogCreek is hiring aggressively for Trello under this
  assumption.

- `Citydesk`_ and `Copilot`_ make nominal revenue

Technology
================================================================================

Only FogBugz, Kiln, and Trello remains under actively development. Copilot and
CityDesk are maintained and available for purchase. In addition, Fog Creek has a
dev tools division.

FogBugz
--------------------------------------------------------------------------------

FogBugz originally started as an internal bug tracking tool while the company
was focused on consulting.

FogBugz is written in a number of languages, including ASP and PHP, which are
compiled down to .NET. Some of it is written in an in-house language called
Wasabi which also compiles to .NET. Reportedly, Java can be found. [2]_

FogBugz is being rewritten in C# (termed "FastBugz").

Kiln
--------------------------------------------------------------------------------

Kiln is written entirely in C#.

Trello
--------------------------------------------------------------------------------

Trello was prototyped in `Creek Week`_ after Joel suggested the idea to some
designers.

Trello is written in Coffeescript, node.js, and MongoDB.

Copilot
--------------------------------------------------------------------------------

Copilot (originally Project Aardvark) is written in C++ and was developed by a
group of interns.


Internships
--------------------------------------------------------------------------------

- $5000/mo ($31/hr)
- Free housing
- Free gym membership
- Free lunch
- Free transportation

Culture
================================================================================

Fog Creek was built according to Joel's theory of building software companies,
which is basically: attract the best software developers and then outperform
competition (see: `Hitting the high notes`).

Engineering Culture
--------------------------------------------------------------------------------

Since software is the product being sold, the company is very engineering
focused and takes pride in shipping quality software. [1]_ [2]_ For instance,
the FogBugz team consciously tries to improve its development process, [2]_ and
the Trello team does not release code before review. [1]_

Structure is fairly flat, and nobody is far away from either founder. There is
at team for each service and each team is lead by a PM (who was at one point
formerly a developer). [1]_ Implementation and design is left entirely to
developers. [1]_

.. _creek week:

Developers have leeway on decisions somewhere in between a startup and midsize
(~250) company. [1]_ Engineers may work on their own projects with permission
(e.g. `WebPutty`_).  Additionally, Fog Creek regularly a "Creek Week" (hack
week) where developers are free to prototype new ideas. [2]_ There is
opportunity to switch teams. Two of senior engineers now on Trello were on
FogBugz. [2]_

Engineers are very smart, which means you can trust other people to complete
their work well, and they are very good about teaching. Programming interests
are diverse, which means there is a lot to be learned. [2]_

Company Culture
--------------------------------------------------------------------------------

-   A lot of the people here hang out together after work. [1]_

-   Intern events. Once every week or two weeks, devs and interns go do
    something cool in NYC. [1]_

-   Every Thursday people stick around and play board games. 10-15 people
    there. [1]_

-   Every Friday people sticks around for beer. [1]_

-   Many people do not know anyone in the city so they hang out often. Notably,
    improv classes were mentioned. [1]_

-   Half of people are 23 +/- 5 years. [1]_

Team preferences for new hires are usually accommodated. [2]_

Competition
================================================================================

FogBugz and Trello competes with `Pivotal Tracker`, `Basecamp`, and `Asana`

Kiln competes with `Github` and `Bitbucket`.

Screens
================================================================================

The screening process consists of three stages:

1. Phone screen
2. Phone screen
3. In-person interview

   - 3 to 5 back-to-back interviews (each 1 hr)
   - Largely technical, or asking about resume
   - If accepted, Fog Creek will give an offer letter before you leave

As far as I can tell, both phone screens are conducted blind, meaning, the
interviewer does not read your resume nor check your online profiles. Presumably
this is to prevent any non-technical from biasing the interviewer. The
interviewers may ask you to describe yourself.

Between each screen, Fog Creek will be back within at most a week, but usually
much faster.

Phone Screen 1
--------------------------------------------------------------------------------

Fog Creek Code Interview

.. code:: python

    Bt(item=1, 
             1   
           /   \   
         2       3   
          \     /   
           4   5   

          
    2 6 4 7 1 5 3

    def _inorder(bt):
        if bt.left is not None:
            for node in _inorder(bt.left):
                yield node
        yield bt.item
        if bt.right is not None:
            for node in _inorder(bt.right):
                yield node

    def inorder(bt):
        """
        >>> bt = BT(1, BT(2), BT(3))
        >>> inorder(bt)
        >>> 2 1 3
        """
        for node in _inorder(bt):
            print node

    def _preorder(bt):
        yield bt.item
        if bt.left is not None:
            for node in _inorder(bt.left):
                yield node
        if bt.right is not None:
            for node in _inorder(bt.right):
                yield node

    def preorder(bt):
        for node in _preorder(bt):
            print node

    pre: 1 3 7 6 2 4 5 8
    in:  3 6 7 1 4 2 5 8

    pre: 3 7 6
    in:  3 6 7

    pre: 2 4 5 8
    in: 4 2 5 8

             1
           /   \
         3       2
       /  \     /  \
      X    7  4     5
     / \  / \ / \  / \
    X  X 6  X X X   8

             1
           /   \
         6       2
       /  \     /  \
      3    7  4     5
     / \  / \ / \  / \
    X  X  X X X X  8  X


    # O(n ^ 2)
    def _construct_bt(preorder, inorder, p_indexes, i_indexes):
        root = preorder[0] # 1, 3, 
        # O(n)
        i = inorder.index(root) # 3, 0,
        i_left, i_right = inorder[:i], inorder[i+1:]
        preorder2 = preorder[1:]
        # (3 7 6, 2 4 5 8), (, 7 6)
        p_left, p_right = preorder2[:i], preorder2[i:]
        return BT(
            item=root, # 1
            left=construct_bt(p_left, i_left) if p_left else None,
            right=construct(p_right, i_right) if p_right else None,
        )

    def construct_bt(preorder, inorder):
        # get indexes
        return _construct_bt(preorder, inorder, p_indexes, i_indexes)

Phone Screen 2
--------------------------------------------------------------------------------

1. Flatten a quasi-linked linked tree
2. Unflatten it

.. code:: python

    class Node:
        def __init__(self, val, next, prev, child):
            self.val = val
            self.next = next
            self.prev = prev
            self.child = child

    h           t
    1 - 2 - 3 - 4 - 9 layer 1
        |       |
        5 - 6   7  layer 2
        
                |---------------v
    1 - 2 - 3 - 4 - 9 - 5 - 6 - 7
        |---------------^

    h   t
    1 - 2
        
    def slice(node):
        prev = node.prev
        prev.next = None
        node.prev = None
        return prev

    def unflatten(h, t):
        current = t
        while current:
            if current.child:
                t = slice(current.child)
            current = current.prev
        retun h, t

    n nodes total
    d layers

    runtime O(n)
    space O(d)

    h                       t
    1 - 2 - 5 - 6 - 3 - 4 - 7
        |___^           |___^
        
    1 - 2 -         4
        |           |
        5 - 6 - 3   7


    def join(a, b):
        a.next = b
        b.prev = a

    def flatten(h, t=None):
        current = h
        while current:
            next = current.next
            if current.child:
                h2, t2 = flatten(current.child)
                join(current, h2)
                if next is not None:
                    join(t2, next)
                else: # we reached the end of the list
                    return h, t2
            if next is None:
                return h, current
            else:
                current = next

    flatten(h, t)

References
================================================================================

.. [1] Based on first phone screen conducted on 12.6.2013. The interviewer's
       points of reference were internships at a startup (employee 8) and a
       midsize (~250 people) company.

.. [2] Based on second phone screen with a 5-year employee on 12.11.2013. The
       interviewer had worked at an IT company before accepting a full-time
       position out of school.

