
================================================================================
Uber
================================================================================
--------------------------------------------------------------------------------
Everyone's private driver
--------------------------------------------------------------------------------

:HQ: San Francisco, CA

:Industry: Transport

:Founders: Garret Camp; Travis Kalanick

:Founded: March 2009

:Ownership: Venture-backed

:Chairman:
    Garret Camp

:CEO: Travis Kalanick

:CTO: Thuan Pham

:Head of Global Operations: Ryan Graves

:CFO: Brent Callinicos

:Keywords: mobile, transportation, logistics

:Valuation: $3.5B (December 2013) [6]_
:Estimated annual revenue: $210M (December 2013) [7]_

:Abstract:
    Uber makes a mobile application that connects passengers on-demand with
    drivers of vehicles for hire.

.. contents::
   :depth: 1

Services
================================================================================

Users open the Uber app on their smart phone and choose one of several grades of
cars and indicate where they want to be picked up. Payments are charged directly
to credit card and tip is included in the fare. Drivers and riders rate each
other after each trip, improving the experience for both the driver and the
rider.

======= =========   ========    ==========  ======== ======
Service Base fare   Per mile    Per minute  Min Fare Notes
======= =========   ========    ==========  ======== ======
Taxi    $3.50       $2.75       $0.55       $0.00    
UberX   $5.00       $3.25       $0.75       $10.00   Casual
Black   $8.00       $4.90       $1.25       $15.00
SUV     $15.00      $5.25       $1.35       $25.00   Seats 6.
======= =========   ========    ==========  ======== ======

Price surging
-------------

During holiday times such as Halloween or New Year's Eve, Uber increases its
prices to "surge price" levels to reach an economic equilibrium by attracting
more drivers. Uber has also used surge pricing during extremely inclement
weather, such as a July 8, 2013 rainstorm that flooded many streets in the
Greater Toronto Area

Availability
------------

As of December 2013, Uber operates in 22 countries and 60 cities:

- San Francisco
- Bangalore
- New York City
- Seattle
- Chicago
- Boston
- Washington, DC
- Toronto
- Johnanesburg
- Cape Town
- Lyon
- Paris (December 7, 2011)
- Berlin
- Los Angeles (February 2012)
- Philadelphia (June 2012)
- Dallas
- Abu Dhabi
- New Delhi, India
- Guangzhou, China
- Shenzhen, China

History
================================================================================

Founded in March 2009 as UberCab by Garret Camp and Travis Kalanick.

The first prototype was developed by Garret and Travis with help of Oscalar Salarazar and Conrad Whelean, both friends of Garret from grad school.

Initially was "uberapp.com".

On August 1, 2009, Uber raised $200,000 in Seed funding.

In early 2010, Travis met Ryan Grave who became Uber's first full-time employee.

In June 2010, Uber officially launched in San Francisco with a few cars.

Users could text their address to UBR-CAB (827-222) if they did not have a smartphone.

Ryan Graces became CEO but stepped down in August replaced by Travic Kalanick.

In 2010, Uber's mobile app launched in San Francisco on iPhones and Android phones.

In 2010, "uber.com" was transffer to Uber via a pruchase from Universal Music Group.

On October 15, 2010, Uber raised $1,250,000 in Angel funding.

On February 14, 2011, Uber raised $11,000 in Series A funding.

On December 07, 2011, Uber raised $37,000,000 in Series B funding.

In April 2010, Uber tested reservations for conventional taxis, at lower rates, in Chicago.

In May 2011, Uber received a cease-and-desist letter from the San Francisco Municipal Transportation Agency, claiming that it was operating an unlicensed taxi service, and another legal demand from the California Public Utilities Commission that it was operating an unlicensed limousine dispatch. Both claimed criminal violations and demanded that the company cease operations. In response the company, among other things, changed its name from UberCab to Uber.

In late 2011, Uber launched UberTAXI.

Uber introduces On-Demand BBQ for Austin, TX during SXSW 2012. Also pedicabs.

In July 2012, Uber entered the London market with an initial staff of about 90 drivers of Mercedes, BMW, and Jaguar.

