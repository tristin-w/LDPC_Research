# RL-Optimized LDPC Decoding

Python/C++ implementations of LDPC decoders (erasure, bit-flipping, sum-product,
min-sum) with flooding and sequential scheduling, plus a Q-learning agent
that learns check-node update orders.

**Researcher:** Tristin Webb, New Mexico State University
**Advisor:** Dr. David G. M. Mitchell, Klipsch School of ECE

## Roadmap
- [ ] Encoder, parity-check/generator matrices, Tanner graph
- [ ] Erasure and bit-flipping decoders
- [ ] Sum-product (BP) decoder, flooding schedule
- [ ] BER/FER Monte Carlo simulation
- [ ] CCSDS (128,64) baseline validated
- [ ] Min-sum and normalized min-sum
- [ ] Sequential (serial check-node) scheduling
- [ ] Q-learning scheduler
- [ ] RL vs. flooding vs. sequential comparison

## Repository structure
    decoders/      decoding algorithms
    codes/         parity-check matrices (toy codes, CCSDS)
    channel/       BPSK/AWGN simulation
    rl/            RL environment and Q-learning agent
    experiments/   scripts that produce results
    tests/         unit tests against textbook examples
    results/       figures and data

## Validation
- SPA decoder reproduces the worked example in Johnson,
  "Introducing Low-Density Parity-Check Codes," pp. 35–38.

## References
1. S. J. Johnson, "Introducing Low-Density Parity-Check Codes."
2. J. Chen et al., "Reduced-Complexity Decoding of LDPC Codes,"
   IEEE Trans. Commun., 2005.
3. S. Habib and D. G. M. Mitchell, "Reinforcement Learning for
   Sequential Decoding of Generalized LDPC Codes," ISTC, 2023.
