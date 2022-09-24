-   initialize network `net`
-   loop
    -   initialize simulation (with a start state)
    -   initialize a replay buffer `D`
    -   set `s_0` ot the initial state
    -   loop while the simulation is not complete
        -   compute the action `a_t`
        -   send the action to the simulation
        -   sample `s_(t+1)`, `r_t`
        -   add the tuple `(s_t, a_t, r_t, s_t+1)` to D
-   `torch.save(net, 'net.tch')`

### Variables

-   `s_t` - state at time `t`
-   `a_t` - action taken by the agent at time `t`
-   `r_t` - reward given to the agent by the simulation at time `t` after taking the
    action `a_t` on state `s_t`
-   `s_(t+1)` - state `t+1`, the result of the agent taking action `a_t` on `s_t`
-   `o_t` - `1` if `s_t` is the final state else `0`

-   `R_t` - return - the cumulative sum of the rewards
    $$R_t = \sum_{k=0}^{\infty}r_{t+k+1}$$
-   `R_t` - discounted return - scaled sum of the cumulative rewards
    -   `gamma` - discount factor
        $$R_t = \sum_{k=0}^{\infty}\gamma^{k}r_{t+k+1}$$
-   `pi(s, a)` - policy - the probability of the agent taking action `a` given state `s`
-   `V(s, pi)` - state value function - expected return starting from `s` and following the policy `pi`
    $$V^\pi(s) = \mathbb{E}_\pi\big[R_t | s_t = s\big]$$
-   `Q(s, a, pi)` - action value function - expected return starting from `s`, taking the action `a` and then following the policy `pi`
    $$Q^\pi(s, a) = \mathbb{E}_\pi\big[R_t | s_t = s, a_t = a\big] = r_t + \lambda V^{\pi}(s_{t+1})$$
-   `q(s, a)` - the optimal action value function - it is given by the Bellman Optimality Equation
    $$q(s, a) = \mathbb{E}_\pi\big[r_{t+1} + \gamma \max_{a'} q(s', a')\big]$$

## Pseudo Code

## Action Space example

-   available actions: `right`, `left`, `up`, `down`, `shoot`

    -   Action space:

    ```
    (right, no)
    (left, no)
    (up, no)
    (down, no)
    (shoot, no)

    (right, shoot)
    (left, shoot)
    (up, shoot)
    (down, shoot)
    (shoot, shoot)
    ```

-   available actions: `right`, `left`, `up`, `down`, `shoot`

## State Value Function Example

-   action space: `[a_a, a_b]`
-   current state: `s_0`
-   if you take action `a_a` you will be transformed to state `s_1a`
-   if you take action `a_b` you will be transformed to state `s_1b`
-   let `pi(s, a_a) = 0.2`, `pi(s, a_b) = 0.8`
-   then `V(s) = pi(s, a_a) * V(s_0) + pi(s, a_b) * V(s_1a) = 0.2 * V(s_0) + 0.8 * V(s_1b)`
