// Last updated: 02/03/2026, 13:58:13
function map(arr: number[], fn: (n: number, i: number) => number): number[] {
  const ans: number[] = [];
  arr.forEach((a, index) => {
    ans.push(fn(a, index));
  });
  return ans;
}