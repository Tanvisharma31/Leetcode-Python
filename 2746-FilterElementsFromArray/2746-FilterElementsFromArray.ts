// Last updated: 02/03/2026, 13:58:15
type Fn = (n: number, i: number) => any;

function filter(arr: number[], fn: Fn): number[] {
  const ans: number[] = [];
  arr.forEach((a, index) => {
    if (fn(a, index)) {
      ans.push(a);
    }
  });
  return ans;
}