On July 4, 2012, Uber launched UberX and Uber SUV.[3] UberX includes hybrid vehicles at a lower price point (35%[1]).

> “Uber X” will allow Uber partners to use its dispatching software in order to dole out vehicles beyond Lincoln Town Cars, giving passengers a choice between Toyota Prius Hybrids and SUVs like the Cadillac Escalade, etc.[1]

On July 13 2012, in honor of National Ice Cream Month, Uber launched Uber Ice Cream, which added the ability in 7 cities to summon an ice cream truck for on-demand delivery and bill the purchase to the user's account.

On July 3, 2013, Uber started offering experimental UberCHOPPER rides from New York City to The Hamptons for $3000 via cab and helicopter.

On August 23, 2013, Uber raised $258,000,000 in Series C funding.

On September 4, 2013, Uber announced its first sports deal. Partnering with the NFL Players Association to promote safe rides for NFL players, Uber, plans to appeal to a more mainstream audience for the future.

Finance
=======

Legal
================================================================================

Marketing
================================================================================

Uber has been known to promote its services with promotional codes for first
time users.

In New York, where the yellow cab market is functional and robust, Uber is seen
a good app, but not a life-changing one, and its use is still pretty much
limited to young people with disposable income. [6]_

Uber has said that its high prices are the premium that the customers pay for a
cab service that is not only reliable but also punctual and comfortable.

Several drivers have credited Uber for increasing their potential earnings by
30%.

Technology
================================================================================

:Technology:
    Python, Ruby, Javascript, C++, Java
    PostgreSQL, MySQL,
    Node.js,
    Redis,
    iOS,
    Android,
:Size:
    80 engineers

    - 10 on infrastructure, 2 of which on developer tools
:Perks: Uber credits

.. contents:: Engineering Groups
   :local:

Data and Analytics
------------------

Quants and scientists

Back end systems
----------------

Apps
----

iPhone, Android, SMS, web, the works

Dispatch
--------

node.js automated dispatch.

Rider/Driver support
--------------------

Internal tools, customer facing features.


Marketing systems
-----------------

Payments
--------

Infrastructure team
-------------------

The infrastructure team has control of all things below the platform level

Responsibilities:

- Manage physical devices
- Load balancing
- Writing base-line application
- Common utilities
- Hand it off to engineer and build hooks into various systems
- Logging
- Monitoring

  - Build tools for other teams

- Security
- Perimeter
- Developer tools
- Developer environments
- Sometimes fixing hot issues

  - If resources use of of control
  - Platform application stack

- Infrastructure must be reliable; down-time means drivers and riders lose

  - Occasional all-nighters to fight fires

- Most important problems (Fall 2013)

  - Eliminating single points of failure
  - Disaster recovery mechanisms
  - Scaling; betters tools for provisioning machines
  - Streamlining developer tools


Screen
--------------------------------------------------------------------------------

Phone screen (new grads)
~~~~~~~~~~~~~~~~~~~~~~~~

Very short. Just three questions:

1. Walk me through a project. Explain what went well and what didn't.
2. What is a feature Uber is missing?
3. How do you think software can be improved? What are bad software habits you have?

## Technical screen

45 minutes.

1. Describe your current passion in software
2. Technical problem: Weighted choice
3. Questions for interviewer

Solution:

.. code:: python

    import random

    # weighted random chooser
    def choose(choices):
        """Makes a weighted random choice from the input list.
         
        takes a tuple of (value, weight) tuples and returns a random value based on the distribution of weights.
       
        that is, given enough iterations, the distribution of values returned by this function
        should approximate the weight distribution. eg/
       
        choose(("a", 1), ("b", 2), ("c", 3)) should return "a" with a 1/6 chance,
        "b" with a 1/3 chance, and "c" with a 1/2 chance.
        ("a", 1), ("b", 1), ("c", 1)
        """
        if not choices:
          raise ValueError("no choices")
        x, weight = choices[0] #a, 1
        for x2, weight2 in choices[1:]: #c, 3
            r = random.randint(1, weight + weight2) #0-6
            if r > weight: #
                x = x2
            weight += weight2
        return x

