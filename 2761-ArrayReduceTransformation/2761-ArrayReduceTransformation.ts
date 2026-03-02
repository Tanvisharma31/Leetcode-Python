// Last updated: 02/03/2026, 13:58:09
type Fn = (accum: number, curr: number) => number;

function reduce(nums: number[], fn: Fn, init: number): number {
  let ans = init;
  for (const num of nums) {
    ans = fn(ans, num);
  }
  return ans;
}