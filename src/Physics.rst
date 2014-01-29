

================================================================================
Physics
================================================================================

Coloumb's law
================================================================================

    q1 o            r             Q
       |--------------------------o
    q2 o

.. code::

    F = k * (Q / (r && 2 + a ** 2)) * ((q_1 + q_2) * r, (q_2, q_1) * a)

Electric monopole: If two forces are of the same charge, then they act like the
same as `r` increases. In such a case, Fx = 2kQqr / () = 2kQq / r**2, Fy=0

Electric dipole: If they are different, Fx=0, Fy= - 2kQq()a, limit is 2kQq * a /
r^3

Important thing is r^3 here. Bipole expansion.

Electric potential energy
================================================================================

Electric force is conservative force, so it has electric potential energy.

Energy is conserved provided you account for potential energy.


    o ----------- o
    q1     r12    q2

What is work t bring q2 from inf to r21.

Electric force opposes 

F21 = k * q1 * q2 / (r ** 2) * ^r

W = integral(infinity, r21, F_applied o d * s)

  = integral(infinity, r21, - F_21 o d * s)

  = integral(infinity, r21, -k * q1 * q2 / r&2 * ^r) * (^r * d * r)

  = k q1 * q2 * r21


Line integral describes wokr done by a force.

W is independent of Path.

Potential energy, U = work to bring charges from inf

U = W = k * q1 * q2 / r12

Now, what if we add a 3rd charge?

Change in work:

    dW = integral -F3 * d s = integral -F * d * s - integral f32 * d * s
    dW = k * q1 * q2  / r31 + k * q2 * q3 / r32
    

Total work to bring 3 charges:

    U = k * (q1 * q2 / rr1 + k * q1 * q3 / r31 + q2 * q3 / r32)

Conjecture for N charges:

    U = sum (i < j = 1) (N) (k * qi * jq / rij)

See: Madeleng Const