On-site Interview
~~~~~~~~~~~~~~~~~

At least for the Uber infrastructure team, hints were very rare.

Round 1
^^^^^^^

- Describe a recent problem you had and how you solved it
- Explain what happens when a browser hits "uber.com"
- Write a routine which prints all the prime numbers from 1 to 100
- Given two files, f1 and f2, which both contains a list of line-separated words, write a function which returns all items unique to f1
- Count the number of 1 bits in a file.
- Given schema S of Users and Purchases:
    - Write a SQL query to find a user named "Daniel Chen"
    - Write a SQL query to count the country with the most purchases.
        - Requires a join and count
- Explain what happens when you type `ls` into the shell.

Round 2
^^^^^^^

- Describe the kinds of the problems you like to solve
- Given a file, `f`, of space separated words:
    - Write a function `exists` which returns if a string `s` is in `f`
        - I wrote a joke function with just did `s in f.read()` at first
        - Then they said assume the file cannot fit into memory
    - Write a function `is_compound` which takes a string `s` and returns True if `s` can be composed of words in `f`
- How comfortable are you with Unix?
- What is the difference between TCP and UDP?

Competition
================================================================================

- TaxiMagic
- SideCar (January 2012)
- Lyft (Summer 2012)

Uber faces competition from lower-cost real-time ridesharing startups such as Lyft and SideCar. To compete at lower price levels, Uber has introduced UberTaxi (partnerships with local taxi commissions) and UberX (non-luxury cars such as Toyota Prius Hybrids).[47] This move has led to dissatisfaction among existing Uber limo drivers who have seen their earnings decrease

Speculation
================================================================================

As of December 2013:

There is evidence Uber is attempting to dominate the taxi business.

- Last week, Uber lined up $2.5 billion in outside financing for low interest
  car loan for UberX drivers, making it possible for up to 200,000 drivers to
  buy their own cars at very low interest rates, under the condition they use
  those cars on the Uber network for the duration of the loan (~4 years). [6]_
  [8]_ This will increase availability of UberX at lower prices, potentially
  making them cheaper than taxis.

If Uber becomes cheap enough and expands it serves enough, it may be possible to
kill ownership of cars. [6]_ In this case, Uber effectively would become a
complete logistics company, and may effectively compete with Amazon:

    Kalanick said previous experiments, like delivering on-demand barbeque to
    attendees at SXSW and mariachi bands on Cinco de Mayo, showed Uber that its
    delivery system could expand to other functions. “It’s just different
    logistics.” [2]_

    "Uber is a cross between lifestyle and logistics. Lifestyle is gimme what I
    want and give it to me right now and logistics is physically delivering it
    to the person that wants it . . . once you're delivering cars in five
    minutes, there's a lot of things you can deliver in 5 minutes." [6]_

Long-term, many speculate Uber may partner with Google (one if its investors) to
use self-driving cars.


References
================================================================================

.. [1] http://techcrunch.com/2012/07/01/uber-opens-up-platform-to-non-limo-vehicles-with-uber-x-service-will-be-35-less-expensive/> (Tsotis, Alexia. July 1, 2012. TechCrunch. "Uber Opens up Platform to Non-Limo Vehicles With 'Uber X,' Service will be 35% Less Expensive")
.. [2] http://allthingsd.com/20120702/a-status-symbol-moves-down-market-whats-behind-the-uberx-launch/
.. [3] http://blog.uber.com/2012/07/03/sf-vehicle-choice/
.. [4] http://news.cnet.com/8301-30685_3-57338236-264/car-service-uber-raises-$32-million-launches-in-paris/ (December 7, 2011. "Car service Uber raises $32 million, launches in Paris.)
.. [5] http://yellowcabsf.com/index.php/service/cab-fares
.. [6] http://nymag.com/daily/intelligencer/2013/12/uber-might-be-more-valuable-than-facebook.html
.. [7] http://valleywag.gawker.com/leaked-ubers-internal-revenue-and-ride-request-number-1475924182
.. [8] http://www.bloomberg.com/news/2013-11-25/uber-drivers-to-get-gm-and-toyota-financing-deals.html
