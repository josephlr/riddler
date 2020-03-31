use core::{iter, mem};
use rand::{seq::SliceRandom, thread_rng};
use rayon::prelude::*;

const N: usize = 1_000_000;
const CHUNK_ITER: usize = 10_00;
const NUM_CHUNKS: usize = N / CHUNK_ITER;

fn avg(n: usize) -> f64 {
    let mut mem = vec![0; 2 * n * NUM_CHUNKS];
    let chunks = mem.chunks_exact_mut(2 * n).collect::<Vec<_>>();

    let sum: usize = chunks.into_par_iter().map(run_chunk).sum();
    sum as f64 / N as f64
}

fn run_chunk(v: &mut [usize]) -> usize {
    let (v1, v2) = v.split_at_mut(v.len() / 2);
    iter::repeat_with(|| run(v1, v2)).take(CHUNK_ITER).sum()
}

fn run<'a>(mut input: &'a mut [usize], mut output: &'a mut [usize]) -> usize {
    debug_assert_eq!(input.len(), output.len());
    // Setup the initial input
    for (i, entry) in input.iter_mut().enumerate() {
        *entry = i;
    }

    let mut count = 0;
    while !all_same(input) {
        rand_select(input, output);
        mem::swap(&mut input, &mut output);
        count += 1;
    }
    count
}

fn rand_select<T: Copy>(input: &[T], output: &mut [T]) {
    let mut rng = thread_rng();
    for item in output {
        *item = *input.choose(&mut rng).unwrap();
    }
}

fn all_same<T: Eq>(s: &[T]) -> bool {
    let fst = &s[0];
    s[1..].iter().all(|x| x == fst)
}

fn main() {
    // println!("{}", avg(6));
    for n in 2..100 {
        println!("{} -> {}", n, avg(n))
    }
}
