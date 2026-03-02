// Last updated: 02/03/2026, 13:58:17
declare global {
  interface Array<T> {
    groupBy(fn: (item: T) => string): Record<string, T[]>;
  }
}

Array.prototype.groupBy = function (fn) {
  const ans: Record<string, any[]> = {};
  for (const item of this) {
    const key = fn(item);
    if (ans[key] === undefined) {
      ans[key] = [];
    }
    ans[key].push(item);
  }
  return ans;
};